# WSL에서 시작하는 실습 환경 (Windows)

Windows 노트북에서 **WSL(Windows 안의 리눅스, Ubuntu)** 을 켜고, 오늘 강의에서 본 것들을 같은 명령으로 따라 하는 순서입니다. 강사 화면도 WSL Ubuntu라서 **화면의 명령을 그대로** 칠 수 있습니다.

> **오늘 기본 실습(트랙 A0)은 WSL이 필요 없습니다.** 웹 브라우저의 AI 채팅만으로 완주합니다. 이 문서는 트랙 C(코딩 에이전트) · 강의 시연(Claude Code · Codex · VS Code · 메신저 비서)을 직접 해 보고 싶은 분용입니다. 처음 설치는 재부팅이 필요할 수 있으니 **집에서** 하는 것을 권합니다.

```
1 WSL 켜기 → 2 Ubuntu 기본 도구 → 3 실습 저장소 받기 · 예시 실행 → 4 Claude Code · Codex CLI → 5 VS Code 연결
→ (선택) 6 메신저 비서(Hermes · OpenClaw) → 7 정리
```

| 단계 | 시간 | 다 하면 할 수 있는 것 |
| --- | --- | --- |
| 1~3 | 20분 | 예시 웹앱 `news3_app` 실행, 테스트 10개 통과 확인 |
| 4 | 10분 | Claude Code CLI · Codex CLI로 코드 만들기 ([장면 3+](demo/3_coding_agents_three_ways.md)) |
| 5 | 10분 | VS Code에서 diff를 보며 승인 |
| 6 | 40분 | 디스코드로 메신저 비서 부르기 ([장면 0](demo/0_messenger_connect.md)) |

---

## 1 · WSL 켜기 (Windows 10 2004 이상 · Windows 11)

1. 시작 메뉴에서 **PowerShell**을 오른쪽 클릭 → **관리자로 실행**
2. 아래를 입력합니다.

   ```powershell
   wsl --install -d Ubuntu-24.04
   ```

3. 재부팅하라고 하면 재부팅합니다. 다시 켜지면 **Ubuntu** 창이 열립니다 (안 열리면 시작 메뉴에서 'Ubuntu').
4. **사용자 이름**(영어 소문자)과 **비밀번호**를 만듭니다. 비밀번호는 입력해도 화면에 안 보이는 것이 정상입니다.

**확인:** PowerShell에서 `wsl -l -v` → `Ubuntu-24.04`가 `Running` 또는 `Stopped`, VERSION `2`

| 이럴 때 | 이렇게 |
| --- | --- |
| '가상화를 켜야 한다'는 오류 | 컴퓨터 BIOS에서 가상화(Virtualization, VT-x · SVM)를 켭니다. 회사 노트북은 관리자에게 문의 |
| 관리자 권한이 없다 (회사 · 학교 PC) | WSL을 쓸 수 없습니다. 웹 실습(A0)으로 하고, 개인 노트북에서 해 봅니다 |
| 이미 WSL이 있다 | 재부팅 없이 Ubuntu만 추가됩니다 |

> **WSL 안의 파일은 Windows와 분리**되어 있습니다. 에이전트가 Windows의 내 문서를 건드리지 않게 하는 울타리 역할도 합니다. 다만 Windows 드라이브는 `/mnt/c`로 보이므로, 에이전트에게 그 경로를 맡기지 않습니다.

## 2 · Ubuntu 기본 도구 (10분)

Ubuntu 창에서 한 줄씩 붙여 넣습니다 (붙여 넣기: 마우스 오른쪽 클릭 또는 `Ctrl+Shift+V`).

```bash
sudo apt update && sudo apt install -y git python3 curl zip
curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
source ~/.bashrc
nvm install 22
```

**확인**

```bash
python3 --version     # 3.10 이상
node -v               # v22.x
git --version
```

## 3 · 실습 저장소 받기와 예시 실행 (5분)

```bash
cd ~
git clone https://github.com/aifrenz/pcu-2026.git
cd ~/pcu-2026/ai-agent-2026/day3/examples/news3_app
python3 -m unittest discover -s tests      # 마지막 줄에 OK (테스트 10개)
python3 app.py                             # http://127.0.0.1:8000
```

Windows 브라우저에서 `http://127.0.0.1:8000`을 엽니다 (WSL의 주소가 그대로 열립니다). **날짜 칸을 `2026-10-18`로 바꾸고** [`sample_articles.txt`](examples/news3_app/sample_articles.txt) 9줄을 붙여 넣어 결과를 봅니다. 끄기: Ubuntu 창에서 `Ctrl+C`.

## 4 · Claude Code · Codex CLI (10분)

**먼저 확인:** 구독으로 쓰려면 API 키 환경 변수가 **비어 있어야** 합니다.

```bash
echo $ANTHROPIC_API_KEY      # 아무것도 안 나오면 OK
```

**Claude Code** (Claude Pro 이상 구독)

```bash
curl -fsSL https://claude.ai/install.sh | bash
claude --version
mkdir -p ~/news3 && cd ~/news3 && git init
claude                       # 처음이면 로그인 주소 → Windows 브라우저에서 열어 구독 계정으로 승인
```

