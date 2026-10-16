"""웹 화면 한 장: 주제와 기사 목록을 넣으면 3개를 골라 카드로 보여 준다.

    python app.py        → 브라우저에서 http://127.0.0.1:8000
"""
import html
from datetime import date
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

from llm import get_judge
from pick import parse, pick_top3

PAGE = """<!doctype html><meta charset="utf-8"><title>뉴스 3개</title>
<style>body{{font-family:sans-serif;max-width:760px;margin:2em auto;padding:0 1em}}textarea,input{{width:100%}}
.card{{border:1px solid #ccc;border-radius:8px;padding:.8em;margin:.6em 0}}small{{color:#666}}</style>
<h1>주제를 넣으면 뉴스 3개</h1><p><small>판단: {mode}</small></p>
<form method="post"><p>주제 <input name="topic" value="{topic}"></p>
<p>오늘 날짜 <input name="today" value="{today}" placeholder="2026-10-18"></p>
<p>기사 목록 (한 줄에 하나: <code>1. 10/16 · 제목 · 링크</code>)<textarea name="articles" rows="10">{articles}</textarea></p>
<button>3개 고르기</button></form>{result}"""


class Handler(BaseHTTPRequestHandler):
    def _send(self, topic="", today="", articles="", result=""):
        mode = "Claude API" if get_judge().__name__ == "claude_judge" else "모의 판단 (키 없음)"
        body = PAGE.format(mode=mode, topic=html.escape(topic), today=html.escape(today),
                           articles=html.escape(articles), result=result).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self._send(today=date.today().isoformat())

    def do_POST(self):
        form = parse_qs(self.rfile.read(int(self.headers.get("Content-Length", 0))).decode())
        topic, today_s, text = (form.get(k, [""])[0].strip() for k in ("topic", "today", "articles"))
        if not topic or not text:
            return self._send(topic, today_s, text, "<p>주제와 기사 목록을 넣어 주세요.</p>")  # 빈 입력이면 AI를 부르지 않음
        today = date.fromisoformat(today_s) if today_s else date.today()
        top = pick_top3(parse(text, today.year), today, topic, get_judge())
        cards = "".join(f'<div class="card"><b>{html.escape(t["title"])}</b> <small>{t["date"]}</small><br>'
                        f'{html.escape(t["reason"])}<br><a href="{html.escape(t["link"])}">{html.escape(t["link"])}</a></div>'
                        for t in top) or "<p>최근 7일 안에 고를 기사가 없습니다.</p>"
        self._send(topic, today_s, text, f"<h2>고른 기사 {len(top)}개</h2>{cards}")


if __name__ == "__main__":
    print("http://127.0.0.1:8000  (끄기: Ctrl+C)")
    HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
