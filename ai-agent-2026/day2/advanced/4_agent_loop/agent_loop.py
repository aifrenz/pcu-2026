"""미니 에이전트 루프 — '계획 → 도구 실행 → 관찰 → 다시 계획'을 눈으로 보기.

    python agent_loop.py                 # 모의 두뇌 (API 키 필요 없음), 보내기 전에 승인을 물음
    python agent_loop.py --no            # 승인 질문에 자동으로 '아니오' (수업 시연용)
    python agent_loop.py --yes           # 승인 질문에 자동으로 '예'
    python agent_loop.py --real          # 실제 Claude API (환경 변수 ANTHROPIC_API_KEY 필요)

일정표는 가상 자료입니다. 메시지는 실제로 보내지지 않고 화면에 '보냈다고 가정'만 표시합니다.
"""
import json
import os
import sys
import urllib.request

GOAL = "다음 주 일정을 점검해서 문제가 있으면 관련된 사람에게 보낼 메시지 초안을 만들고, 내가 승인하면 보내 줘."
MAX_STEPS = 8  # 멈추는 장치: 루프가 끝없이 돌지 않게

# ---------------------------------------------------------------- 도구 (실행은 프로그램이 한다)
SCHEDULE = [
    {"day": "화", "start": "14:00", "end": "15:30", "title": "협력사 미팅", "place": "둔산동 협력사 사무실", "with": "협력사 김 팀장"},
    {"day": "화", "start": "15:00", "end": "15:30", "title": "고객 화상 통화", "place": "온라인", "with": "고객사 박 과장"},
    {"day": "수", "start": "16:30", "end": "18:40", "title": "외부 세미나", "place": "유성구 컨벤션홀", "with": ""},
    {"day": "수", "start": "19:00", "end": "21:00", "title": "스터디 모임", "place": "서구 카페", "with": "스터디원"},
    {"day": "목", "start": "10:00", "end": "11:00", "title": "분기 실적 발표", "place": "본사 대회의실", "with": ""},
]


def _min(t):
    h, m = t.split(":")
    return int(h) * 60 + int(m)


def read_schedule(week="다음 주"):
    return SCHEDULE


def find_conflicts(events):
    """규칙으로 되는 일은 코드로: 겹침과 30분 미만 간격을 정확히 계산한다."""
    out = []
    for i, a in enumerate(events):
        for b in events[i + 1:]:
            if a["day"] != b["day"]:
                continue
            gap = _min(b["start"]) - _min(a["end"])
            if gap < 0:
                out.append({"type": "겹침", "a": a["title"], "b": b["title"], "day": a["day"], "minutes": -gap})
            elif gap < 30 and a["place"] != b["place"] and "온라인" not in (a["place"], b["place"]):
                out.append({"type": "이동 빠듯", "a": a["title"], "b": b["title"], "day": a["day"], "minutes": gap})
    return out


def draft_message(to, text):
    return {"to": to, "text": text, "status": "초안"}


def send_message(to, text):
    return {"to": to, "status": "보냈다고 가정 (실습이라 실제로 보내지 않음)"}


TOOLS = {
    "read_schedule": (read_schedule, "다음 주 일정을 읽는다", {"week": "string"}),
    "find_conflicts": (find_conflicts, "일정 목록에서 겹침과 30분 미만 이동을 찾는다", {"events": "array"}),
    "draft_message": (draft_message, "보낼 메시지 초안을 만든다 (보내지 않음)", {"to": "string", "text": "string"}),
    "send_message": (send_message, "메시지를 보낸다 — 사람 승인이 필요하다", {"to": "string", "text": "string"}),
}
NEEDS_APPROVAL = {"send_message"}


# ---------------------------------------------------------------- 두뇌 1: 모의 (규칙으로 AI의 판단을 흉내)
class MockBrain:
    def next(self, history):
        done = [h["tool"] for h in history if h["kind"] == "call"]
        results = {h["tool"]: h["result"] for h in history if h["kind"] == "result"}
        if "read_schedule" not in done:
            return {"think": "먼저 일정을 읽어야 무엇이 문제인지 알 수 있다.", "tool": "read_schedule", "input": {"week": "다음 주"}}
        if "find_conflicts" not in done:
            return {"think": "겹침과 이동 시간은 계산 문제라 코드 도구에 맡긴다.", "tool": "find_conflicts",
                    "input": {"events": results["read_schedule"]}}
        conflicts = results["find_conflicts"]
        overlap = next((c for c in conflicts if c["type"] == "겹침"), None)
        if overlap and "draft_message" not in done:
            ev = next(e for e in SCHEDULE if e["title"] == overlap["b"])
            text = (f"{ev['with']}님, 안녕하세요. {overlap['day']}요일 {ev['start']} {ev['title']} 일정이 앞 일정과 "
                    f"{overlap['minutes']}분 겹칩니다. 15:40으로 미뤄도 괜찮으실까요?")
            return {"think": "겹친 상대 중 시간을 옮기기 쉬운 쪽(온라인 통화)에 양해를 구하는 초안을 쓴다.",
                    "tool": "draft_message", "input": {"to": ev["with"], "text": text}}
        if "draft_message" in done and "send_message" not in done and not any(h["kind"] == "denied" for h in history):
            d = results["draft_message"]
            return {"think": "초안이 준비됐다. 보내는 일은 되돌릴 수 없으니 승인을 받는다.", "tool": "send_message",
                    "input": {"to": d["to"], "text": d["text"]}}
        lines = [f"- {c['day']}요일 {c['a']} ↔ {c['b']}: {c['type']} ({c['minutes']}분)" for c in conflicts]
        if not overlap:
            tail = "겹치는 일정이 없어 보낼 메시지가 없습니다."
        elif "send_message" in results:
            tail = "겹침 건 메시지는 보냈습니다(가정)."
        else:
            tail = "겹침 건 메시지는 보내지 않고 초안으로 남겼습니다."
        return {"final": "다음 주 점검 결과입니다.\n" + "\n".join(lines) + "\n" + tail}


