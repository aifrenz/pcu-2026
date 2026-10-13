"""API 키 없이 Tool Calling 흐름을 보여 주는 모의 클라이언트.

실제 AI가 아니라 간단한 규칙으로 '요청서(tool_use)'를 흉내 냅니다.
응답 모양은 Anthropic SDK와 같아서, 실습 코드는 그대로 둔 채 클라이언트만 바꿔 끼웁니다.
"""
import datetime as dt
import itertools
import re
from types import SimpleNamespace as Obj

CITIES = ["대전", "서울", "부산", "대구", "광주", "인천"]
_ids = itertools.count(1)


def _text(s):
    return Obj(type="text", text=s)


def _tool_use(name, inp):
    return Obj(type="tool_use", id=f"toolu_mock_{next(_ids)}", name=name, input=inp)


def _last_user_text(messages):
    for m in reversed(messages):
        if m["role"] == "user" and isinstance(m["content"], str):
            return m["content"]
    return ""


class _Messages:
    def create(self, model, max_tokens, messages, tools=(), **_):
        last = messages[-1]
        tool_names = {t["name"] for t in tools}

        # 1) 방금 도구 결과를 받았다면 → 결과를 보고 최종 답을 쓴다 (Observe)
        if last["role"] == "user" and isinstance(last["content"], list):
            lines = [f"- {r['content']}" for r in last["content"] if r.get("type") == "tool_result"]
            answer = "도구 결과를 바탕으로 답합니다.\n" + "\n".join(lines)
            if any("강수확률 6" in l or "강수확률 7" in l or "강수확률 8" in l for l in lines):
                answer += "\n강수확률이 높은 곳이 있으니 우산을 챙기세요."
            return Obj(stop_reason="end_turn", content=[_text(answer)])

        # 2) 질문을 보고 어떤 도구를 부를지 정한다 (Plan → Tool)
        q = _last_user_text(messages)
        calls = []
        if "get_weather" in tool_names:
            date = None
            if "내일" in q:
                date = (dt.date.today() + dt.timedelta(days=1)).isoformat()
            for city in CITIES:
                if city in q:
                    inp = {"city": city}
                    if date:
                        inp["date"] = date
                    calls.append(_tool_use("get_weather", inp))
        if "calculate" in tool_names:
            m = re.search(r"\d[\d\s.+\-*/()]*[+\-*/][\d\s.+\-*/()]*\d", q)
            if m:
                calls.append(_tool_use("calculate", {"expression": m.group(0).strip()}))

        if not calls:  # 도구가 필요 없다고 판단
            return Obj(stop_reason="end_turn",
                       content=[_text("이 질문은 도구 없이 답할 수 있어요. (모의 실행이라 내용은 생략)")])
        return Obj(stop_reason="tool_use", content=[_text("필요한 정보를 도구로 확인할게요.")] + calls)


class MockAnthropic:
    def __init__(self):
        self.messages = _Messages()
        print("[모의 실행] 실제 AI 대신 규칙으로 흉내 냅니다. 흐름만 확인하세요.\n")
