# 강사 준비 · 강의 PC의 WSL2에서 심화 시연하기

DAY 2 · 3 심화 시연(Hermes · OpenClaw · n8n · MCP · 에이전트 루프 · Claude Code)을 **강의실 Windows PC의 WSL2(Ubuntu)** 에서 진행하기 위한 준비표입니다. 수강생도 Windows에서 WSL2를 켜면 화면의 명령을 그대로 따라 할 수 있습니다.

| 원칙 | 이유 |
| --- | --- |
| 시연은 Windows가 아니라 **WSL 안의 Ubuntu** 에서 | 수강생이 집에서 같은 명령으로 따라 할 수 있음. 에이전트가 Windows 파일을 건드리지 않게 분리 |
| **깨끗한 기본판(base.tar)** 을 저장해 두고 복제해서 사용 | WSL에는 스냅숏이 없음. 대신 export · import로 '설치 전 상태'를 언제든 다시 만듦 |
| 수업이 끝나면 **USB로 내보내고 PC에서는 지움** | 공용 PC에 봇 토큰 · API 키 · 로그인이 남지 않게. 내일은 USB에서 다시 불러옴 |

**도착 시각: 수업 1시간 전 (17:30 이전)** · 준비물: USB 메모리(8GB 이상), 휴대폰(디스코드 앱 · 핫스팟), 맥북 + 충전기 · USB-C → HDMI 어댑터(백업)

---

## 0. 가능한지 먼저 확인 (5분)

