# AI Artifact Desktop — Electron 래핑 실습

생성형 AI 강의 실습용 프로젝트입니다.
**웹앱(Claude Artifact)을 데스크톱 앱 창 안에서 실행되도록 감싸는** PC용 프로토타입입니다.

> ⚠️ 이 실습은 새 앱을 처음부터 개발하는 것이 아닙니다.
> 이미 있는 웹 URL을 **Electron**이라는 "앱 껍데기"로 감싸는 **하이브리드 앱** 방식입니다.
> 모바일 실습([ai-artifact-app](../ai-artifact-app/))의 WebView 래핑과 같은 아이디어를,
> 스마트폰 대신 **Windows PC 창**으로 옮긴 것입니다.
> 빠르게 데모할 수 있지만, 인터넷이 끊기면 동작하지 않습니다.

---

## 0. 준비물

| 항목 | 설명 |
|---|---|
| Windows PC | Node.js / npm 설치 완료 (강사가 미리 확인) |
| 네트워크 | 인터넷 연결 (웹앱을 실시간으로 불러옴) |

> 💡 **명령어를 입력하는 곳**: VSCode 화면 아래쪽의 **터미널(PowerShell)** 입니다.
> 메뉴 `Terminal → New Terminal` 로 열 수 있습니다.

> 💡 모바일 실습과 달리 **스마트폰·Expo Go·Expo 계정이 필요 없습니다.**
> 앱이 내 PC 안에서 창으로 바로 실행됩니다.

---

## 1. 프로젝트 폴더로 이동하기

터미널을 열면 가장 먼저 실습 폴더 안으로 들어가야 합니다.

```powershell
cd ai-artifact-desktop
```

- `cd` 는 "폴더 이동(change directory)" 명령입니다.
- 이동에 성공하면 터미널 줄 앞의 경로가 `...\ai-artifact-desktop` 으로 바뀝니다.
- 앞으로 나오는 모든 명령은 **이 폴더 안에서** 실행합니다.

---

## 2. 의존성 설치하기 (`npm install`)

이 앱은 `electron`, `electron-builder` 같은 **외부 부품(패키지)** 을 사용합니다.
그 부품들이 모인 `node_modules` 폴더가 있어야 앱이 실행됩니다.

### 내 폴더에 `node_modules` 폴더가 있나요?

VSCode 왼쪽 파일 목록에서 `node_modules` 폴더가 보이는지 확인하세요.

| 상황 | 해야 할 일 |
|---|---|
| **`node_modules` 폴더가 없음** (GitHub/ZIP으로 받은 경우 대부분 여기 해당) | 아래 `npm install` **반드시 실행** |
| **`node_modules` 폴더가 이미 있음** (강사가 통째로 복사해 준 경우) | `npm install` **생략 가능**, 바로 3장으로 |

```powershell
npm install
```

- `package.json` 파일에 적힌 부품 목록을 보고, 인터넷에서 자동으로 내려받습니다.
- Electron 본체가 수백 MB라 **1~5분** 정도 걸릴 수 있습니다. (인터넷 속도에 따라 다름)
- `added ... packages` 같은 메시지가 나오고 다시 입력 줄이 보이면 완료입니다.
- ⚠️ 이 단계를 건너뛰면 3장에서 `'electron'은(는) ... 인식할 수 없습니다` 오류가 납니다.

> 강의장 인터넷이 느릴 수 있으니, **수업 시작 전에 미리** 실행해 두는 것을 권장합니다.

---

## 3. PC에서 실행하기 (`npm start`) — 가장 먼저 해 볼 것

```powershell
npm start
```

- `package.json` 의 `"start"` 에 적힌 `electron .` 명령이 실행됩니다.
- 잠시 뒤 **데스크톱 창**이 하나 열립니다.

창에서 다음 순서로 보이면 **성공**입니다.

1. 빙글빙글 도는 로딩 표시 + "앱을 불러오는 중입니다..." 메시지
2. 웹 서비스 화면 표시

