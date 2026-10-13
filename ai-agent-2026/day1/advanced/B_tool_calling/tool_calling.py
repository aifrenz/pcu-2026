"""DAY 1 심화 B · Tool Calling 한 바퀴 (요청서 → 실행 → 최종 답)

실행:
    python tool_calling.py --mock                 # API 키 없이 흐름만 보기
    python tool_calling.py                        # 실제 모델 (ANTHROPIC_API_KEY 필요)
    python tool_calling.py "서울 내일 날씨 어때?"   # 질문 바꾸기
"""
import json
import os
import sys

try:                                    # .env 파일이 있으면 읽는다 (선택)
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

MODEL = "claude-sonnet-5-5"
args = [a for a in sys.argv[1:] if a != "--mock"]
QUESTION = args[0] if args else "내일 대전 날씨 어때? 우산 챙겨야 해?"

if "--mock" in sys.argv or not os.getenv("ANTHROPIC_API_KEY"):
    from mock_client import MockAnthropic
    client = MockAnthropic()
else:
    import anthropic
    client = anthropic.Anthropic()      # 환경 변수 ANTHROPIC_API_KEY 사용

# ① 도구 설명서: AI는 이것만 보고 언제, 어떻게 부를지 판단한다
TOOLS = [{
    "name": "get_weather",
    "description": "도시의 날씨 예보를 조회한다.",
    "input_schema": {
        "type": "object",
        "properties": {
            "city": {"type": "string", "description": "도시 이름, 예: 대전"},
            "date": {"type": "string", "description": "YYYY-MM-DD (선택)"},
        },
        "required": ["city"],
    },
}]


# ② 실제 도구: 실행은 AI가 아니라 이 프로그램이 한다
def get_weather(city, date=None):
    """실습용 가짜 데이터. 실제로는 여기서 날씨 API를 부른다."""
    fake = {"대전": "대전: 맑음, 최고 21°C, 강수확률 10%",
            "서울": "서울: 흐림, 최고 18°C, 강수확률 60%"}
    return fake.get(city, f"{city}: 데이터 없음")


messages = [{"role": "user", "content": QUESTION}]
print("[질문]", QUESTION)

for turn in range(5):                    # 무한 반복 방지 (중단 스위치)
    resp = client.messages.create(model=MODEL, max_tokens=512,
                                  tools=TOOLS, messages=messages)
    if resp.stop_reason != "tool_use":  # ③ 도구가 더 필요 없으면 최종 답
        print("[최종 답]", "".join(b.text for b in resp.content if b.type == "text"))
        break
    messages.append({"role": "assistant", "content": resp.content})
    results = []
    for b in resp.content:
        if b.type == "tool_use":
            print("[요청서]", b.name, json.dumps(b.input, ensure_ascii=False))
            out = get_weather(**b.input)
            print("[실행 결과]", out)
            results.append({"type": "tool_result", "tool_use_id": b.id, "content": out})
    messages.append({"role": "user", "content": results})   # ④ 결과를 AI에게 돌려준다