하나라도 안 되면 바로 [백업 계획](#백업--맥북--multipass)으로 갑니다.

- [ ] **관리자 권한:** 시작 메뉴 → PowerShell 오른쪽 클릭 → '관리자로 실행' → `wsl --status`가 오류 없이 나온다
- [ ] **복원 프로그램:** 재부팅하면 초기화되는 프로그램이 있는지 센터 담당자에게 확인 (있으면 설치 후 재부팅에서 사라짐)
- [ ] **학교 망:** 브라우저에서 `discord.com/app`이 열린다. 막혀 있으면 휴대폰 핫스팟으로 연결
- [ ] **화면:** 프로젝터에 PC 화면이 나온다

## 1. 기본 Ubuntu 만들기 (20분)

관리자 PowerShell:

```powershell
wsl --install -d Ubuntu-24.04
```

- WSL이 처음이면 **재부팅**을 요구합니다. 재부팅 뒤 Ubuntu 창이 열리면 사용자 이름 · 비밀번호를 만듭니다.
- 이미 WSL이 있으면 재부팅 없이 Ubuntu만 추가됩니다.

Ubuntu 창 안에서:

```bash
sudo apt update && sudo apt install -y git python3 curl
curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
source ~/.bashrc
nvm install 22
node -v                       # v22.x 가 나오면 OK (n8n은 20.19~24.x)
git clone https://github.com/aifrenz/pcu-2026.git
```

`/etc/wsl.conf`를 열어(`sudo nano /etc/wsl.conf`) 아래 두 부분이 있는지 확인하고, 없으면 넣습니다. `내사용자이름`은 위에서 만든 이름입니다.

```
[boot]
systemd=true

[user]
default=내사용자이름
```

- `[user]`가 없으면 복제본이 root로 로그인됩니다.
- `[boot] systemd=true`는 OpenClaw의 백그라운드 실행 등록에 필요할 수 있습니다(리허설에서 확인).

- [ ] `node -v`가 22.x
- [ ] `/etc/wsl.conf`에 `[boot]`, `[user]` 확인

## 2. 기본판 저장 · 복제본 만들기 (10분)

PowerShell (관리자 아니어도 됨):

```powershell
wsl --terminate Ubuntu-24.04
mkdir C:\wsl
wsl --export Ubuntu-24.04 C:\wsl\base.tar
wsl --import openclaw    C:\wsl\openclaw    C:\wsl\base.tar
wsl --import hermes-live C:\wsl\hermes-live C:\wsl\base.tar
wsl -l -v                    # Ubuntu-24.04, openclaw, hermes-live 세 개가 보이면 OK
copy C:\wsl\base.tar E:\     # E: = 내 USB. 내일 DAY 3 복제본을 빨리 만들기 위해
```

복제본에 들어가기: `wsl -d openclaw`, `wsl -d hermes-live`. Windows Terminal을 쓰면 탭 이름으로도 열립니다.

- [ ] 복제본 세 개 확인
- [ ] `base.tar`를 USB에 복사

## 3. 장면별 준비 (30분)

| 장면 | 어디서 | 미리 할 일 |
| --- | --- | --- |
| OpenClaw (비교 상대) | `wsl -d openclaw` | 설치 · 연결 · 메시지 미리 보내 보기 |
| Hermes 라이브 설치 | `wsl -d hermes-live` | 끝까지 리허설 → 설치 전 상태로 되돌리기 |
| n8n 뉴스 브리핑 · 실험 3가지 | `wsl -d openclaw` | 미리 한 번 띄워 내려받기 · 워크플로 준비 |
| MCP | `wsl -d openclaw` 안의 Claude Code | 서버 연결 · 확인 질문 3개 |
| 에이전트 루프 | 아무 복제본 | `--no`로 한 번 실행 |

### OpenClaw

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
openclaw onboard --install-daemon   # 모델 · 디스코드 설정 + 백그라운드 실행 등록
openclaw gateway status             # 돌고 있는지 확인
openclaw doctor                     # 문제 점검
```

- [ ] Discord Developer Portal에서 OpenClaw용 봇 만들기 · 토큰 등록 ([메신저 연결](../day2/advanced/messengers.md#디스코드-추천)) · 내 서버에 초대
- [ ] 디스코드에서 봇에게 DM 한 통 → 답이 온다 (모르는 사용자로 나오면 `openclaw pairing approve discord <코드>`)
- [ ] [시연 메시지 6개](../day2/demo/1_hermes_openclaw.md) 중 앞의 1~2개를 미리 보내 둔다 (DAY 3 '기억' 확인용 대화가 남도록)

### Hermes (리허설 후 되돌리기)

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
hermes model            # 'ChatGPT or Codex Subscription' → 주소를 시크릿 창에서 열고 코드 입력 (API 키 없이)
hermes gateway setup    # Discord (OpenClaw와 다른 봇 토큰 · 내 사용자 ID)
hermes gateway          # 게이트웨이 켜기 (이 탭을 열어 두는 동안 동작)
hermes doctor
```

- [ ] 게이트웨이 명령: 앞에서 켜기 `hermes gateway`, 서비스로 `hermes gateway install` → `start` / `status` / `stop`
- [ ] 디스코드 DM에서 답이 오는 것까지 확인
- [ ] 걸린 시간 메모 (수업에서 이 시간만큼 기다림)

리허설이 끝나면 설치 전 상태로 되돌립니다. PowerShell:

```powershell
wsl --unregister hermes-live
wsl --import hermes-live C:\wsl\hermes-live C:\wsl\base.tar
```

- [ ] 되돌린 뒤 `wsl -d hermes-live` → `hermes` 명령이 **없다**고 나오면 OK

### n8n

```bash
GENERIC_TIMEZONE=Asia/Seoul npx n8n     # 처음에는 내려받느라 몇 분
```

- Windows 브라우저에서 `http://localhost:5678` → 계정 만들기(이 PC 안의 계정)
- 터미널을 닫으면 n8n도 꺼집니다. 시연 중에는 탭을 열어 둡니다.

- [ ] [뉴스 브리핑 워크플로](../day2/demo/2_n8n_briefing.md) 준비 · 한 번 실행
- [ ] 워크플로 **Settings → Timezone** = `Asia/Seoul`

### MCP (Claude Code 경로)

```bash
curl -fsSL https://claude.ai/install.sh | bash     # 설치 명령은 공식 문서에서 한 번 더 확인
echo $ANTHROPIC_API_KEY                            # 아무것도 안 나와야 구독으로 쓰임
mkdir -p ~/Desktop/ai-practice
claude mcp add practice-folder -- npx -y @modelcontextprotocol/server-filesystem ~/Desktop/ai-practice
claude                                             # 로그인 주소는 브라우저 '시크릿 창'에서 열기
```

- [ ] Claude Code 안에서 `/mcp` → `practice-folder` 연결 확인
- [ ] [확인 질문 3개](../day2/advanced/3_mcp.md) · 폴더 밖 파일 읽기가 **실패**하는지 확인

### 에이전트 루프

```bash
cd ~/pcu-2026/ai-agent-2026/day2/advanced/4_agent_loop
python3 agent_loop.py --no
```

- [ ] `[멈춤]` 없이 '최종 답'까지 나온다

## 4. 수업 직전 (5분)

- [ ] Windows **방해 금지** · 알림 끄기 (디스코드 · 메일 알림에 토큰이나 개인 메시지가 뜨지 않게)
- [ ] 터미널 글꼴 크게 (Windows Terminal: Ctrl + `+`)
- [ ] **`wsl -d openclaw` 탭을 하나 열어 두기** — WSL은 열린 터미널이 없으면 잠시 뒤 Linux를 꺼서 봇도 멈춥니다
- [ ] 브라우저 시크릿 창의 디스코드(discord.com/app)에 두 봇과의 DM 창을 나란히 준비

---

## 5. 수업이 끝나면 · 공용 PC 정리 (10분)

PowerShell:

```powershell
wsl --terminate openclaw
wsl --terminate hermes-live
wsl --export openclaw    E:\openclaw.tar      # 내일 DAY 3 오프닝용 (토큰이 들어 있으니 USB는 직접 보관)
wsl --export hermes-live E:\hermes-live.tar   # 수업 중 라이브 설치한 Hermes + 만든 스킬 · 기억
wsl --unregister openclaw
wsl --unregister hermes-live
wsl --unregister Ubuntu-24.04
del C:\wsl\base.tar
wsl -l -v                                 # 아무것도 없으면 OK
```

- [ ] `E:\openclaw.tar`, `E:\hermes-live.tar`, `E:\base.tar`가 USB에 있다
- [ ] 강의 PC에 복제본이 하나도 없다
- [ ] 브라우저에서 디스코드 · Claude 로그아웃, 시크릿 창 닫기
- [ ] (WSL을 처음 설치했다면) 센터 담당자에게 WSL 기능을 남겨 두어도 되는지 확인

## 6. DAY 3 시작 전 (30분)

```powershell
mkdir C:\wsl
wsl --import openclaw    C:\wsl\openclaw    E:\openclaw.tar
wsl --import hermes-live C:\wsl\hermes-live E:\hermes-live.tar
wsl --import cc-live     C:\wsl\cc-live     E:\base.tar      # Claude Code 라이브 설치용 깨끗한 복제본
```

DAY 2에서 메신저 연결을 하지 못했으므로, 오늘 오프닝에서 **디스코드 연결을 라이브로** 보여 줍니다 → [장면 0 · 메신저 연결](../day3/demo/0_messenger_connect.md)

- [ ] (USB 백업이 없으면) 1~3번대로 `openclaw` · `hermes-live`를 다시 설치해 두기. 모델 연결까지만, 메신저는 오프닝에서
- [ ] **수업 전, 화면 공유 없이:** Discord Developer Portal에서 봇 2개(`demo-hermes`, `demo-openclaw`) 만들기 → 토큰 메모 · Message Content Intent 켜기 · 수업용 서버에 초대 · 내 사용자 ID 복사
- [ ] 리허설: 한 봇만 미리 연결해 DM 답이 오는지 확인한 뒤, 오프닝에서는 나머지 하나를 라이브로 연결 (둘 다 라이브로 하면 시간이 빠듯)
- [ ] 오프닝 (10분): 연결 → 두 봇에 '브리핑 규칙' 메시지 → `브리핑` 한 번. 게이트웨이 탭 두 개는 **수업 끝까지** 열어 둠
- [ ] 마무리 (2분): 같은 DM 창에 `브리핑` 한 단어 → 기억 확인 · Hermes 스킬 폴더 확인
- [ ] Claude Code 라이브 설치는 `wsl -d cc-live`에서 ([장면 3](../day3/demo/claude_code_meeting_todo.md)). 로그인은 시크릿 창에서
- [ ] 수업 뒤 5번과 같은 방법으로 정리하고, **봇 토큰 두 개(Developer Portal → Reset Token)와 API 키를 폐기**

---

## 백업 · 맥북 + Multipass

0번에서 막히면 맥북을 HDMI에 연결하고 같은 Ubuntu 명령으로 진행합니다. 맥(ARM)과 강의 PC(x86)는 구조가 달라 WSL의 tar를 맥에서 쓸 수는 없으니, 맥은 따로 준비합니다.

```bash
brew install --cask multipass
multipass launch 24.04 --name openclaw    --cpus 2 --memory 4G --disk 20G
multipass launch 24.04 --name hermes-live --cpus 2 --memory 4G --disk 20G
multipass stop hermes-live && multipass snapshot hermes-live --name clean   # 설치 전 상태 저장
multipass shell openclaw          # 이후 3번의 Ubuntu 명령과 같음
```

- 되돌리기: `multipass stop hermes-live` → `multipass restore hermes-live.clean` (문법은 `multipass help snapshot`으로 확인)
- n8n · MCP는 맥에서 바로 실행해도 됩니다 (`GENERIC_TIMEZONE=Asia/Seoul npx n8n`)
- 맥에서는 '방해 금지', 수업 중 잠자기 방지 `caffeinate -d`

## 리허설에서 꼭 확인할 것

| 항목 | 왜 |
| --- | --- |
| Hermes 게이트웨이를 켜는 명령 | `hermes gateway`(앞에서) 또는 `hermes gateway install` → `start` (공식 메시징 문서에서 확인) |
| OpenClaw 백그라운드 실행이 WSL에서 유지되는지 | systemd 설정과 '열린 터미널' 조건의 영향을 받을 수 있음 |
| import한 복제본에서 디스코드 봇이 바로 답하는지 | 내일 오프닝이 이것에 달려 있음. 오늘 정리 전에 한 번 export → import 해 보면 가장 확실 |
