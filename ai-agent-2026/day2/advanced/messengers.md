# 메신저 연결 · 디스코드(추천) · 왓츠앱 · 라인

OpenClaw와 Hermes에 말을 거는 **메신저 통로**를 무료로 만드는 방법입니다. 둘 다 같은 메신저를 지원하니 하나만 정하면 됩니다.

| 메신저 | 비용 | 준비 난이도 | 이럴 때 |
| --- | --- | --- | --- |
| **디스코드 (추천)** | 무료 | 쉬움 · 15분 | 처음 해 보는 분. 전화번호를 봇에 넘기지 않고, PC · 휴대폰 앱 모두에서 대화 |
| **왓츠앱** | 무료 | 보통 · QR 스캔 | 이미 왓츠앱을 쓰는 분. **비서용 번호를 따로** 쓰는 것을 권장 |
| **라인** | 무료 플랜 있음 | 어려움 · 공개 주소 필요 | 라인을 꼭 써야 하는 분. 내 컴퓨터를 인터넷에 여는 터널이 필요 |

> **단계별 자세한 안내:** [디스코드](../../day3/demo/0_messenger_connect.md#디스코드로-연결하기) · [왓츠앱](../../day3/demo/0_messenger_connect.md#왓츠앱으로-연결하기) · [라인](../../day3/demo/0_messenger_connect.md#라인으로-연결하기-openclaw--hermes-모두-가능) — 설치부터 Hermes/OpenClaw 연결, 허용 사용자, 확인, 정리까지
>
> **강의에서는 디스코드로 연결했습니다.** 두 비서용 봇을 하나씩 만들어 내 디스코드 서버에 초대하고, 각 봇에게 DM(1:1 메시지)으로 말을 겁니다.

---

## 디스코드 (추천)

### 1. 디스코드 봇 만들기 (5분, 웹 브라우저)

1. 디스코드 계정으로 [Discord Developer Portal](https://discord.com/developers/applications)에 로그인 → **New Application** → 이름 정하기 (예: `my-hermes-bot`)
2. 왼쪽 **Bot** 메뉴
   - **Reset Token** → 나온 **토큰**을 메모장에 저장합니다. **한 번만 보이고, 비밀번호와 같습니다.**
   - **Privileged Gateway Intents**에서 **Message Content Intent**를 켭니다(꺼져 있으면 봇이 메시지를 읽지 못함). **Server Members Intent**도 켭니다.
3. 왼쪽 **OAuth2 → URL Generator** (또는 **Installation**)
   - Scopes: `bot`, `applications.commands`
   - Bot Permissions: View Channels · Send Messages · Read Message History · Embed Links · Attach Files
   - 아래에 생긴 주소를 열고 **내 서버**를 골라 초대합니다. 서버가 없으면 디스코드 앱 왼쪽 **+** → '직접 만들기'로 나만 있는 서버를 먼저 만듭니다.
4. 디스코드 앱 **설정 → 고급 → 개발자 모드** 켜기 → 내 프로필을 오른쪽 클릭 → **사용자 ID 복사** (허용 사용자 등록에 씀)

두 비서를 모두 해 볼 거라면 1~3을 두 번 해서 봇을 2개 만듭니다 (예: `my-hermes-bot`, `my-openclaw-bot`).

### 2. 비서에 연결

**Hermes**

```bash
hermes gateway setup    # Discord를 고르고 봇 토큰 · 내 사용자 ID 입력
hermes gateway          # 게이트웨이 켜기 (이 터미널을 열어 두는 동안 동작)
```

- 설정은 `~/.hermes/.env`의 `DISCORD_BOT_TOKEN`, `DISCORD_ALLOWED_USERS`(내 사용자 ID)에 저장됩니다. **허용 사용자가 비어 있으면 아무에게도 답하지 않습니다.**
- 봇에게 **DM**을 보내면 언급 없이 바로 답합니다. 서버 채널에서는 `@봇이름`으로 불러야 답합니다.
- 계속 켜 두려면 `hermes gateway install` → `hermes gateway start`, 상태는 `hermes gateway status`.

**OpenClaw**

```bash
openclaw channels add            # 목록에서 Discord를 고르고 봇 토큰 입력 (처음이면 플러그인 설치를 물어봄)
openclaw channels status --probe # 연결 확인
```

- 처음 설정(`openclaw onboard`) 중에 채널로 Discord를 골라도 됩니다.
- 모르는 사람이 DM을 보내면 **짝 맞추기(pairing) 코드**가 나옵니다. 내 계정이라면 `openclaw pairing approve discord <코드>`로 승인합니다.

### 3. 확인

내 서버의 멤버 목록에서 봇을 눌러 **메시지 보내기** → `안녕, 너는 누구야?` → 답이 오면 성공입니다.

---

## 왓츠앱

왓츠앱 웹처럼 **연결된 기기(QR)** 로 붙습니다. 비즈니스 계정이나 유료 API는 필요 없습니다.

| | Hermes | OpenClaw |
| --- | --- | --- |
| 준비 | Node.js 18 이상 | 처음 선택 시 플러그인 설치를 물어봄 (`openclaw plugins install @openclaw/whatsapp`) |
| QR 연결 | `hermes whatsapp` → 모드 선택 → QR 표시 | `openclaw channels login --channel whatsapp` → QR 표시 |
| 휴대폰에서 | 왓츠앱 **설정 → 연결된 기기 → 기기 연결** → QR 스캔 | 같음 |
| 허용 사용자 | `~/.hermes/.env`의 `WHATSAPP_ALLOWED_USERS=8210…` (국가번호 포함, `+` 없이) | 설정의 `allowFrom`에 내 번호. 모르는 번호는 `openclaw pairing approve whatsapp <코드>` |
| 켜기 | `hermes gateway` | `openclaw gateway status`로 확인 |

**꼭 알아 둘 것**

- 두 도구 문서 모두 **비서 전용 번호를 따로** 쓰라고 권합니다. 왓츠앱은 공식 비즈니스 API 밖의 봇을 지원하지 않아 **계정이 제한될 작은 위험**이 있습니다. 내 번호로 시험만 해 볼 때는 '나와의 대화(self-chat)' 모드를 씁니다.
- 연결 정보(세션 파일)는 **내 왓츠앱 계정 전체 권한**과 같습니다. Hermes는 `~/.hermes/platforms/whatsapp/session`에 저장합니다. 실습이 끝나면 휴대폰의 **연결된 기기**에서 로그아웃합니다.
- QR은 금방 만료됩니다. 터미널에 뜬 QR을 바로 찍습니다.

---

## 라인 (어려움)

라인은 **LINE Developers 콘솔의 Messaging API 채널**을 만들고, 라인 서버가 내 비서에게 메시지를 보낼 **공개 HTTPS 주소(웹훅)** 가 있어야 합니다. 내 노트북 · WSL에서 돌린다면 터널(예: cloudflared, ngrok)로 주소를 열어야 해서, 처음 하는 분께는 권하지 않습니다.

1. [LINE Developers](https://developers.line.biz/) → Provider 만들기 → **Messaging API** 채널 추가
2. **Channel access token**, **Channel secret**을 복사해 둡니다
3. 비서에 연결
   - OpenClaw: `openclaw plugins install @openclaw/line` → 채널 설정
   - Hermes: `hermes gateway setup`에서 LINE 선택
4. Messaging API 설정에서 **Use webhook**을 켜고, 웹훅 주소에 공개 HTTPS 주소를 넣습니다 (OpenClaw 예: `https://내-주소/line/webhook`)

라인 공식 계정의 무료 플랜은 **먼저 보내는 메시지 수에 월 한도**가 있습니다. 실습처럼 내가 말을 걸고 답을 받는 정도라면 충분하지만, 예약 브리핑처럼 비서가 먼저 보내는 일은 한도를 확인하세요.

---

## 공통 안전 수칙

1. **허용 사용자는 나만.** 디스코드 사용자 ID · 왓츠앱 번호를 허용 목록에 넣고, 모두 허용(`*`, allow all)은 쓰지 않습니다. 명령 실행 도구를 가진 비서에게 남이 일을 시킬 수 있게 됩니다.
2. **봇 토큰 · 세션 파일은 비밀번호입니다.** 화면 공유 중에 띄우지 않고, 저장소 · 스크린샷 · 제출물에 넣지 않습니다.
3. **끝나면 정리:** 디스코드는 Developer Portal에서 **Reset Token**(기존 토큰 무효화) 또는 앱 삭제, 왓츠앱은 휴대폰의 연결된 기기에서 로그아웃, 라인은 채널 토큰 재발급.

## 막힐 때

| 이럴 때 | 이렇게 |
| --- | --- |
| 디스코드 봇이 오프라인 | 게이트웨이가 켜져 있는지, **Message Content Intent**가 켜져 있는지 확인 |
| 디스코드 봇이 서버 채널에서 답하지 않음 | `@봇이름`으로 부르거나 DM으로 보냄 |
| 아무에게도 답하지 않음 | 허용 사용자(`DISCORD_ALLOWED_USERS` 등)에 내 ID가 들어 있는지 확인 |
| 왓츠앱 QR이 만료됨 | 명령을 다시 실행해 새 QR을 바로 스캔 |
| 라인 웹훅 확인이 실패 | 주소가 `https`인지, 터널이 켜져 있는지, 비서 게이트웨이가 켜져 있는지 확인 |

출처: [Hermes 메시징 게이트웨이](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/) · [Hermes Discord](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/discord) · [Hermes WhatsApp](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/whatsapp) · [OpenClaw 채널](https://docs.openclaw.ai/channels) · [OpenClaw Discord](https://docs.openclaw.ai/channels/discord/setup) · [OpenClaw WhatsApp](https://docs.openclaw.ai/channels/whatsapp) · [OpenClaw LINE](https://docs.openclaw.ai/channels/line) (2026년 10월 16일 확인)
