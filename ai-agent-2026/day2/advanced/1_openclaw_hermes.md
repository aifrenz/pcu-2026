# 심화 1 · OpenClaw 또는 Hermes 직접 설치

강의에서 강사가 시연한 개인 AI 비서를 **본인 노트북에** 직접 띄워 봅니다. 둘 중 하나만 하면 됩니다. **수업 중에는 강사 시연으로 충분하고, 설치는 집에서 아래 수칙을 보며 천천히** 하세요.

> **Docker Desktop은 필요 없습니다.** 두 도구 모두 데스크톱 앱이나 설치 명령 한 줄로 설치됩니다. Docker를 이미 쓰는 분만 Docker로 띄우세요. 에이전트가 내 컴퓨터와 분리되어 더 안전합니다.

## 설치 방법 고르기

| 방법 | OpenClaw | Hermes Agent |
| --- | --- | --- |
| **데스크톱 앱 (추천)** | Windows: [Windows Hub 설치 파일](https://github.com/openclaw/openclaw-windows-node/releases/latest) · macOS: [릴리스](https://github.com/openclaw/openclaw/releases)의 `.dmg` | [Hermes 설치 안내](https://hermes-agent.nousresearch.com/docs/getting-started/installation/)의 데스크톱 앱 (macOS는 Apple Silicon만) |
| 설치 명령 (Windows PowerShell) | `iwr -useb https://openclaw.ai/install.ps1 \| iex` | `iex (irm https://hermes-agent.nousresearch.com/install.ps1)` |
| 설치 명령 (macOS · Linux) | `curl -fsSL https://openclaw.ai/install.sh \| bash` | `curl -fsSL https://hermes-agent.nousresearch.com/install.sh \| bash` |
| Docker (이미 쓰는 분) | [OpenClaw 설치 문서](https://docs.openclaw.ai/install)의 Docker 안내 | [Hermes 설치 안내](https://hermes-agent.nousresearch.com/docs/getting-started/installation/) 참고 |

- 설치 명령은 인터넷에서 받은 스크립트를 바로 실행합니다. **주소가 위의 공식 주소인지 한 번 더 확인**하세요.
- 설치 방법은 버전마다 바뀝니다. 막히면 공식 문서([OpenClaw](https://docs.openclaw.ai/install) · [Hermes](https://hermes-agent.nousresearch.com/docs/getting-started/installation/))를 기준으로 합니다.

## 내 노트북에 깔 때 지킬 것

OpenClaw·Hermes는 명령을 실행하고 파일을 읽고 쓸 수 있는 에이전트입니다. Docker 없이 깔면 내 노트북 전체에 닿을 수 있으니 세 가지를 지킵니다.

1. **개인 메일·드라이브·회사 계정을 연결하지 않습니다.** 텔레그램 봇과 모델 키만 씁니다.
2. **명령 실행·파일 쓰기는 '승인 후 실행'** 으로 둡니다. 지시문에 "묻고 해"라고 적는 것은 권한 통제가 아닙니다. 설정으로 승인 모드를 켤 수 없다면 내 노트북에 깔지 말고 별도 컴퓨터·가상 머신·Docker에서 씁니다.
3. **끝나면 정리합니다.** 봇 토큰과 API 키를 폐기하고, 계속 쓰지 않으면 앱을 지웁니다.

## 연결하고 확인하기

| 항목 | OpenClaw | Hermes Agent |
| --- | --- | --- |
| 첫 설정 | 설치 뒤 나오는 안내(onboard)를 따라 모델·메신저 연결 | 설치 뒤 `hermes setup` |
| 모델 연결 | 개인 API 키, 또는 ChatGPT 구독 로그인 ([공식 문서](https://docs.openclaw.ai/providers/openai)) | 개인 API 키, 또는 `hermes setup --portal`로 Nous Portal |
| 메신저 | 텔레그램 @BotFather에서 봇 토큰 발급 후 등록 | `hermes gateway setup`으로 텔레그램 등록 후, 설정 마지막 안내대로 게이트웨이 켜기 |
| 확인 | 내 봇에 시나리오 카드의 일을 말로 시켜 보기 | 일을 끝낸 뒤 새 스킬 파일이 생겼는지 확인 |

- Claude 구독(Pro·Max)으로는 연결할 수 없습니다. Claude 모델은 API 키로 연결합니다.
- 텔레그램 봇 토큰도 비밀번호입니다. 화면 공유 중에 띄우지 않습니다.

## 봇에게 처음 보낼 말 (빈칸 예시)

시나리오 카드가 있으면 프로젝트 지시문을 그대로 보내면 됩니다. 막막하면 아래 중 하나를 보내세요.

```
너는 내 개인 비서야. 앞으로 내가 "브리핑"이라고 하면, 최근 7일 AI 에이전트 뉴스 중 [공공 행정] 실무자에게 중요한 3개를 골라 제목 · 한 줄 이유 · 링크로 알려 줘. 출처 없는 내용은 쓰지 마.
```

```
너는 내 회의 정리 비서야. 내가 회의록을 보내면 결정 사항, 결정하지 못한 사항, 할 일(담당·마감)을 표로 정리해 줘. 회의록에 없는 담당·마감은 '미정'으로 둬.
```

**기억 확인:** 한참 뒤에 `브리핑`이라고만 보내 보세요. 처음 설명한 형식대로 나오면 비서가 기억하고 있는 것입니다. Hermes라면 이때 새 스킬 파일이 생겼는지도 봅니다.

## 끝내기

실습이 끝나면 쓰지 않는 봇 토큰과 API 키를 폐기합니다. 앱으로 깔았다면 계속 쓰지 않을 때 앱을 지우고, Docker로 띄웠다면 컨테이너를 멈춥니다(`docker compose down` 등).
