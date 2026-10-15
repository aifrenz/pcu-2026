# DAY 3 · AI 에이전트 미니 프로젝트

어제 만든 시나리오 카드를 **실제로 동작하는 에이전트**로 만듭니다.

- **목표:** 어제의 시나리오 카드를 '입력 → AI 판단 → 도구 → 결과'로 동작하는 나만의 에이전트로 만듭니다.
- **완주 기준:** 입력을 넣으면 AI가 판단·생성해 결과가 나오는 흐름이 **실제로 한 번** 동작하면 완주입니다. 화면만 있고 AI 판단이 없으면 목업입니다. 미완성이어도 어디까지 됐는지 제출합니다.
- **준비물:** 노트북, 어제의 시나리오 카드, 범용 AI 계정 (트랙 C는 Coding Agent 하나)

> **오프닝:** 어제 강사가 설치한 비서에게 "어제 무엇을 부탁받았지?"를 물어 비교 기록표의 '기억' 칸을 함께 확인합니다.

> **처음이면 `quickstart`만 하세요.** 아래 진행 순서 표는 직접 설계하고 싶은 분용입니다.
>
> **가장 쉬운 길 · 바로 실습:** [`quickstart/`](quickstart/README.md)에서 프로젝트 하나를 골라 **회색 상자를 차례로 복사해 붙여 넣기만** 하세요. 빈칸이 없고, 테스트 자료와 안전 테스트, 2분 데모 대본까지 들어 있습니다.

> **막막하면:** [`examples/project_examples.md`](examples/project_examples.md)에서 완성 예시 6개 중 하나를 골라 그대로 만드세요. 캔버스 · 지시문 · 웹앱 프롬프트 · 테스트 입력 두 개가 한 묶음으로 들어 있습니다.

## 진행 순서

| 순서 | 단계 | 할 일 | 파일 |
| --- | --- | --- | --- |
| 1 | 설계 캔버스 | 시나리오 카드를 5칸으로 압축 + 테스트 입력 두 개 정하기 | [`design_canvas.md`](design_canvas.md) |
| 2 | 트랙별 제작 | A0·A·B·C 중 하나 (중간에 'AI 판단이 한 번이라도 돌았나' 점검) | [`tracks/`](tracks/) |
| 3 | 안전 · 데모 준비 | 체크리스트 5문항 + 2분 데모 연습 | [`worksheets/safety_checklist.md`](worksheets/safety_checklist.md) |
| 4 | 제출 | 데모 링크·화면 | [`worksheets/demo_and_submit.md`](worksheets/demo_and_submit.md) |

## 완성 예시 고르기

| 어제 카드 | 오늘 만드는 것 | 추천 트랙 |
| --- | --- | --- |
| ① 주간 AI 뉴스 브리핑 | [① 내 분야 뉴스 카드](examples/project_examples.md#ex1) | A0 (웹 검색이 필요) |
| ② 회의록 → 할 일 메일 | [② 회의록 할 일표 생성기](examples/project_examples.md#ex2) | A0 · A · B · C 모두 |
| ③ 관심 목록 변화 추적 | [③ 조건 맞춤 추천기](examples/project_examples.md#ex3) | A0 · A · C |
| ④ 논문 알림 비서 | [④ 논문 초록 관련성 판정기](examples/project_examples.md#ex4) | A0 · A |
| ⑤ 지원사업 공고 비서 | [⑤ 지원사업 자격 판정기](examples/project_examples.md#ex5) | A0 · A · B |
| ⑦ 받은 메일 분류 비서 | [⑥ 메일 우선순위 분류기](examples/project_examples.md#ex6) | A0 · A |

테스트 입력은 [`data/test_inputs.md`](data/test_inputs.md)에 모아 두었습니다.

## 트랙 고르기

망설여지면 A0을 고릅니다. **모든 트랙의 완주 기준은 같습니다**: AI 판단이 한 번 실제로 동작하면 됩니다.

| 트랙 | 대상 | 무엇을 만드나 | 도구 | 안내 |
| --- | --- | --- | --- | --- |
| A0 기본 | 모두 | 맞춤 에이전트 (지시문 + 지식 파일 + 도구) | 범용 AI의 프로젝트·맞춤 에이전트 기능 | [`tracks/A0_custom_agent.md`](tracks/A0_custom_agent.md) |
| A 기본+ | 모두 | AI 판단이 들어간 작은 웹앱 | Artifacts 등 자연어 앱 제작, (선택) Stitch로 화면 설계 | [`tracks/A_web_app.md`](tracks/A_web_app.md) |
| B 중급 | 자동화에 관심 | 폼·웹훅 입력 → AI Agent 노드 → 전달 | n8n 또는 Make | [`tracks/B_n8n_workflow.md`](tracks/B_n8n_workflow.md) |
| C 심화 | 개발 경험자 | 웹앱 + API·MCP 연결 | Claude Code 등 Coding Agent | [`tracks/C_coding_agent.md`](tracks/C_coding_agent.md) |

## 강의 시연 따라 하기

강사가 화면에서 Claude Code를 설치해 '회의록 정리기'를 만든 장면을 그대로 적었습니다. 트랙 C를 고른 분은 이 순서대로 하면 됩니다: [`demo/claude_code_meeting_todo.md`](demo/claude_code_meeting_todo.md)

## 막힐 때

| 이럴 때 | 이렇게 |
| --- | --- |
| 어제 카드가 없다 / 마음에 안 든다 | [`examples/project_examples.md`](examples/project_examples.md)에서 하나 골라 그대로 만든다 |
| 화면은 됐는데 입력을 바꿔도 결과가 같다 | 목업 상태입니다. "정해진 글 대신 AI를 호출해서 판단하게 해 줘"를 다시 요청 |
| 시간 안에 끝낼 자신이 없다 | 트랙을 A0으로 내리고 판단 1회 동작부터 만든다 |
| 앱에서 오류가 난다 | 오류 메시지를 그대로 붙여 넣고 "원인을 설명하고 고쳐 줘" |
| n8n에서 AI 노드가 실패한다 | 모델 연결 자격 증명과 입력 필드 이름을 확인하고, 노드를 하나씩 실행한다 |
| Coding Agent가 파일을 너무 많이 바꾼다 | 멈추고 "가장 작은 버전부터, 파일 3개 이내로"라고 범위를 줄인다 |

## 이후 과제 (선택)

| 다음 단계 | 해 볼 일 |
| --- | --- |
| 쓰는 사람 | 매주 한 가지 일을 DAY 1 STEP 3 방식(목표 · 기준 · 제약)으로 맡겨 보기 |
| 연결하는 사람 | 시나리오 카드 하나를 예약 실행까지, 또는 n8n으로 Workflow + Agent 하나 완성 |
| 만드는 사람 | 오늘 만든 프로토타입을 배포하고, API·MCP로 도구 하나를 직접 연결 |

질문과 후기, 더 발전시킨 결과물은 과정 게시판(Padlet)에 올려 주세요.
