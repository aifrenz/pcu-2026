# DAY 2 · AI 비서 시나리오 구성과 체험

> **처음 오신 분 → [처음 하는 분 안내 (3분)](quickstart/start_here.md)부터 보세요.** 맨 끝의 링크로 시나리오 2(회의록 정리 비서)로 넘어갑니다.  
> 복사 · 붙여 넣기에 익숙하면 바로 → [시나리오 2 · 회의록 정리 비서 만들기 (약 25분)](quickstart/2_meeting_todo.md)

## 오늘 할 일

1. 회의록을 정리해 주는 **AI 비서**를 만들어 한 번 써 본다 (복사해서 붙여 넣기만 하면 됩니다)
2. 구글 설문지(**Form**)에 4가지를 적어 낸다 → **https://forms.gle/49KjeRbGa6JtS7Lr9**

이 두 가지면 **완주**입니다. 준비물은 AI 계정 하나(무료 가능)뿐입니다.

<details><summary><b>오늘 실습 50분 예</b> — 준비 5분 · 시나리오 2 25분 · 제출 10분 · 여유 10분</summary>

| 시간 | 할 일 |
| --- | --- |
| 5분 | [처음 하는 분 안내](quickstart/start_here.md) 보고 화면 두 개 준비 |
| 25분 | [시나리오 2](quickstart/2_meeting_todo.md)의 1~3단계 |
| 10분 | 시나리오 2의 4단계 · Form 제출 |
| 10분 | 여유 · 시간이 남으면 [시나리오 0 · AI가 물어보며 내 지시문 만들기](quickstart/0_prompt_builder.md)의 1~2단계(질문에 답하기)까지, 3단계는 집에서 |

</details>

---

# 더 알아보기 (시간이 남는 분 · 집에서 · 직접 설계하고 싶은 분)

여기부터는 **오늘 완주에 필요하지 않습니다.**

| 이런 분 | 가 볼 곳 |
| --- | --- |
| 다른 주제로 해 보고 싶다 (뉴스 · 일정 · 메일 등 6개) | [`quickstart/`](quickstart/README.md) |
| 강의 내용을 다시 보고 싶다 (챗봇 vs 비서, 트리거, Workflow + Agent, MCP 등) | [`concepts.md`](concepts.md) |
| 내 서비스 · 플랜에서 프로젝트 · 예약 · 커넥터가 되는지, OpenClaw와 Hermes는 뭐가 다른지 | [`services.md`](services.md) (10월 15일 기준) |
| 완성 카드 예시를 보고 싶다 | [`examples/scenario_examples.md`](examples/scenario_examples.md) |
| 카드를 처음부터 직접 설계하고 싶다 | 아래 '진행 순서' |

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
