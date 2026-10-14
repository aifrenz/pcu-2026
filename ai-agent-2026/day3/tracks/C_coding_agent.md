# 트랙 C · Coding Agent로 웹앱 (심화, 개발 경험자)

빈 폴더에서 Coding Agent(Claude Code, Codex, Antigravity 등)를 열고 **명세**를 줍니다. 테스트를 통과하고 로컬에서 돌아가면 완주입니다.

- Claude Code는 Claude Pro·Max 구독으로 쓸 수 있습니다. 다만 컴퓨터에 `ANTHROPIC_API_KEY` 환경 변수가 있으면 구독 대신 API로 과금됩니다.
- 만드는 앱이 LLM API를 호출하므로 **앱용 API 키**가 따로 필요합니다. 키는 `.env`에만 두고 `.gitignore`에 넣습니다.

## 명세 틀

```
[프로젝트 이름] 웹앱을 만들어 줘.
목표: [입력]을 받아 [Agent 판단]해서 [결과]를 보여 준다.
기술: 간단한 백엔드에서 LLM API를 호출한다. API 키는 환경 변수로만 읽는다.
도구: [필요한 API 또는 MCP 서버]
테스트: 입력 2개에 대해 결과 형식을 검사하는 테스트를 먼저 쓰고, 통과할 때까지 고쳐.
시작 전에 계획을 보여 주고, 파일 삭제나 배포는 나에게 먼저 물어봐.
```

## 완성 예 · 회의록 정리기

```
meeting-todo 웹앱을 만들어 줘.
목표: 회의록 텍스트를 받아 결정 사항·미결정 사항·할 일(담당·마감·상태)을 구분해서 표로 보여 준다. 회의록에 없는 담당·마감은 '미정'으로 둔다.
기술: Python FastAPI 백엔드 + HTML 한 장. 백엔드에서 Anthropic API를 호출하고, 응답은 JSON 스키마 {decisions: [], undecided: [], todos: [{task, owner, due, status}]}로 받는다. API 키는 환경 변수 ANTHROPIC_API_KEY로만 읽는다. .env.example과 .gitignore를 만든다.
도구: 외부 API는 LLM 하나만.
테스트: tests/ 폴더에 회의록 2개(fixtures)를 두고, LLM 호출을 가짜(mock)로 바꾼 상태에서 JSON 스키마·'미정' 처리·빈 입력 오류를 검사하는 테스트를 먼저 쓰고, 통과할 때까지 고쳐.
시작 전에 계획을 보여 주고, 파일 삭제나 배포는 나에게 먼저 물어봐.
```

테스트용 회의록: [`../../day1/data/meeting_notes_sample.md`](../../day1/data/meeting_notes_sample.md), [`../../day1/data/meeting_notes_more.md`](../../day1/data/meeting_notes_more.md)

## 완성 예 · 노트북 고르기 도우미

```
laptop-picker 웹앱을 만들어 줘.
목표: 예산·최대 무게·용도·더 중요한 것과 후보 목록을 받아, 조건 밖 후보를 이유와 함께 빼고 남은 것 중 하나를 추천한다.
기술: Node.js(Express) 백엔드 + HTML 한 장. 조건 필터(예산·무게)는 코드로 먼저 걸러 내고, 남은 후보 중 추천과 이유만 LLM이 판단한다. API 키는 환경 변수로만 읽는다.
도구: 외부 API는 LLM 하나만.
테스트: 가상 후보 6개와 조건 2가지로, 코드 필터 결과(제외 목록)는 정확히 일치하는지, LLM 응답은 형식만 검사하는 테스트를 먼저 쓰고, 통과할 때까지 고쳐.
시작 전에 계획을 보여 주고, 파일 삭제나 배포는 나에게 먼저 물어봐.
```

테스트용 후보와 조건: [`../data/test_inputs.md`](../data/test_inputs.md#laptops)

이 예시는 **'규칙으로 되는 것은 코드(Workflow), 판단이 필요한 것만 AI(Agent)'**로 나누는 연습입니다.

## 빈칸 예시

| 빈칸 | 예 |
| --- | --- |
| `[프로젝트 이름]` | meeting-todo · laptop-picker · paper-triage · grant-checker · mail-triage |
| `[필요한 API 또는 MCP 서버]` | LLM API 하나만 · 검색 API · 실습용 폴더만 허용한 파일 시스템 MCP |

## 막힐 때

| 이럴 때 | 이렇게 |
| --- | --- |
| 파일을 너무 많이 바꾼다 | 멈추고 "가장 작은 버전부터, 파일 3개 이내로"라고 범위를 줄인다 |
| 테스트가 실제 API를 부른다 | "테스트에서는 LLM 호출을 mock으로 바꿔 줘" |
| 키가 코드에 들어갔다 | 바로 키를 폐기하고, "키를 환경 변수로 옮기고 .gitignore를 확인해 줘" |
