# DAY 1 · 사람이 지휘할 때 vs AI에게 맡길 때

같은 과제를 두 번 합니다. 바뀌는 것은 **'누가 다음 단계를 정하는가'** 하나뿐입니다.

- **완주 기준:** STEP 2와 STEP 3을 모두 해 보고, 관찰 기록표 첫 줄('다음 단계를 정한 것은 누구?')을 채우면 완주입니다.
- **준비물:** 범용 AI 계정 1개(Claude 권장, ChatGPT·Gemini 가능, 무료 계정 가능), 고른 관통 과제

## 진행 순서

| 순서 | 단계 | 할 일 | 파일 |
| --- | --- | --- | --- |
| 0 (강의 중) | STEP 1 맛보기 | 질문 한 줄로 던지고 답 저장 | [`prompts/step1.md`](prompts/step1.md) |
| 1 | STEP 1 복기 | 질문 한 줄로는 어디까지 나왔나 | — |
| 2 | STEP 2 사람이 지휘 | 조사 → 분석 → 정리 → 작성을 한 단계씩 4번 지시 | 과제별 프롬프트 파일 |
| 3 | STEP 3 AI에게 위임 | **새 대화**에서 목표·기준·제약만 주고 맡기기 | 과제별 프롬프트 파일 |
| 4 | 비교 기록 | 관찰 기록표 채우기 | [`worksheets/observation_sheet.md`](worksheets/observation_sheet.md) |
| 5 | 제출 | Google Form 5문항 | [`worksheets/form_questions.md`](worksheets/form_questions.md) |

## 관통 과제 고르기

고민되면 A를 고르세요. 프롬프트의 `[ ]`만 내 상황으로 바꾸면 됩니다. **무엇을 넣을지 막막하면 [`data/fill_in_examples.md`](data/fill_in_examples.md)에서 하나 골라 그대로 넣으세요.**

| 과제 | 내용 | 프롬프트 | 예제 자료 |
| --- | --- | --- | --- |
| A 동향 브리핑 | 내 분야 AI·업계 뉴스를 찾아 정리 | [`prompts/A_trend_briefing.md`](prompts/A_trend_briefing.md) | [`data/fill_in_examples.md`](data/fill_in_examples.md) (처지별 주제) |
| B 문서 → 보고서 | 회의록을 할 일표와 공유 메일로 | [`prompts/B_doc_to_report.md`](prompts/B_doc_to_report.md) | [`data/meeting_notes_sample.md`](data/meeting_notes_sample.md), [`data/meeting_notes_more.md`](data/meeting_notes_more.md) (연구실·회사·메일) |
| C 조사 비교표 | 제품·공고·논문을 기준별로 비교 | [`prompts/C_comparison.md`](prompts/C_comparison.md) | [`data/comparison_personas.md`](data/comparison_personas.md) |
| D 내 업무 | 반복되는 내 일 (예: 논문 동향 정리) | [`prompts/D_my_work.md`](prompts/D_my_work.md) | [`data/fill_in_examples.md`](data/fill_in_examples.md) (연구 주제 13개) |

## 더 잘하고 싶다면

- [`prompts/delegation_card.md`](prompts/delegation_card.md) — 좋은 위임 프롬프트 공식, 약한 지시 → 강한 지시, 한 장 프롬프트 카드
- [`homework.md`](homework.md) — 시간이 부족했다면 집에서 짧은 복습 코스와 확장 과제

## 심화 (개발 경험자, 선택)

| 과제 | 내용 | 폴더 |
| --- | --- | --- |
| A · 서비스 비교 | 같은 STEP 3 지시를 두 번째 AI에 맡겨 비교 | [`advanced/A_compare_services.md`](advanced/A_compare_services.md) |
| B · Tool Calling | AI가 쓰는 '요청서'를 직접 보기 (API 키 없이 모의 실행 가능) | [`advanced/B_tool_calling/`](advanced/B_tool_calling/) |

## 막힐 때

| 이럴 때 | 이렇게 |
| --- | --- |
| STEP 3에서 AI가 계획 없이 바로 답한다 | 마지막 줄 "계획을 먼저 보여 주고"가 들어갔는지 확인하고 다시 보낸다 |
| 검색을 안 하고 예전 내용으로 답한다 | 검색·리서치 기능을 켜거나 "최근 7일 자료를 검색해서"를 넣는다 |
| 리서치가 너무 오래 걸린다 | 제약에 "출처 5개 이내, 10분 안에"를 더하고, 기다리는 동안 기록표를 채운다 |
| 무료 한도에 걸렸다 | 다른 AI 서비스로 옮기거나 짝의 화면을 함께 보며 기록한다 |
| 결과가 마음에 안 든다 | 정상입니다. 어느 기준이 빠졌는지 기록하는 것이 오늘의 목표입니다 |
