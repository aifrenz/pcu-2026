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

## 개발 환경 준비 (VSCode · Node.js · Git)

아래 **모바일 앱 실습**과 **데스크톱 앱 실습**을 진행하려면, 먼저 PC에 세 가지 도구를 설치해야 합니다.
한 번만 설치하면 두 실습 모두에 사용됩니다.

| 도구 | 역할 | 다운로드 |
|---|---|---|
| **Node.js** | 앱을 실행·빌드하는 기반 도구 (`npm` 포함) | <https://nodejs.org> → **LTS** 버전 |
| **VSCode** | 코드를 보고 수정하는 편집기 (터미널 내장) | <https://code.visualstudio.com> |
| **Git** | 실습 코드를 GitHub에서 내려받는 도구 | <https://git-scm.com/download/win> |

### 설치 순서

1. **Node.js 설치**
   - [nodejs.org](https://nodejs.org) 에서 **LTS** 버튼을 눌러 설치 파일을 받습니다.
   - 받은 파일을 실행하고, 모든 단계에서 **Next**(또는 동의)를 눌러 설치합니다.
   - 패키지 설치 도구인 `npm` 이 함께 설치됩니다.

2. **VSCode 설치**
   - [code.visualstudio.com](https://code.visualstudio.com) 에서 Windows용 설치 파일을 받아 실행합니다.
   - 설치 중 "추가 작업 선택" 화면에서 **"Code(으)로 열기" 메뉴 추가** 항목을 체크하면 편리합니다.

3. **Git 설치**
   - [git-scm.com](https://git-scm.com/download/win) 에서 Windows용 설치 파일을 받아 실행합니다.
   - 선택 옵션이 많지만, **기본값 그대로 Next** 를 눌러 끝까지 설치하면 됩니다.

### 설치 확인

VSCode를 열고 메뉴 `Terminal → New Terminal` 로 터미널(PowerShell)을 연 뒤, 아래를 한 줄씩 입력합니다.

```powershell
node -v
npm -v
git --version
```

`v22.x.x`, `10.x.x`, `git version 2.x.x` 처럼 **버전 숫자**가 각각 나오면 설치 성공입니다.
`인식할 수 없습니다` 오류가 나면, 해당 도구를 다시 설치하고 **VSCode를 완전히 닫았다가 다시 여세요.**

### 실습 코드 내려받기

설치가 끝나면 이 저장소를 PC로 복제(clone)합니다.

```powershell
git clone https://github.com/aifrenz/pcu-2026.git
cd pcu-2026
```

그런 다음 VSCode 메뉴 `File → Open Folder` 로 `pcu-2026` 폴더를 열면 실습 준비가 끝납니다.

> 💡 강사가 ZIP 파일이나 폴더로 코드를 직접 나눠 준 경우, 이 단계는 생략하고
> 받은 폴더를 VSCode로 열면 됩니다.

---

## VSCode AI 코딩 도구 (확장 프로그램)

VSCode에 AI 코딩 도구를 확장 프로그램으로 설치하면, 편집기 안에서 AI와 대화하며
코드 작성·수정·설명을 맡길 수 있습니다. 도구별 설치·사용 가이드는 아래 문서를 참고하세요.

- **Claude** — [docs/vscode-claude.md](docs/vscode-claude.md)
- **Codex (OpenAI)** — [docs/vscode-codex.md](docs/vscode-codex.md)
- **Gemini (Google)** — [docs/vscode-gemini.md](docs/vscode-gemini.md)
- **로컬 LLM (Ollama + Continue)** — [docs/vscode-ollama-continue.md](docs/vscode-ollama-continue.md) — 인터넷 없이 무료로 쓰는 로컬 모델 코드 어시스트

---

## Claude 업무 활용 (협업 · 자동화)

Claude를 코드 작성을 넘어 **팀 협업과 업무 자동화**에 활용하는 방법입니다.
claude.ai 웹과 Claude Desktop 앱을 함께 사용하며, MCP·스킬·플러그인 개념 설명과
**폴더 파일 다루기 · 웹 크롤링 · 영수증 사진을 엑셀로 정리하기** 예제를 담았습니다.

- **Claude Cowork 활용 가이드** — [docs/claude-cowork.md](docs/claude-cowork.md)

---

## NotebookLM — 내 자료 기반 AI 실습

NotebookLM은 내가 올린 자료(출처)에 근거해 답하는 **RAG 방식 AI 도구**라
할루시네이션(환각)이 적습니다. 출처 추가 방법(파일·웹·YouTube), 출처 기반 질문으로
할루시네이션을 비교하는 실습, 오디오·인포그래픽·슬라이드 등 생성 기능을 다룹니다.

- **NotebookLM 실습 가이드** — [docs/notebooklm.md](docs/notebooklm.md)

---

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

