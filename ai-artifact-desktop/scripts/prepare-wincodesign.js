// scripts/prepare-wincodesign.js
// "npm run dist" 직전에 npm 이 자동으로 실행하는 준비 스크립트입니다.
// (package.json 의 "predist" 에 연결되어 있습니다.)
//
// ─── 왜 필요한가 ────────────────────────────────────────────────
// electron-builder 는 Windows 설치 파일을 만들 때 "winCodeSign" 이라는
// 도구 묶음을 내려받아 압축을 풉니다. 그 안에는 macOS 용 파일이
// "심볼릭 링크" 형태로 들어 있는데, Windows 에서 심볼릭 링크를 만들려면
// 관리자 권한 또는 개발자 모드가 필요합니다. 권한이 없는 PC 에서는
// 압축 해제가 실패하고 "Cannot create symbolic link" 오류로 빌드가 멈춥니다.
//
// ─── 이 스크립트가 하는 일 ──────────────────────────────────────
// Windows 빌드에 필요 없는 macOS(darwin) 폴더를 제외하고 winCodeSign 을
// 미리 풀어서 electron-builder 캐시에 넣어 둡니다. 심볼릭 링크가 아예
// 없으므로 권한이 필요 없고, electron-builder 는 이 캐시를 그대로 쓰므로
// 어떤 PC 에서도(관리자 권한·개발자 모드 없이) 빌드가 됩니다.

const fs = require('fs');
const os = require('os');
const path = require('path');
const https = require('https');
const { spawnSync } = require('child_process');

// macOS·Linux 에서는 심볼릭 링크 권한 문제가 없습니다 — 그대로 종료합니다.
if (process.platform !== 'win32') {
  console.log('[prepare-wincodesign] Windows 가 아니므로 건너뜁니다.');
  process.exit(0);
}

// electron-builder 25.x 가 사용하는 winCodeSign 버전 (오랫동안 고정되어 있음)
const VERSION = '2.6.0';
const ARCHIVE_URL =
  'https://github.com/electron-userland/electron-builder-binaries/releases/' +
  `download/winCodeSign-${VERSION}/winCodeSign-${VERSION}.7z`;

// electron-builder 캐시 위치: 보통 %LOCALAPPDATA%\electron-builder\Cache
const cacheBase =
  process.env.ELECTRON_BUILDER_CACHE ||
  path.join(
    process.env.LOCALAPPDATA || path.join(os.homedir(), 'AppData', 'Local'),
    'electron-builder',
    'Cache'
  );
const winCodeSignDir = path.join(cacheBase, 'winCodeSign');
const destDir = path.join(winCodeSignDir, `winCodeSign-${VERSION}`);

// 이미 준비돼 있으면(rcedit 파일 확인) 다시 하지 않고 빠르게 넘어갑니다.
if (fs.existsSync(path.join(destDir, 'rcedit-x64.exe'))) {
  console.log('[prepare-wincodesign] 이미 준비돼 있습니다 — 건너뜁니다.');
  process.exit(0);
}

// 7za 실행 파일 경로 (electron-builder 와 함께 설치되는 7zip-bin 패키지)
const { path7za } = require('7zip-bin');

const tmp7z = path.join(winCodeSignDir, `winCodeSign-${VERSION}.download.7z`);

// GitHub 릴리스 주소는 다른 주소로 리다이렉트되므로 따라가며 내려받습니다.
function download(url, dest, cb) {
  https
    .get(url, (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        res.resume();
        return download(res.headers.location, dest, cb);
      }
      if (res.statusCode !== 200) {
        res.resume();
        return cb(new Error(`다운로드 실패 (HTTP ${res.statusCode})`));
      }
      fs.mkdirSync(path.dirname(dest), { recursive: true });
      const file = fs.createWriteStream(dest);
      res.pipe(file);
      file.on('finish', () => file.close(() => cb(null)));
      file.on('error', (err) => cb(err));
    })
    .on('error', (err) => cb(err));
}

console.log('[prepare-wincodesign] winCodeSign 도구를 준비합니다...');
console.log('[prepare-wincodesign] 1/2 내려받는 중...');

download(ARCHIVE_URL, tmp7z, (err) => {
  if (err) {
    console.error('[prepare-wincodesign] ' + err.message);
    console.error('[prepare-wincodesign] 인터넷 연결을 확인한 뒤 다시 시도하세요.');
    process.exit(1);
  }

  console.log('[prepare-wincodesign] 2/2 압축 해제 중 (macOS 파일 제외)...');
  // -xr!darwin : macOS(darwin) 폴더를 통째로 제외 → 심볼릭 링크가 없어 권한 불필요
  const result = spawnSync(
    path7za,
    ['x', tmp7z, `-o${destDir}`, '-xr!darwin', '-y'],
    { stdio: 'inherit' }
  );

  // 내려받은 임시 압축 파일은 지웁니다.
  fs.rmSync(tmp7z, { force: true });

  if (result.status !== 0) {
    console.error('[prepare-wincodesign] 압축 해제에 실패했습니다.');
    process.exit(1);
  }

  console.log('[prepare-wincodesign] 완료 — 이제 빌드를 진행합니다.');
});
