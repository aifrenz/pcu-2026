"""기사 목록에서 3개 고르기 — 규칙으로 되는 일은 코드로, 판단은 AI(judge)에게."""
import re
from datetime import date

LINE = re.compile(r"^\s*\d+\.\s*(\d{1,2})/(\d{1,2})\s*·\s*(.+?)\s*·\s*(https?://\S+)\s*$")


def parse(text, year):
    """'1. 10/16 · 제목 · https://…' 형식의 줄을 기사 목록으로 바꾼다. 형식이 다른 줄은 건너뛴다."""
    out = []
    for line in text.splitlines():
        m = LINE.match(line)
        if m:
            mm, dd, title, link = m.groups()
            out.append({"date": date(year, int(mm), int(dd)), "title": title, "link": link})
    return out


def _words(title):
    return {w for w in re.findall(r"[가-힣A-Za-z0-9]+", title) if len(w) > 1}


GENERIC = {"AI"}  # 거의 모든 기사에 나오는 말은 같은 소식 판단에서 뺀다


def _same_story(a, b):
    """두 제목이 'AI'를 뺀 낱말을 3개 이상 함께 쓰면 같은 소식으로 본다."""
    wa, wb = _words(a["title"]) - GENERIC, _words(b["title"]) - GENERIC
    return len(wa & wb) >= 3


def filter_recent(articles, today, days=7):
    """규칙 1: 최근 days일 안의 기사만 (미래 날짜도 뺀다)."""
    return [a for a in articles if 0 <= (today - a["date"]).days < days]


def merge_duplicates(articles):
    """규칙 2: 같은 소식을 다룬 기사는 최신 하나만 남기고, 합친 기사 링크를 also에 남긴다."""
    kept = []
    for a in sorted(articles, key=lambda x: x["date"], reverse=True):
        dup = next((k for k in kept if _same_story(k, a)), None)
        if dup:
            dup.setdefault("also", []).append(a["link"])
        else:
            kept.append(dict(a))
    return kept


def pick_top3(articles, today, topic, judge):
    """규칙으로 거른 뒤, 남은 기사 중 무엇이 중요한지는 judge(AI)가 정한다. 3개가 안 되면 있는 만큼."""
    candidates = merge_duplicates(filter_recent(articles, today))
    if not candidates:
        return []
    ranked = judge(candidates, topic)  # [{"index": i, "reason": "..."}] 중요한 순서
    out = []
    for r in ranked[:3]:
        if 0 <= r.get("index", -1) < len(candidates):
            out.append({**candidates[r["index"]], "reason": r.get("reason", "")})
    return out
