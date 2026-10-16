# 장면 3+ · Coding Agent 세 가지 환경 — Claude Code CLI · Codex CLI · VS Code

같은 과제를 **세 가지 환경**에서 보여 줍니다. 하는 일(계획 → 코드 작성 → 테스트 실행 → 고침)은 같고, **도구와 보는 방법**만 다릅니다.

| | **Claude Code CLI** | **Codex CLI** | **VS Code** (Claude Code · Codex 확장) |
| --- | --- | --- | --- |
| 만든 곳 · 로그인 | Anthropic · Claude 구독 | OpenAI · ChatGPT 구독 | 편집기 안에서 위 둘 중 하나 |
| 화면 | 터미널 | 터미널 | 왼쪽 코드 + 오른쪽 대화 패널 |
| 잘 보이는 것 | 루프(계획 → 실행 → 결과 → 다시) | 같은 루프, 다른 에이전트의 방식 | 바뀐 코드의 **나란히 비교(diff)** 와 줄마다 승인 |
| 계획 먼저 | `Shift+Tab` → plan 모드, `/plan` | 프롬프트에 "계획만 먼저" | 모드 표시 → plan, `/plan` (Claude Code) |
| 권한 정하기 | `Shift+Tab`으로 권한 모드 | `/permissions` | 모드 표시 (Claude Code) |
| 프로젝트 설명 파일 | `/init` → `CLAUDE.md` | `/init` → `AGENTS.md` | 같음 |
| 바뀐 것 검토 | `git diff` · `/rewind` | `/review` (고치지 않고 검토만) | diff 화면 · 되돌리기 단추 |
| 한 번만 실행 (스크립트용) | `claude -p "…"` | `codex exec "…"` | — |

**강의에서는** 같은 과제를 세 환경에서 이어서 보여 줍니다: **Claude Code CLI로 계획 · 테스트 루프 → Codex CLI에게 같은 폴더를 검토(`/review`)시키기 → VS Code로 열어 diff를 읽고 승인**. 과제와 실제 결과물은 [예시 · 습관대로 만든 '뉴스 3개' 웹앱](../examples/news3_app/README.md)과 같습니다.

---

## 공통 준비 (수업 전)

Windows라면 먼저 [WSL에서 시작하는 실습 환경](../wsl_setup.md) 1~3단계를 합니다.

| 확인 | 명령 · 방법 | 이렇게 나오면 OK |
| --- | --- | --- |
| Claude 구독 | Pro · Max · Team · Enterprise (API 키 없이 로그인) | — |
| ChatGPT 구독 (Codex) | Plus 이상 권장 (API 키 없이 "Sign in with ChatGPT") | — |
| Node.js (Codex를 npm으로 설치할 때) | `node -v` | v22 이상 |
| 구독 대신 API로 과금되지 않게 | WSL · macOS `echo $ANTHROPIC_API_KEY` / PowerShell `$env:ANTHROPIC_API_KEY` | **아무것도 안 나옴** |
| 깨끗한 작업 환경 | 강의 PC: `wsl -d cc-live` ([강사 준비표 6번](../../instructor/wsl_demo_setup.md)) | Ubuntu 프롬프트 |
| 빈 폴더 | `mkdir ~/news3 && cd ~/news3 && git init` | `Initialized empty Git repository` |
| Python | `python3 --version` | 3.10 이상 |

---

## A. Claude Code CLI (약 4분)

### A-1 · 설치와 로그인

```bash
curl -fsSL https://claude.ai/install.sh | bash      # WSL · macOS · Linux
claude --version
cd ~/news3 && claude                                # 처음이면 브라우저 로그인 주소가 나옴 → 시크릿 창에서 열기
```