테스트를 끝내려면 **창을 닫거나**, 터미널에서 **`Ctrl + C`** 를 누릅니다.

> 💡 모바일 실습은 QR 코드를 폰으로 스캔했지만, 데스크톱 실습은
> 명령 한 줄로 **내 PC에 바로 창이 뜹니다.** 네트워크 차단(터널 모드) 걱정이 없습니다.

---

## 4. 웹 서비스 주소 바꾸기 (`service-url.json`)

이 앱이 보여주는 웹 서비스 주소는 코드(`main.js`)가 아니라 **별도 파일** [service-url.json](service-url.json) 에 분리되어 있습니다.
다른 웹 서비스로 바꾸고 싶으면 **이 파일 하나만** 수정하면 됩니다. 코드는 건드릴 필요가 없습니다.

`service-url.json` 파일 내용:

```json
{
  "_comment": "앱이 보여줄 웹 서비스 주소입니다. 아래 url 값(따옴표 안)만 바꾸세요.",
  "url": "https://claude.ai/public/artifacts/13f22a87-15af-4319-bfea-4661ef3dd00a"
}
```

**바꾸는 방법**

1. VSCode에서 `service-url.json` 파일을 엽니다.
2. `"url"` 값의 **큰따옴표 안 주소만** 원하는 주소로 바꿉니다.
3. 파일을 저장합니다 (`Ctrl + S`).
4. 앱에 반영하기: 열려 있는 창을 닫고 `npm start` 를 다시 실행합니다.

**주의사항 (JSON 문법)**

- 큰따옴표 `"`, 중괄호 `{ }`, 콜론 `:`, 쉼표 `,` 같은 기호는 **그대로 두어야** 합니다.
- 주소는 반드시 큰따옴표 `" "` 안에 넣습니다.
- `"_comment"` 줄은 설명용이니 건드리지 마세요. (없어도 동작은 합니다)

> 💡 동작 원리: `main.js` 가 이 파일을 `require('./service-url.json')` 으로
> 읽어서 `ARTIFACT_URL` 에 넣습니다. 그래서 주소를 바꿔도 코드 수정이 필요 없습니다.

---

## 5. 실행 화면 점검 체크리스트

앱이 떴다면 아래 항목을 직접 확인해 보세요.

- [ ] 로딩 표시("앱을 불러오는 중입니다...")가 잠깐 보였는가
- [ ] 웹 서비스 화면이 정상적으로 표시되는가
- [ ] 창 크기를 마우스로 늘리거나 줄여도 화면이 따라오는가
- [ ] 웹앱 안의 버튼·입력 등이 정상 동작하는가
- [ ] 인터넷을 끄고 다시 실행하면 오류 화면이 뜨는가 (의도된 동작)
- [ ] `service-url.json` 의 주소를 바꿔 보고, 다른 웹 화면이 뜨는가

---

## 6. (참고) 이 프로젝트는 이렇게 만들어졌습니다

이미 완성된 폴더를 받았다면 이 장은 읽기만 해도 됩니다. 직접 처음부터 만들고 싶을 때 참고하세요.

```powershell
# (1) 폴더를 만들고 들어갑니다
mkdir ai-artifact-desktop
cd ai-artifact-desktop

# (2) package.json 생성 (질문에 기본값으로 Enter)
npm init -y

# (3) Electron + 빌드 도구 설치 (개발용 의존성)
#     7zip-bin: predist 스크립트가 빌드 도구 압축을 푸는 데 사용
npm install --save-dev electron electron-builder 7zip-bin
```

그 뒤 `package.json` 의 `"main"` 을 `main.js` 로 바꾸고,
`"scripts"` 에 `start`·`dist` 를, 그리고 `electron-builder` 용 `"build"` 설정을 추가합니다.

프로젝트의 주요 파일:

