// main.js
// "AI Artifact Desktop" - 웹앱(Claude Artifact)을 Electron 창으로 감싸는 데스크톱 앱
// 핵심 개념: 새 앱을 개발하는 것이 아니라, 기존 웹앱을 데스크톱 창 안에 띄우는 방식입니다.
//            (모바일 실습의 WebView 래핑과 같은 아이디어를, PC 창으로 옮긴 것입니다.)

const { app, BrowserWindow } = require('electron');
const path = require('path');

// 웹 서비스 주소는 service-url.json 파일에 분리되어 있습니다.
// 주소를 바꿀 때는 이 코드가 아니라 service-url.json 의 "url" 값만 수정하세요.
const serviceConfig = require('./service-url.json');

// service-url.json 에서 읽어온 웹 서비스 주소
const ARTIFACT_URL = serviceConfig.url;

// 메인 창(앱 화면) 객체를 담아 둘 변수
let mainWindow = null;

// 앱 창을 만들고 화면을 띄우는 함수
function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1000,             // 창 가로 크기(px)
    height: 720,             // 창 세로 크기(px)
    title: 'AI Artifact Desktop',
    backgroundColor: '#ffffff', // 로딩 전 깜빡임(흰 화면)을 줄이기 위한 배경색
    webPreferences: {
      // 보안 기본값: 웹 페이지에서 Node.js 기능을 쓰지 못하게 막습니다.
      contextIsolation: true,
      nodeIntegration: false,
    },
  });

  // 파일/편집 같은 상단 메뉴 막대를 숨겨, 일반 앱처럼 보이게 합니다.
  mainWindow.setMenuBarVisibility(false);

  // 1) 먼저 로컬 "로딩 화면"을 보여줍니다.
  mainWindow.loadFile(path.join(__dirname, 'renderer', 'loading.html'));

  // 2) 웹 서비스 로딩에 실패하면 "오류 화면"으로 바꿉니다.
  //    did-fail-load: 페이지를 불러오지 못했을 때 발생하는 이벤트
  mainWindow.webContents.on('did-fail-load', (event, errorCode) => {
    // errorCode -3 은 리다이렉트 등으로 인한 정상적인 중단이라 무시합니다.
    if (errorCode === -3) return;
    mainWindow.loadFile(path.join(__dirname, 'renderer', 'error.html'));
  });

  // 3) 로딩 화면이 잠깐 보인 뒤, 실제 웹 서비스 주소를 불러옵니다.
  //    (loadURL 이 끝날 때까지 로딩 화면이 계속 보입니다.)
  setTimeout(() => {
    mainWindow.loadURL(ARTIFACT_URL);
  }, 400);

  // 창이 닫히면 변수도 비웁니다.
  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

// Electron 준비가 끝나면 창을 만듭니다.
app.whenReady().then(() => {
  createWindow();

  // macOS: Dock 아이콘을 눌렀을 때 창이 없으면 다시 만듭니다.
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

// 모든 창이 닫히면 앱을 종료합니다. (macOS 는 관례상 계속 떠 있게 둡니다.)
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});
