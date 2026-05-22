# pcu-2026
배재대학교 AI 교육

## Google Workspace Labs
[Workspace Experiments](https://workspace.google.com/experiments/)

Google Workspace Experiments는 Google이 제공하는 실험적 기능(Test Features)들을 미리 사용해볼 수 있는 프로그램으로, 
특히 Google Docs, Gmail, Sheets, Slides 등의 Google Workspace 앱에 
생성형 AI 기능을 통합해 사용자 생산성을 향상시키는 것을 목표로 합니다.

## Claude Artifacts
https://claude.ai/artifacts

### 취침 동화 생성기
https://claude.ai/public/artifacts/22dc6903-eff9-4c49-a690-2b17d8020d95

### AAC 음성 퀴즈 게임 (발달 장애아이들용 교구 앱)
https://claude.ai/public/artifacts/13f22a87-15af-4319-bfea-4661ef3dd00a

## 모바일 앱 실습 — AI Artifact App

Claude Artifact로 만든 웹앱을 **Expo + React Native WebView**로 감싸,
스마트폰 앱처럼 실행되도록 만드는 실습 프로젝트입니다.
위 **AAC 음성 퀴즈 게임**을 모바일 앱 화면 안에서 실행되도록 감쌌습니다.

새 앱을 처음부터 개발하는 것이 아니라, 기존 웹 URL을 "앱 껍데기"로 감싸는
하이브리드 앱 방식이며, Android APK 빌드까지 다룹니다. 보여줄 웹 주소는
`service-url.json` 파일만 바꾸면 교체할 수 있습니다.

- 프로젝트 폴더: [ai-artifact-app/](ai-artifact-app/)
- **실습 가이드 (설치 · 실행 · 주소 변경 · APK 빌드): [ai-artifact-app/README.md](ai-artifact-app/README.md)**

## 데스크톱 앱 실습 — AI Artifact Desktop

같은 웹앱을 이번엔 **Electron**으로 감싸, 윈도우 PC에서 실행되는
**데스크톱 앱**으로 만드는 실습 프로젝트입니다.
모바일 실습의 WebView 래핑과 같은 아이디어를, 스마트폰 대신 PC 창으로 옮긴 것입니다.

스마트폰·Expo Go·클라우드 빌드 없이, 명령 한 줄로 내 PC에 창이 바로 뜨며,
다른 PC에 설치할 수 있는 Windows 설치 파일(`.exe`) 만들기까지 다룹니다.
보여줄 웹 주소는 `service-url.json` 파일만 바꾸면 교체할 수 있습니다.

- 프로젝트 폴더: [ai-artifact-desktop/](ai-artifact-desktop/)
- **실습 가이드 (설치 · 실행 · 주소 변경 · .exe 빌드): [ai-artifact-desktop/README.md](ai-artifact-desktop/README.md)**

