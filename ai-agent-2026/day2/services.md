# 서비스별로 지금 되는 것 · 2026년 10월 15일 기준

AI 서비스의 메뉴와 플랜별 기능은 자주 바뀝니다. 아래는 **수업 당일 공식 도움말과 기사로 확인한 내용**입니다. 내 화면과 다르면 화면이 맞습니다.

## 한눈에 보기

**기본 실습(프로젝트에 지시문 저장 → 실행)은 세 서비스 모두 무료로 됩니다.** 예약과 커넥터는 서비스 · 플랜마다 다릅니다. 그래서 오늘 완주 기준에서 예약은 '가능한 플랜만'입니다.

| | 프로젝트 (지시문 저장) | 예약 실행 | 커넥터 (메일 · 캘린더 · 드라이브) |
| --- | --- | --- | --- |
| **Claude** | 무료: 프로젝트 5개까지 · Pro 이상: 무제한 | **Pro 이상.** 서버에서 돌아서 컴퓨터를 꺼도 실행됨 | 무료부터 가능 |
| **ChatGPT** | 무료부터 가능 (2025년 9월부터) | **무료 포함 전 플랜.** 무료 · Go: 활성 3개, 하루 1번, 시간대 안에서 실행 · Plus: 5개, 매시간 · 정확한 시각 | 유료 플랜 중심 (무료는 확인 필요) |
| **Gemini** | Gem 무료부터 가능. **10월 13일부터 'Skills'로 바뀌는 중** | **Google AI Pro · Ultra 이상** | Google 앱(Gmail · 캘린더 · 드라이브) 연결 가능 |

<details><summary><b>Gemini의 Gem이 Skills로 바뀌는 중</b> — 오늘 화면에 'Skills'가 보여도 같은 용도입니다</summary>

- Google은 9월 30일에 Gem의 후속으로 **Skills**를 발표했습니다. Gemini 앱에는 10월 13일부터 들어오기 시작해 11월 중순까지 퍼집니다.
- **기존 Gem은 계속 만들고 쓸 수 있습니다.** 11월 17일에 Gem 메뉴가 설정 화면으로 옮겨집니다.
- 오늘 실습에서는 Gem이 보이면 Gem을, Skills만 보이면 Skills에 지시문을 넣으면 됩니다. 둘 다 못 찾으면 **지시문을 새 대화의 첫 메시지로** 보내세요.

</details>

<details><summary><b>무료 Gemini는 가장 가벼운 모델만</b> — 10월 9일부터 Flash-Lite 하나</summary>

- 10월 9일부터 Google AI 플랜이 없는 무료 계정은 **Flash-Lite 모델만** 씁니다.
- 그래서 같은 지시문이라도 다른 서비스보다 판단이 약하게 나올 수 있습니다. 결과가 기준과 다르면 지시문 문제인지, 모델 차이인지 함께 생각해 보세요. Form 4번(막힌 지점)의 좋은 소재입니다.

</details>

<details><summary><b>예약을 걸었다면 꼭 확인할 것</b> — AI가 말로만 '예약했습니다'라고 할 수 있음</summary>

- **ChatGPT:** 왼쪽 메뉴의 **예약(Scheduled)** 화면에 실제로 등록됐는지 봅니다. 무료는 정확한 시각이 아니라 정해진 시간대 안에서 돌고, 하루 1번까지입니다.
- **Claude (Pro 이상):** 대화에서 "매일 8시에 해 줘"처럼 말하면 Claude가 질문한 뒤 이름 · 주기 · 지시를 보여 주고, **'Schedule'** 을 눌러야 등록됩니다. 왼쪽 **Scheduled** 메뉴에서 확인합니다.
- **Gemini (Pro · Ultra):** 설정의 **예약된 작업(Scheduled actions)** 화면에서 확인합니다. 한 번에 10개까지입니다.

</details>

---

## 메신저 비서: OpenClaw와 Hermes

강의에서 강사가 설치해 보여 준 두 비서입니다. 범용 AI와 달리 **내 컴퓨터 · 서버에 깔아 두고 메신저로 말을 겁니다.**

