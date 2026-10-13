"""DAY 1 심화 B · 도구 2개 중 고르기 + 한 번에 여러 도구 부르기

AI가 질문을 보고 날씨 도구와 계산기 중 무엇을, 몇 번 부를지 스스로 정합니다.

실행:
    python tool_calling_two_tools.py --mock
    python tool_calling_two_tools.py "12900 * 3 은 얼마야?"
"""
import ast
import json
import operator
import os
import sys

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

MODEL = "claude-sonnet-5-5"
args = [a for a in sys.argv[1:] if a != "--mock"]
QUESTION = args[0] if args else "대전과 서울 내일 날씨를 비교해 줘. 그리고 12900 * 3 은 얼마야?"

if "--mock" in sys.argv or not os.getenv("ANTHROPIC_API_KEY"):
    from mock_client import MockAnthropic
    client = MockAnthropic()
else:
    import anthropic
    client = anthropic.Anthropic()

TOOLS = [
    {
        "name": "get_weather",
        "description": "도시의 날씨 예보를 조회한다. 여러 도시를 비교할 때는 도시마다 한 번씩 부른다.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "도시 이름, 예: 대전"},
                "date": {"type": "string", "description": "YYYY-MM-DD (선택)"},
            },
            "required": ["city"],
        },
    },
    {
        "name": "calculate",
        "description": "사칙연산 식을 정확히 계산한다. 금액·수량 계산은 반드시 이 도구를 쓴다.",
        "input_schema": {
            "type": "object",
            "properties": {"expression": {"type": "string", "description": "예: 12900 * 3"}},
            "required": ["expression"],
        },
    },
]


def get_weather(city, date=None):
    fake = {"대전": "대전: 맑음, 최고 21°C, 강수확률 10%",
            "서울": "서울: 흐림, 최고 18°C, 강수확률 60%"}
    return fake.get(city, f"{city}: 데이터 없음")


_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
        ast.Div: operator.truediv, ast.USub: operator.neg}


def calculate(expression):
    """eval()을 쓰지 않는 안전한 계산기 — AI가 보낸 값도 '입력'일 뿐이다."""
    def ev(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
            return _OPS[type(node.op)](ev(node.left), ev(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
            return _OPS[type(node.op)](ev(node.operand))
        raise ValueError("사칙연산만 계산할 수 있습니다")
    try:
        value = ev(ast.parse(expression.replace(",", ""), mode="eval").body)
        return f"{expression} = {value:,}"
    except (ValueError, SyntaxError, ZeroDivisionError) as e:
        return f"계산 실패: {e}"


HANDLERS = {"get_weather": get_weather, "calculate": calculate}

messages = [{"role": "user", "content": QUESTION}]
print("[질문]", QUESTION)

for turn in range(5):
    resp = client.messages.create(model=MODEL, max_tokens=800, tools=TOOLS, messages=messages)
    if resp.stop_reason != "tool_use":
        print("[최종 답]", "".join(b.text for b in resp.content if b.type == "text"))
        break
    messages.append({"role": "assistant", "content": resp.content})
    calls = [b for b in resp.content if b.type == "tool_use"]
    print(f"[이번 차례 요청서 {len(calls)}개]")
    results = []
    for b in calls:
        print("  [요청서]", b.name, json.dumps(b.input, ensure_ascii=False))
        out = HANDLERS[b.name](**b.input)
        print("  [실행 결과]", out)
        results.append({"type": "tool_result", "tool_use_id": b.id, "content": out})
    messages.append({"role": "user", "content": results})