| 파일 | 역할 |
|---|---|
| [service-url.json](service-url.json) | **보여줄 웹 서비스 주소** (수강생이 바꾸는 파일) |
| [main.js](main.js) | Electron 메인 코드 — 창을 만들고 주소를 불러와 표시 |
| [renderer/loading.html](renderer/loading.html) | 불러오는 동안 보여줄 로컬 로딩 화면 |
| [renderer/error.html](renderer/error.html) | 불러오기 실패 시 보여줄 로컬 오류 화면 |
| [scripts/prepare-wincodesign.js](scripts/prepare-wincodesign.js) | 빌드 전 자동 실행 — 빌드 도구 권한 문제를 미리 해결 (9장 참고) |
| [package.json](package.json) | 앱 이름, 실행 스크립트, `electron-builder` 빌드 설정 |

> 💡 모바일 실습의 `App.tsx`(WebView) ↔ 데스크톱 실습의 `main.js`(BrowserWindow) 가
> 서로 대응됩니다. 둘 다 "웹 주소를 앱 화면 안에 띄운다"는 같은 일을 합니다.

---

## 7. 설치 파일(.exe) 만들기 — `electron-builder`

여기서부터는 다른 PC에도 설치할 수 있는 **Windows 설치 파일(`.exe`)** 을 만드는 단계입니다.
설치 파일은 `electron-builder` 도구로 만듭니다. **클라우드 빌드 없이 내 PC에서 바로 만듭니다.**

> 💡 모바일 실습은 APK를 Expo 클라우드(EAS)에서 빌드했지만,
> 데스크톱 실습은 **내 PC에서 직접** 설치 파일을 만듭니다. Expo 계정이 필요 없습니다.

`electron-builder` 는 2장 `npm install` 단계에서 이미 설치되었으므로, 추가 설치는 없습니다.

---

## 8. `package.json` 의 `build` 설정

이 프로젝트의 [package.json](package.json) 에는 빌드 설정이 **이미 포함**되어 있어 따로 만들 필요가 없습니다.

```json
"build": {
  "appId": "com.example.aiartifactdesktop",
  "productName": "AI Artifact Desktop",
  "files": ["main.js", "service-url.json", "renderer/**/*"],
  "win": { "target": "nsis" },
  "nsis": { "oneClick": false, "allowToChangeInstallationDirectory": true }
}
```

- `appId` : 앱을 구분하는 고유 이름입니다.
- `productName` : 설치될 앱의 표시 이름입니다.
- `files` : 설치 파일에 포함할 파일 목록입니다. (`node_modules` 는 자동 포함)
- `win.target: "nsis"` : Windows용 **설치 마법사 형식(.exe)** 으로 만든다는 뜻입니다.
- `nsis` : 설치할 때 사용자가 설치 폴더를 고를 수 있게 합니다.

---

## 9. 빌드 명령어

```powershell
npm run dist
```

- `npm run dist` 는 두 단계를 자동으로 실행합니다.
  1. **`predist`** (`scripts/prepare-wincodesign.js`) — 빌드 도구를 미리 준비 (아래 설명)
  2. **`dist`** (`electron-builder --win`) — 실제 설치 파일 빌드
- 빌드는 **내 PC에서** 진행됩니다 (인터넷이 빠르면 처음 한 번만 빌드 도구를 내려받음, 약 **2~5분**).
- 완료되면 프로젝트 안에 **`dist` 폴더**가 생기고, 그 안에
  `AI Artifact Desktop Setup 1.0.0.exe` 같은 **설치 파일**이 들어 있습니다.
- 그 `.exe` 파일을 실행하면 다른 PC에도 앱을 설치할 수 있습니다.

> 💡 설치 없이 바로 실행되는 형태가 필요하면 `win.target` 을 `"portable"` 로 바꾸면 됩니다.

### `predist` 스크립트 — `Cannot create symbolic link` 오류 자동 해결

