"""내가 만드는 MCP 서버 — 가상 일정표를 AI에게 '도구'로 꽂아 준다.

    pip install "mcp[cli]"        # 공식 Python SDK
    python schedule_server.py     # 보통은 직접 실행하지 않고, AI 앱(Claude Desktop 등)이 실행합니다

도구 3개: get_schedule(읽기), find_conflicts(규칙 계산), suggest_message(초안만 — 보내지 않음).
보내기 · 일정 변경 도구는 일부러 만들지 않았습니다. 서버가 가진 도구가 곧 AI의 권한입니다.
"""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("practice-schedule")

SCHEDULE = [
    {"day": "월", "start": "09:30", "end": "10:30", "title": "주간 팀 회의", "place": "본사 5층"},
    {"day": "월", "start": "19:00", "end": "21:30", "title": "대학원 수업", "place": "배재대 공학관"},
    {"day": "화", "start": "14:00", "end": "15:30", "title": "협력사 미팅", "place": "둔산동 협력사 사무실"},
    {"day": "화", "start": "15:00", "end": "15:30", "title": "고객 화상 통화", "place": "온라인"},
    {"day": "수", "start": "16:30", "end": "18:40", "title": "외부 세미나", "place": "유성구 컨벤션홀"},
    {"day": "수", "start": "19:00", "end": "21:00", "title": "스터디 모임", "place": "서구 카페"},
    {"day": "목", "start": "10:00", "end": "11:00", "title": "분기 실적 발표", "place": "본사 대회의실"},
    {"day": "금", "start": "08:00", "end": "18:00", "title": "서울 출장", "place": "서울"},
]


def _min(t: str) -> int:
    h, m = t.split(":")
    return int(h) * 60 + int(m)


@mcp.tool()
def get_schedule(day: str = "") -> list[dict]:
    """다음 주 가상 일정을 돌려준다. day에 '월'~'금'을 주면 그날 일정만 돌려준다."""
    return [e for e in SCHEDULE if not day or e["day"] == day]


@mcp.tool()
def find_conflicts() -> list[dict]:
    """다음 주 일정에서 시간이 겹치는 일정과, 장소가 달라 이동 시간이 30분 미만인 일정을 찾는다."""
    out = []
    for i, a in enumerate(SCHEDULE):
        for b in SCHEDULE[i + 1:]:
            if a["day"] != b["day"]:
                continue
            gap = _min(b["start"]) - _min(a["end"])
            if gap < 0:
                out.append({"type": "겹침", "day": a["day"], "a": a["title"], "b": b["title"], "minutes": -gap})
            elif gap < 30 and a["place"] != b["place"] and "온라인" not in (a["place"], b["place"]):
                out.append({"type": "이동 빠듯", "day": a["day"], "a": a["title"], "b": b["title"], "minutes": gap})
    return out


@mcp.tool()
def suggest_message(to: str, issue: str) -> str:
    """일정 문제를 알리는 메시지 '초안'을 만든다. 보내지 않는다. 보내는 것은 사람이 한다."""
    return f"{to}님, 안녕하세요. {issue} 일정 조정이 가능할지 여쭙습니다. (초안 — 보내기 전에 확인하세요)"


if __name__ == "__main__":
    mcp.run()  # 기본은 stdio: AI 앱이 이 파일을 실행하고 표준 입출력으로 대화합니다