Windows PowerShell에 바로 설치한다면 `irm https://claude.ai/install.ps1 | iex`. 설치 명령은 바뀔 수 있으니 [공식 문서](https://code.claude.com/docs/en/setup)에서 한 번 더 확인합니다.

### A-2 · 계획부터 (plan 모드)

`Shift+Tab`을 눌러 아래 상태 줄이 **plan mode**가 될 때까지 바꾼 뒤 보냅니다.

```
주제를 입력하면 뉴스 3개를 골라 보여 주는 웹앱을 만들 거야. 바로 코드를 쓰지 말고 계획부터 보여 줘.
- 가장 작은 버전부터: 첫 단계는 '기사 목록에서 3개 고르는 함수 하나와 테스트'만. 파일 3개 이내.
- 규칙으로 되는 일(7일 지난 기사 빼기, 같은 소식 합치기)은 코드로, 무엇이 중요한지는 AI가 판단.
- 키는 환경 변수로만. 파일 삭제 · 배포는 먼저 물어봐.
```

**보여 줄 것:** 코드를 한 줄도 쓰지 않고 계획만 보여 주고 멈춥니다. 계획에 웹 화면 · 배포가 없는지 확인하고 승인합니다.

### A-3 · 테스트 먼저 → 실패 → 통과 (루프가 보이는 장면)

```
코드를 쓰기 전에 테스트부터 써 줘. 7일 지난 기사 제외, 같은 소식 합치기, 3개가 안 되면 있는 만큼만, 빈 입력.
AI 판단은 가짜 함수로 바꿔서 실제 API를 부르지 않게. 테스트를 돌려 실패하는 걸 보여 주고, 그다음 통과하도록 채워 줘.
```

**보여 줄 것**

- 파일을 만들거나 명령(`python3 -m unittest …`)을 실행하기 전에 **허락을 묻는 화면**: 무엇을 실행하는지 읽고 허용합니다.
- 테스트가 **실패(FAILED)** → 코드를 채움 → 다시 실행 → **OK**. 이것이 DAY 1에서 본 Agent Loop(계획 → 도구 → 관찰 → 다시 계획)입니다.
- 끝나면 `테스트 통과했으면 커밋해 줘` → `git log --oneline`으로 확인

### A-4 · 되돌리기 맛보기

`Esc`를 두 번 누르거나 `/rewind` → 이전 메시지 시점으로 대화 · 코드를 되돌릴 수 있음을 보여 줍니다 (실제로 되돌리지는 않아도 됨).

| CLI에서 쓸 키 · 명령 | 하는 일 |
| --- | --- |
| `Shift+Tab` | 권한 모드 바꾸기 (plan 모드 포함) |
| `Esc` | 지금 하는 일 멈추기 |
| `Esc` 두 번 · `/rewind` | 이전 시점으로 되돌리기 |
| `@파일이름` | 파일을 가리켜 보여 주기 |
| `/init` | 프로젝트 설명 파일(CLAUDE.md) 만들기 |
| `/mcp` | 연결된 MCP 서버 보기 |
| `/logout` | 시연 뒤 로그아웃 (공용 PC) |

---

## B. Codex CLI (약 2분)

같은 폴더(`~/news3`)를 이번에는 **다른 회사의 Coding Agent**에게 보여 줍니다.

### B-1 · 설치와 로그인

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh    # macOS · Linux · WSL
# 또는 npm install -g @openai/codex                      # Node.js 22 이상
codex --version
cd ~/news3 && codex                                       # 처음이면 "Sign in with ChatGPT" → 브라우저(시크릿 창)
```

### B-2 · 고치지 말고 검토만 시키기

```
/review
```

또는

```
이 폴더의 코드와 테스트를 읽고, 같은 소식을 합치는 규칙에서 놓칠 수 있는 경우를 3개만 짚어 줘. 파일은 고치지 마.
```

**보여 줄 것**

- `/permissions`로 **무엇을 묻지 않고 해도 되는지** 정하는 화면 (처음에는 편집 · 명령 실행 전에 묻도록)
- `/review`는 작업 폴더를 **고치지 않고** 검토 결과만 우선순위로 보여 줍니다. A에서 Claude Code가 만든 코드를 Codex가 검토하는 장면 — "에이전트끼리도 서로 확인시킬 수 있다"
- Claude Code와 무엇이 다른지: 계획을 보여 주는 방식, 묻는 시점, 답의 길이. **우열이 아니라 방식의 차이**를 봅니다.

| Codex에서 쓸 명령 | 하는 일 |
| --- | --- |
| `/permissions` | 묻지 않고 해도 되는 일(편집 · 명령 실행) 정하기 |
| `/model` | 모델과 추론 수준 고르기 |
| `/review` | 바뀐 것을 고치지 않고 검토 |
| `/init` | 프로젝트 설명 파일 `AGENTS.md` 만들기 |
| `codex exec "…"` | 한 번만 실행하고 끝내기 (스크립트 · 메신저 비서가 부를 때) |

## C. VS Code (약 3분)

### C-1 · 설치

1. [VS Code](https://code.visualstudio.com/) 설치 (1.94 이상)
2. VS Code에서 `Ctrl+Shift+X`(맥 `Cmd+Shift+X`) → **Claude Code** 검색 → **Install** (만든 곳: Anthropic)
3. (선택) **Codex** 확장도 같은 방법으로 검색해 설치할 수 있습니다 (만든 곳: OpenAI). 한 편집기에서 두 에이전트를 나란히 쓸 수 있습니다.
4. **강의 PC(WSL)에서 연다면:** VS Code 확장에서 **WSL**도 설치 → WSL 터미널의 프로젝트 폴더에서 `code .` → VS Code 왼쪽 아래에 `WSL: …`이 보이면 WSL 안에서 열린 것입니다.

확장 프로그램에는 Claude Code가 들어 있어서, 대화 패널만 쓸 때는 CLI를 따로 설치하지 않아도 됩니다. VS Code 아래 터미널에서 `claude`를 치려면 A-1의 CLI 설치가 필요합니다.

### C-2 · 열기와 로그인

1. 파일 하나를 연 상태에서 편집기 오른쪽 위의 **불꽃(Spark) 아이콘**을 누르면 Claude 패널이 열립니다. 왼쪽 막대의 같은 아이콘은 대화 목록입니다.
2. 처음이면 **Sign in** → 브라우저에서 구독 계정으로 승인 (공용 PC면 시크릿 창)
3. `Ctrl+Esc`(맥 `Cmd+Esc`)로 편집기 ↔ Claude 입력창을 오갑니다.

### C-3 · A에서 만든 코드를 VS Code로 열어 '읽고 승인'하기

같은 `~/news3` 폴더를 VS Code로 열고 이어서 시킵니다.

```
@pick.py 에서 같은 소식을 합치는 규칙이 제목이 길면 잘 안 될 것 같아. 고치기 전에 긴 제목으로 재현하는 테스트를 먼저 추가하고, 그다음 고쳐 줘.
```

**보여 줄 것**

- **diff 화면:** 원래 코드와 바뀐 코드가 나란히 보이고, 변경마다 **Accept this change / Reject this change** 단추가 있습니다. 한 줄씩 읽고 승인합니다. 마음에 안 들면 diff에서 직접 고쳐도 되고, Claude는 사람이 고친 것을 알고 이어 갑니다.
- **코드 선택 + `Alt+K`:** `_same_story` 함수를 마우스로 선택하고 `Alt+K` → 입력창에 `@pick.py#24-30`처럼 줄 번호가 들어갑니다. "이 부분만 설명해 줘"처럼 좁혀 물을 수 있습니다.
- **모드 표시:** 프롬프트 아래 모드 표시를 눌러 plan · 수동 승인 등을 바꿉니다. 처음에는 수동 승인(편집마다 묻기)으로 둡니다.
- **되돌리기:** 메시지에 마우스를 올려 **Rewind code to here**(코드만 그 시점으로) 를 보여 줍니다.
- **통합 터미널**(`` Ctrl+` ``)에서 `python3 -m unittest discover -s tests` → 사람이 직접 결과 확인

검은 터미널이 익숙하면 설정 → Extensions → Claude Code → **Use Terminal**을 켜서 VS Code 안에서 CLI 화면으로 쓸 수도 있습니다.

---

## 시연 대본 (10분)

| 시간 | 환경 | 말할 것 |
| --- | --- | --- |
| 0:00 | Claude Code CLI | "같은 과제를 세 환경으로 봅니다. 먼저 터미널에서 계획부터." (A-2) |
| 1:30 | Claude Code CLI | "테스트를 먼저 쓰게 하고 실패를 봅니다. 실패 → 고침 → 통과, 이게 루프입니다." (A-3) |
| 4:00 | Codex CLI | "다른 회사의 에이전트에게 같은 폴더를 검토만 시킵니다. 고치지 않고 짚기만." (B-2) |
| 6:00 | VS Code | "이번엔 편집기로 열어서, 바뀐 코드를 눈으로 읽고 줄마다 승인합니다." (C-3 diff) |
| 8:30 | VS Code | "되돌리기 단추, 그리고 마지막 확인은 사람이 터미널에서." |
| 9:30 | — | "도구는 달라도 습관은 같습니다: 작게 · 테스트 먼저 · diff 읽기 · 자주 커밋 · 키는 .env." |

시간이 부족하면 A-3 대신 [예시 저장소](../examples/news3_app/README.md)의 커밋 기록과 결과를 보여 주고, B-2 · C-3만 라이브로 합니다.

## 끝내기 (공용 PC)

1. Claude Code `/logout`, Codex 로그아웃(`codex logout`), VS Code 패널에서도 로그아웃
2. `cc-live` WSL 정리 ([강사 준비표 5번](../../instructor/wsl_demo_setup.md#5-수업이-끝나면--공용-pc-정리-10분))

## 직접 코드를 만들고 실행하는 예시 모음

| 예시 | 무엇 | 실제 실행 |
| --- | --- | --- |
| [뉴스 3개 웹앱](../examples/news3_app/README.md) | 습관 5개를 지키며 만든 웹앱 · 테스트 10개 · 커밋 6개 | 테스트 · 화면 실행 결과 기록 (실제 API 판단은 미실행) |
| [회의록 정리기 (장면 3 원본)](claude_code_meeting_todo.md) | 명세 한 장 → FastAPI 앱 + 테스트 + 안전 테스트 | 강의 시연용 순서 |
| [미니 에이전트 루프](../../day2/advanced/4_agent_loop/) | 계획 → 도구 → 관찰 → 승인 루프를 150줄로 | `python3 agent_loop.py --no` 실행 결과 기록 |
| [메신저 비서가 Coding Agent 부르기](5_messenger_to_coding_agent.md) | 디스코드에서 말로 시키면 Hermes · OpenClaw가 Claude Code · Codex를 실행 | 강사 라이브용 |

출처 (2026년 10월 16일 확인): [Claude Code · VS Code](https://code.claude.com/docs/en/vs-code) · [Claude Code 설치](https://code.claude.com/docs/en/setup) · [Codex CLI](https://learn.chatgpt.com/docs/codex/cli)