**Codex CLI** (ChatGPT 구독)

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh     # 또는 npm install -g @openai/codex
codex --version
cd ~/news3 && codex          # "Sign in with ChatGPT" 선택
```

설치 명령은 바뀔 수 있으니 [Claude Code 설치 문서](https://code.claude.com/docs/en/setup) · [Codex CLI 문서](https://learn.chatgpt.com/docs/codex/cli)에서 한 번 더 확인하세요. 이어서 [장면 3+ · 세 가지 환경](demo/3_coding_agents_three_ways.md)의 A · B 순서대로 해 봅니다.

## 5 · VS Code를 WSL에 연결 (10분)

1. Windows에 [VS Code](https://code.visualstudio.com/) 설치
2. VS Code에서 `Ctrl+Shift+X` → **WSL**(Microsoft) 설치, **Claude Code**(Anthropic) 설치, (선택) **Codex**(OpenAI) 설치
3. Ubuntu 창에서 프로젝트 폴더로 가서 엽니다.

   ```bash
   cd ~/news3 && code .
   ```

4. VS Code 왼쪽 아래에 **`WSL: Ubuntu-24.04`** 가 보이면 WSL 안에서 열린 것입니다.
5. 편집기 오른쪽 위 **불꽃(Spark) 아이콘** → **Sign in** → [장면 3+의 C 순서](demo/3_coding_agents_three_ways.md#c-vs-code-약-3분)대로 diff를 읽고 승인해 봅니다. 아래 터미널(`` Ctrl+` ``)도 WSL의 Ubuntu입니다.

## 6 · (선택) 메신저 비서 — Hermes · OpenClaw

명령 실행 · 파일 접근 권한을 가진 비서라, 내 노트북이라면 **WSL을 하나 더 만들어 그 안에서만** 쓰는 것을 권합니다.

```powershell
# PowerShell: 지금 Ubuntu를 복제해 비서 전용 환경 만들기
wsl --terminate Ubuntu-24.04
mkdir C:\wsl
wsl --export Ubuntu-24.04 C:\wsl\base.tar
wsl --import agent C:\wsl\agent C:\wsl\base.tar
wsl -d agent
```

복제본은 root로 로그인되므로, 복제본 안에서 `/etc/wsl.conf`에 아래를 넣고 PowerShell에서 `wsl --terminate agent` 뒤 다시 엽니다 (`내사용자이름` = 1단계에서 만든 이름).

```
[boot]
systemd=true

[user]
default=내사용자이름
```

그다음 복제본(`wsl -d agent`) 안에서 설치합니다.

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash      # Hermes
hermes model            # 'ChatGPT or Codex Subscription' → 구독으로 로그인 (API 키 없이)
# 또는
curl -fsSL https://openclaw.ai/install.sh | bash                         # OpenClaw
openclaw onboard --install-daemon
```

메신저(디스코드 · 왓츠앱 · 라인) 연결은 [장면 0 · 메신저 연결](demo/0_messenger_connect.md#자세한-설치--연결-방법)을 따릅니다. 비서가 Claude Code · Codex를 부르게 하려면 [장면 5](demo/5_messenger_to_coding_agent.md)를 봅니다.

**주의:** 비서 게이트웨이는 열린 Ubuntu 창이 하나도 없으면 잠시 뒤 꺼질 수 있습니다. 쓰는 동안은 창 하나를 열어 둡니다.

## 7 · 정리

| 무엇 | 어떻게 |
| --- | --- |
| 로그인 | `claude` 안에서 `/logout`, `codex logout` |
| 봇 토큰 | 디스코드 Developer Portal → Bot → **Reset Token** |
| 비서 전용 환경 | PowerShell `wsl --unregister agent` (그 안의 토큰 · 로그인 · 파일이 모두 지워짐) |
| 기본 Ubuntu까지 지우기 | `wsl --unregister Ubuntu-24.04` (되돌릴 수 없음 — 필요한 파일은 먼저 옮기기) |
| 복제용 파일 | `C:\wsl\base.tar` 삭제 |

## 막힐 때

| 이럴 때 | 이렇게 |
| --- | --- |
| `curl: command not found` | 2단계의 `sudo apt install -y … curl`부터 |
| `node: command not found` (새 창에서) | `source ~/.bashrc` 또는 Ubuntu 창을 새로 열기 |
| `code: command not found` | VS Code를 Windows에 설치한 뒤 Ubuntu 창을 새로 열기 |
| 브라우저에서 `127.0.0.1:8000`이 안 열림 | Ubuntu 창에서 `python3 app.py`가 켜져 있는지 확인 |
| 로그인 주소가 안 열림 | 주소를 복사해 Windows 브라우저 주소창에 붙여 넣기 |
| Claude Code가 '사용량 과금'을 묻는다 | `echo $ANTHROPIC_API_KEY`가 비어 있는지 확인. 키를 쓸지 물으면 **No** |
| 회사 · 학교 망에서 설치가 끊김 | 휴대폰 핫스팟으로 바꿔 다시 |

강사가 강의 PC에서 쓴 준비 순서(복제 · USB 내보내기 · 정리 포함)는 [강사 준비표](../instructor/wsl_demo_setup.md)에 있습니다.
