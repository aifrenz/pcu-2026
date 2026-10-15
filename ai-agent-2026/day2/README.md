# DAY 2 · AI 비서 시나리오 구성과 체험

어제 맡긴 일을 **매번 시키지 않아도 돌아가는 비서**로 바꿉니다.

- **목표:** 어제 고른 과제를 '기억 · 예약 · 연결'을 갖춘 AI 비서 시나리오로 설계하고, 내 범용 AI에서 한 번 실제로 돌려 봅니다.
- **완주 기준:** 시나리오 카드 7칸 + 1회 실행 결과를 Google Form 4문항으로 제출 (비교표는 '내 범용 AI' 칸만 채워도 됨). 예약 실행은 플랜이 허용하는 분만 합니다.
- **준비물:** 범용 AI 계정, 어제 Form에 적은 '다음에 자동화하고 싶은 부분', 강의 중 채운 비교 기록표(OpenClaw·Hermes 칸)

> **처음이면 `quickstart`만 하세요.** 아래 진행 순서 표는 카드를 직접 설계하고 싶은 분용입니다.
>
> **내 일로 지시문을 만들고 싶다면:** [`quickstart/0_prompt_builder.md`](quickstart/0_prompt_builder.md) — AI가 질문 7개를 하나씩 물어보고 지시문을 완성해 줍니다.
>
> **가장 쉬운 길 · 바로 실습:** [`quickstart/`](quickstart/README.md)에서 시나리오 하나를 골라 **회색 상자를 차례로 복사해 붙여 넣기만** 하세요. 빈칸이 없고, 가상 자료가 모두 들어 있습니다.

> **강의 내용 다시 보기:** [`concepts.md`](concepts.md) — 챗봇 vs 비서, 트리거 3가지, Workflow + Agent, API · MCP, 구독 vs API, 권한 화면 읽는 법을 한 장에 정리했습니다.

> **막막하면:** [`examples/scenario_examples.md`](examples/scenario_examples.md)에서 완성 카드 7개 중 하나를 골라 그대로 쓰세요. 카드·지시문·1회 실행 문장이 한 묶음으로 들어 있습니다.

## 진행 순서

