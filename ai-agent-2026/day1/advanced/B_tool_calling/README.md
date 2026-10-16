# 심화 B · Tool Calling — AI가 쓰는 '요청서' 직접 보기

AI는 도구를 직접 실행하지 않습니다. **어떤 도구를, 어떤 값으로 부를지 적은 요청서(tool_use)만 씁니다.** 실행은 프로그램이 하고, 결과(tool_result)를 돌려받은 AI가 최종 답을 씁니다.

```
질문 → AI: 요청서 작성 → 프로그램: 실행 → AI: 결과를 보고 최종 답
```

길은 세 가지입니다. 상황에 맞는 하나를 고르세요.

| 길 | 필요한 것 | 볼 수 있는 것 |
| --- | --- | --- |
| ① 모의 실행 | Python만 | 요청서 → 실행 → 결과의 흐름 (AI 판단은 규칙으로 흉내) |
| ② 실제 API | Python + API 키 (지출 상한 설정) | 실제 모델이 고르는 도구와 값 |
| ③ 구독만으로 | Claude Pro·Max 또는 ChatGPT 구독 | Coding Agent가 실제로 부르는 도구 호출 |

> **Windows라면 WSL에서:** [WSL에서 시작하는 실습 환경](../../../day3/wsl_setup.md) 1~2단계(WSL 켜기 · 기본 도구)를 먼저 합니다. 아래 `python3` 명령과 API 키 설정(`export …`)은 Ubuntu 창에서 그대로 칩니다.

## ① 모의 실행 (API 키 없이)

```bash
python tool_calling.py --mock
python tool_calling_two_tools.py --mock
```

결과 예:

```
[질문] 내일 대전 날씨 어때? 우산 챙겨야 해?
[요청서] get_weather {"city": "대전", "date": "2026-10-15"}
[실행 결과] 대전: 맑음, 최고 21°C, 강수확률 10%
[최종 답] 도구 결과를 바탕으로 답합니다. ...
```

## ② 실제 API

```bash
pip install -r requirements.txt
cp .env.example .env        # .env를 열어 키를 넣는다 (Windows: copy .env.example .env)
python tool_calling.py
python tool_calling_two_tools.py
```

- 키가 없거나 `--mock`을 붙이면 자동으로 모의 실행으로 바뀝니다.
- API 키는 코드에 직접 쓰지 않습니다. `.env`는 저장소에 올라가지 않습니다.

### 바꿔 보면서 관찰하기

| 해 볼 것 | 볼 것 |
| --- | --- |
| `python tool_calling.py "대전과 서울 중 어디가 더 맑아?"` | 요청서가 한 차례에 2개 나오나? (병렬 도구 호출) |
| `python tool_calling.py "오늘 기분 어때?"` | 도구를 부르지 않고 바로 답하나? (도구 사용 여부도 AI가 판단) |
| `python tool_calling.py "부산 내일 날씨 알려줘"` | '데이터 없음' 결과를 받고 최종 답을 어떻게 쓰나? (Observe) |
| `python tool_calling_two_tools.py` | 날씨와 계산기 중 무엇을 고르나? 둘 다 부르나? |
| 도구 설명(`description`)을 바꿔 보기 | 설명 한 줄이 AI의 도구 선택을 바꾸나? |

`calculate`가 `eval()` 대신 직접 만든 계산기를 쓰는 이유도 살펴보세요. AI가 보낸 값도 결국 '외부 입력'이라서, 그대로 실행하면 안 됩니다. 이 내용은 DAY 3 안전 파트로 이어집니다.

## ③ 구독만으로 도구 호출 관찰하기

코드를 쓰지 않아도 Coding Agent 화면에서 같은 구조를 볼 수 있습니다.

1. Claude Code(Claude Pro·Max 구독에 포함) 또는 Codex(ChatGPT 로그인)를 빈 폴더에서 엽니다.
2. 이렇게 요청합니다:
   ```
   이 폴더에 data.csv(가상의 월별 매출 12줄)를 만들고, 합계와 최고 매출 월을 계산해 줘. 각 단계에서 어떤 도구를 쓰는지 보여 줘.
   ```
3. 화면에 파일 쓰기 → 명령 실행 → 결과 읽기 같은 도구 호출이 하나씩 찍히는 것을 관찰합니다. 각 호출을 '요청서'라고 생각하고 기록표에 적어 보세요.

> **주의:** 컴퓨터에 `ANTHROPIC_API_KEY` 환경 변수가 설정돼 있으면 Claude Code는 구독 대신 그 API 키로 과금됩니다. ②를 해 본 뒤 ③을 하려면 환경 변수를 먼저 지우세요.