# ---------------------------------------------------------------- 두뇌 2: 실제 Claude API (tool use)
class ClaudeBrain:
    def __init__(self, model=None):
        self.key = os.environ.get("ANTHROPIC_API_KEY")
        if not self.key:
            sys.exit("ANTHROPIC_API_KEY 환경 변수가 없습니다. 모의 실행은 --real 없이 하세요.")
        self.model = model or os.environ.get("CLAUDE_MODEL", "claude-sonnet-5-5")
        self.messages = [{"role": "user", "content": GOAL}]
        self.tools = [{"name": n, "description": d, "input_schema": {"type": "object", "properties":
                      {k: {"type": v} for k, v in p.items()}}} for n, (_, d, p) in TOOLS.items()]
        self.pending = None

    def _call(self):
        body = json.dumps({"model": self.model, "max_tokens": 1024, "tools": self.tools,
                           "system": "너는 일정 비서다. 도구로 확인한 사실만 쓰고, 보내기 전에는 반드시 send_message로 승인을 받는다.",
                           "messages": self.messages}).encode()
        req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=body, headers={
            "x-api-key": self.key, "anthropic-version": "2023-06-01", "content-type": "application/json"})
        with urllib.request.urlopen(req) as r:
            return json.load(r)

    def next(self, history):
        if self.pending:  # 직전 도구 결과를 tool_result로 돌려준다
            last = history[-1]
            content = json.dumps(last.get("result", {"거절": "사용자가 승인하지 않았습니다"}), ensure_ascii=False)
            self.messages.append({"role": "user", "content": [
                {"type": "tool_result", "tool_use_id": self.pending, "content": content}]})
            self.pending = None
        resp = self._call()
        self.messages.append({"role": "assistant", "content": resp["content"]})
        text = " ".join(b["text"] for b in resp["content"] if b["type"] == "text")
        use = next((b for b in resp["content"] if b["type"] == "tool_use"), None)
        if use:
            self.pending = use["id"]
            return {"think": text or "(생각 없이 바로 도구 호출)", "tool": use["name"], "input": use["input"]}
        return {"final": text}


# ---------------------------------------------------------------- 루프 (Workflow): 이 부분은 매번 똑같다
def approve(tool, inp, mode):
    print(f"   ⏸  승인 필요: {tool} → {inp.get('to')}")
    print(f"      내용: {inp.get('text')}")
    if mode in ("yes", "no"):
        print(f"      (자동 응답: {'예' if mode == 'yes' else '아니오'})")
        return mode == "yes"
    return input("      보낼까요? [y/N] ").strip().lower() == "y"


def run(brain, mode):
    print(f"목표: {GOAL}\n")
    history = []
    for step in range(1, MAX_STEPS + 1):
        d = brain.next(history)
        if "final" in d:
            print(f"[{step}] 최종 답\n{d['final']}")
            return
        print(f"[{step}] 생각: {d['think']}")
        print(f"    도구 요청서: {d['tool']}({json.dumps(d['input'], ensure_ascii=False)[:120]})")
        history.append({"kind": "call", "tool": d["tool"]})
        if d["tool"] in NEEDS_APPROVAL and not approve(d["tool"], d["input"], mode):
            print("    결과: 사람이 거절함 → 보내지 않음\n")
            history.append({"kind": "denied", "tool": d["tool"]})
            continue
        fn = TOOLS[d["tool"]][0]
        result = fn(**d["input"])
        history.append({"kind": "result", "tool": d["tool"], "result": result})
        shown = json.dumps(result, ensure_ascii=False)
        print(f"    결과(관찰): {shown[:160]}{'…' if len(shown) > 160 else ''}\n")
    print(f"[멈춤] {MAX_STEPS}단계를 넘어 루프를 멈췄습니다.")


if __name__ == "__main__":
    args = sys.argv[1:]
    mode = "yes" if "--yes" in args else "no" if "--no" in args else "ask"
    run(ClaudeBrain() if "--real" in args else MockBrain(), mode)