| | OpenClaw | Hermes Agent |
| --- | --- | --- |
| 한 줄로 | 만들어진 스킬을 **골라 깔아서** 넓게 쓰는 비서 | 해 본 일을 **스스로 스킬로 적어 두고** 점점 나아지는 비서 |
| 만든 곳 | 오픈소스 커뮤니티 | Nous Research (오픈 모델 Hermes 시리즈) |
| 프로그램 비용 | 무료 (오픈소스) | 무료 (오픈소스) |
| 모델 연결 | 개인 API 키, **ChatGPT 구독 로그인** | 개인 API 키, **ChatGPT 구독 로그인**, GitHub Copilot, Nous Portal, 내 컴퓨터의 Ollama 등 |
| 강의에서 볼 것 | 설치된 스킬 목록, 로그의 도구 호출 | 같은 일을 몇 번 시킨 뒤 새로 생긴 스킬 파일 |
| 주의 | 남이 만든 스킬을 깔기 전에 내용 확인 | 스킬을 만들면서 토큰을 더 쓸 수 있음. 스스로 만든 스킬도 열어 보기 |

**공통점:** 게이트웨이가 늘 켜져서 메시지를 기다리고, 명령 실행 · 파일 접근 같은 강한 도구를 가집니다. 그래서 **어디에 깔고 무엇을 허용할지**가 범용 AI보다 훨씬 중요합니다. 강의에서는 강의 PC와 분리한 가상 환경(WSL)에 깔았습니다.

<details><summary><b>어떤 구독으로 모델을 연결할 수 있나</b> — ChatGPT 구독은 됨, Claude Pro는 안 됨</summary>

| 가진 구독 | Hermes · OpenClaw 연결 |
| --- | --- |
| **ChatGPT** | **됩니다.** Hermes는 `hermes model` → 'ChatGPT or Codex Subscription' → 화면의 주소를 열고 코드 입력. 어느 플랜까지 되는지, 구독 한도에서 어떻게 차감되는지는 공식 문서에 없으니 짧게 써 보고 확인 |
| **GitHub Copilot** | Hermes에서 로그인 연결 가능 |
| **Claude Pro** | 안 됩니다 |
| **Claude Max** | Hermes 문서상 '추가 사용량(extra usage)'을 따로 구매한 경우에만 로그인 연결, 사용량은 별도 과금 |
| **Gemini 구독** | 안 됩니다. Gemini는 API 키로만 (무료 키는 에이전트 대화 몇 번 만에 소진될 수 있음) |
| 없음 | 개인 API 키(선불 소액 충전 권장), 또는 내 컴퓨터에서 Ollama로 오픈 모델 (메모리가 넉넉한 컴퓨터 필요) |

로그인 정보는 그 컴퓨터 안(Hermes는 `~/.hermes/auth.json`)에 저장됩니다. 실습이 끝나면 지우거나 로그아웃하세요. 학교 · 회사 망에서는 로그인 중 보안 장비 때문에 SSL 오류가 날 수 있습니다. 그때는 휴대폰 핫스팟으로 바꿔 로그인합니다.

</details>

자세한 설치 · 운영은 [심화 1](advanced/1_openclaw_hermes.md), 강의 장면은 [강의 시연 1](demo/1_hermes_openclaw.md)에 있습니다.

---

## 출처 (2026년 10월 15일 확인)

- [Claude 도움말 · Schedule recurring tasks](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork) · [Claude 요금제](https://claude.com/pricing)
- [ChatGPT Tasks 플랜별 정리 (ai-toolbox, 2026-09 검토)](https://www.ai-toolbox.co/chatgpt-management-and-productivity/how-to-use-chatgpt-tasks-schedule-2026) · [ChatGPT 프로젝트 무료 개방 (Engadget)](https://engadget.com/ai/openai-rolls-out-chatgpt-projects-to-free-users-215027802.html)
- [Gemini Gem → Skills 일정 (Android Authority, 2026-09-30)](https://www.androidauthority.com/gemini-gems-phase-out-timeline-3717503/) · [무료 Gemini Flash-Lite 전환 (2026-10-05)](https://www.relevantaudience.com/ai/gemini-app-free-users-flash-lite-october-9/) · [Gemini 예약 실행 (Android Authority)](https://www.androidauthority.com/gemini-scheduled-actions-rollout-3565152)
- [Hermes Agent · 모델 공급자](https://hermes-agent.nousresearch.com/docs/integrations/providers)

**확인하지 못한 것:** ChatGPT 무료 플랜의 커넥터 범위, Gemini 예약 실행이 무료로 열렸는지(근거 기사는 2025년). 수업 중 화면으로 확인합니다.