electron-builder는 빌드 시 코드 서명 도구(`winCodeSign`)를 내려받아 압축을 푸는데,
그 안에는 macOS용 **심볼릭 링크** 파일이 있습니다. Windows에서 심볼릭 링크를 만들려면
**관리자 권한 또는 개발자 모드**가 필요해, 권한이 없는 PC에서는 아래 오류로 빌드가 멈춥니다.

```
ERROR: Cannot create symbolic link : 클라이언트는 필요한 권한을 가지고 있지 않습니다.
  ... winCodeSign ... libcrypto.dylib
```

이 프로젝트에는 [scripts/prepare-wincodesign.js](scripts/prepare-wincodesign.js) 가 포함되어 있어,
`npm run dist` 를 실행하면 **빌드 전에 자동으로** 이 도구를 macOS 폴더(심볼릭 링크)만
제외하고 미리 풀어 둡니다. 그래서 **관리자 권한·개발자 모드 없이도, 어떤 PC에서든**
`npm run dist` 한 줄이면 빌드가 됩니다. (수강생이 따로 할 일은 없습니다.)

> 💡 만약 회사·연구소 정책 등으로 자동 준비가 막힌다면, 대안으로 Windows
> **개발자 모드**(`설정 → 개인 정보 및 보안 → 개발자용`)를 켜거나, 터미널을
> **관리자 권한으로 실행**한 뒤 `npm run dist` 를 다시 시도하세요.

---

## 10. 설치 파일 사용 시 주의사항

1. **Windows SmartScreen 경고**: 코드 서명을 하지 않은 설치 파일이라
   "Windows의 PC 보호" 경고가 뜰 수 있습니다. `추가 정보 → 실행`을 눌러야 설치됩니다.
2. **인터넷 연결 필수**: 웹앱을 실시간으로 불러오므로 오프라인에서는 동작하지 않습니다.
3. **공유 URL 접근 권한 (가장 중요)**: Claude Artifact 주소가 비공개이거나
   접근이 제한되면 창이 빈 화면/오류 화면을 보일 수 있습니다.
   실습 전에 PC 브라우저 **시크릿 모드**로 URL이 로그인 없이 열리는지 확인하세요.

---

## 11. 자주 발생하는 오류와 해결 방법

| 증상 | 원인 | 해결 |
|---|---|---|
| `'electron'은(는) ... 인식할 수 없습니다` | 2장 `npm install`을 안 함 | `npm install` 실행 후 다시 시도 |
| `'npm'은(는) ... 인식할 수 없습니다` | Node.js 미설치 | Node.js 설치 후 터미널 재시작 |
| 창이 안 뜨고 터미널만 멈춰 있음 | Electron 첫 실행이 느림 | 10~20초 기다리기, 안 되면 `Ctrl + C` 후 `npm start` 재시도 |
| 오류 화면("웹앱을 불러오지 못했습니다")만 보임 | 인터넷 끊김 / 주소 오타 | 네트워크 확인, `service-url.json` 의 `url` 값 점검 |
| 흰 화면만 보임 | URL이 비공개/차단됨 | 시크릿 모드로 URL 확인, Artifact를 공개 공유로 설정 |
| 주소를 바꿨는데 앱이 안 켜짐 | JSON 문법 깨짐 (따옴표·쉼표 등) | `service-url.json` 의 `{ } " :` 기호가 그대로인지 확인 |
| 주소를 바꿨는데 화면에 반영 안 됨 | 창을 다시 켜지 않음 | 창을 닫고 `npm start` 다시 실행 |
| `[prepare-wincodesign] ... 다운로드 실패` | 빌드 도구 다운로드 실패(네트워크) | 인터넷 확인 후 `npm run dist` 다시 실행 |
| `Cannot create symbolic link` (winCodeSign) | `predist` 자동 준비가 막힘 (정책 등) | 개발자 모드 켜기 또는 관리자 권한으로 재실행 (9장 참고) |
| 설치 파일 실행 시 SmartScreen 경고 | 코드 서명이 없음 | `추가 정보 → 실행` 클릭 (10장 참고) |