| 순서 | 단계 | 할 일 | 파일 |
| --- | --- | --- | --- |
| 1 | 시나리오 카드 | 어제 과제를 7칸 카드로 | [`scenario_card.md`](scenario_card.md) |
| 2 | 구성 · 1회 실행 | 프로젝트 → 커넥터 → 1회 실행 → (가능하면) 예약 | [`prompts/project_instruction.md`](prompts/project_instruction.md) |
| 3 | 비교 기록 | 내 범용 AI 칸 채우기 | [`worksheets/comparison_sheet.md`](worksheets/comparison_sheet.md) |
| 4 | 카드 고치기 | "내 일은 어느 유형의 비서에 맡길까" | [`worksheets/comparison_sheet.md`](worksheets/comparison_sheet.md#카드-고치기) |
| 5 | 제출 | Google Form 4문항 | [`worksheets/form_questions.md`](worksheets/form_questions.md) |

## 완성 예시 고르기

| 어제 과제 | 완성 카드 | 커넥터 없이 해 볼 때 |
| --- | --- | --- |
| A 동향 브리핑 | [① 주간 AI 뉴스 브리핑](examples/scenario_examples.md#ex1) | 웹 검색만 있으면 됨 |
| B 문서 → 보고서 | [② 회의록 → 할 일 메일](examples/scenario_examples.md#ex2) | DAY 1 가상 회의록 붙여 넣기 |
| C 조사 비교표 | [③ 관심 목록 변화 추적](examples/scenario_examples.md#ex3) | 웹 검색만 있으면 됨 |
| D 내 업무 (대학원생) | [④ 논문 알림 비서](examples/scenario_examples.md#ex4) | 웹 검색만 있으면 됨 |
| D 내 업무 (직장인) | [⑤ 지원사업 공고 비서](examples/scenario_examples.md#ex5) | [가상 공고 목록](data/sample_inputs.md#notices) |
| 새로 해 보고 싶다면 | [⑥ 다음 주 일정 점검 비서](examples/scenario_examples.md#ex6) | [가상 일정표](data/sample_inputs.md#schedule) |
| 새로 해 보고 싶다면 | [⑦ 받은 메일 분류 비서](examples/scenario_examples.md#ex7) | [가상 메일 6통](data/sample_inputs.md#mails) |

커넥터(캘린더·메일 연결)는 **안 해도 완주**입니다. 연결이 부담되면 [`data/sample_inputs.md`](data/sample_inputs.md)의 가상 자료를 붙여 넣으세요.

## 구성하기 · 1회 실행

메뉴 이름은 서비스·플랜마다 다릅니다. **'기억(프로젝트·지시문) · 연결(커넥터) · 예약'** 세 기능을 찾으면 됩니다.

1. **프로젝트 만들기** — 새 프로젝트(또는 맞춤 지시문)에 카드로 만든 지시문을 저장합니다.
2. **커넥터 연결** — 필요한 것만, 읽기 권한부터. 없거나 어렵다면 가상 자료를 붙여 넣는 것으로 대신합니다.
3. **1회 실행** — `지금 한 번 실행해 줘`를 보내고 결과를 카드의 'AI 판단' 칸과 비교합니다.
4. **예약 걸기 (가능한 플랜만)** — 카드의 트리거·주기대로 설정합니다. 안 되면 건너뛰어도 완주입니다.

## 강의 시연 따라 하기

강사가 화면에서 직접 설치해 보여 준 두 장면을 보낸 메시지 · 설정 · 확인할 것까지 그대로 적었습니다. 수업 중에는 보기만 하고, 따라 해 보고 싶다면 집에서 합니다.

| 장면 | 내용 | 파일 |
| --- | --- | --- |
| 1 | Hermes Agent 라이브 설치, OpenClaw와 같은 메시지 6개 비교 (기억 · 안전 · 권한 테스트 포함) | [`demo/1_hermes_openclaw.md`](demo/1_hermes_openclaw.md) |
| 2 | `npx n8n`으로 띄우고 뉴스 브리핑 돌리기, 기준 · 입력 · AI 유무를 바꾸는 실험 3가지 | [`demo/2_n8n_briefing.md`](demo/2_n8n_briefing.md) |

## 심화 (선택) · 강의에서 본 장면을 직접

전체 지도와 순서는 [`advanced/README.md`](advanced/README.md)에 있습니다.

| 심화 | 내용 | 파일 |
| --- | --- | --- |
| 1 | 메신저 비서 구조 · OpenClaw와 Hermes 차이 · 운영 명령 · 응용 레시피 | [`advanced/1_openclaw_hermes.md`](advanced/1_openclaw_hermes.md) |
| 2 · 2+ | n8n 워크플로 4개: 뉴스 브리핑 · 폼 회의록 정리기 · 메일 분류 + 사람 승인 · 도구를 가진 채팅 비서 | [`advanced/2_n8n_news_briefing.md`](advanced/2_n8n_news_briefing.md), [`advanced/2b_n8n_more_workflows.md`](advanced/2b_n8n_more_workflows.md) |
| 3 | MCP 서버 꽂기 · 내가 만든 MCP 서버 · n8n과 MCP | [`advanced/3_mcp.md`](advanced/3_mcp.md) |
| 4 | 미니 에이전트 루프 — API 키 없이 실행해 루프 · 승인 · 멈춤 장치 보기 | [`advanced/4_agent_loop/`](advanced/4_agent_loop/) |

## 막힐 때

| 이럴 때 | 이렇게 |
| --- | --- |
| 어제 Form 5번을 비워 뒀다 | [`examples/scenario_examples.md`](examples/scenario_examples.md)에서 하나 고르거나, [`scenario_card.md`](scenario_card.md#어제-form-5번-답을-카드로-바꾸기)의 문장 틀을 채운다 |
| 프로젝트·커넥터 메뉴가 없다 (무료 플랜 등) | 지시문을 대화 첫 메시지로 보내고, 자료는 붙여 넣는다. 그래도 완주 |
| 예약 기능이 없다 | 건너뛰고, 카드에 '예약은 어디서 할지'만 적는다 (예: n8n) |
| 커넥터 권한 화면이 부담된다 | 연결하지 않아도 됩니다. 테스트용 계정이 아니면 읽기만 허용한다 |
| 결과가 카드 기준과 다르다 | [결과가 이상할 때 고치는 순서](prompts/project_instruction.md#결과가-이상할-때-고치는-순서)대로 지시문부터 고친다 |
| 메일 발송까지 해 보고 싶다 | 오늘은 초안까지만. 전송은 내가 확인하고 직접 보낸다 |
