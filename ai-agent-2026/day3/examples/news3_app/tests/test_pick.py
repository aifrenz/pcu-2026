import os, sys, unittest
from datetime import date
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from pick import parse, filter_recent, merge_duplicates, pick_top3

TODAY = date(2026, 10, 18)
SAMPLE = """1. 10/16 · 정부, 공공기관 AI 에이전트 도입 가이드라인 초안 공개 · https://example.com/news/1
2. 10/17 · 공공 AI 에이전트 가이드라인 초안 주요 내용 · https://example.com/news/2
3. 10/15 · 한빛시, 민원 상담 AI 비서 시범 운영 결과 · https://example.com/news/3
7. 10/05 · 지자체 내년도 AI 예산 편성 현황 · https://example.com/news/7
형식이 다른 줄은 무시된다"""


def fake_judge(cands, topic):
    """가짜 AI: 실제 API를 부르지 않고 앞에서부터 순서대로 고른다."""
    return [{"index": i, "reason": f"{topic} 관련"} for i in range(len(cands))]


class TestPick(unittest.TestCase):
    def test_parse_skips_bad_lines(self):
        self.assertEqual(len(parse(SAMPLE, 2026)), 4)

    def test_drop_older_than_7_days(self):
        recent = filter_recent(parse(SAMPLE, 2026), TODAY)
        self.assertNotIn("https://example.com/news/7", [a["link"] for a in recent])

    def test_merge_same_story(self):
        merged = merge_duplicates(filter_recent(parse(SAMPLE, 2026), TODAY))
        self.assertEqual(len(merged), 2)
        guide = next(a for a in merged if "가이드라인" in a["title"])
        self.assertEqual(guide["link"], "https://example.com/news/2")      # 최신 것을 남김
        self.assertEqual(guide["also"], ["https://example.com/news/1"])    # 합친 기사도 남김

    def test_merge_same_story_with_long_titles(self):
        """실제 기사처럼 제목이 길어도 같은 소식이면 합친다 (화면에서 직접 돌려 보고 찾은 버그)."""
        long = """1. 10/16 · 정부, 공공기관 AI 에이전트 도입 가이드라인 초안 공개… 민원·문서 업무에 '사람 확인 단계' 의무화 · https://example.com/news/1
2. 10/17 · "공공 AI 에이전트, 사람이 최종 확인해야" 가이드라인 초안 주요 내용 · https://example.com/news/2
3. 10/15 · 한빛시, 민원 상담 AI 비서 3개월 시범 운영 결과… 야간 문의 40% 자동 응대 · https://example.com/news/3"""
        merged = merge_duplicates(parse(long, 2026))
        self.assertEqual(len(merged), 2)

    def test_fewer_than_three_is_ok(self):
        top = pick_top3(parse(SAMPLE, 2026), TODAY, "공공 행정", fake_judge)
        self.assertEqual(len(top), 2)               # 억지로 3개를 채우지 않음
        self.assertTrue(all(t["reason"] for t in top))

    def test_empty_input(self):
        self.assertEqual(pick_top3([], TODAY, "공공 행정", fake_judge), [])

    def test_judge_bad_index_is_ignored(self):
        bad = lambda c, t: [{"index": 99, "reason": "x"}, {"index": 0, "reason": "ok"}]
        top = pick_top3(parse(SAMPLE, 2026), TODAY, "공공 행정", bad)
        self.assertEqual([t["reason"] for t in top], ["ok"])


    def test_mock_judge_puts_topic_match_first(self):
        from llm import mock_judge
        cands = merge_duplicates(filter_recent(parse(SAMPLE, 2026), TODAY))
        ranked = mock_judge(cands, "민원 상담")
        self.assertIn("민원", cands[ranked[0]["index"]]["title"])

    def test_mock_judge_does_not_pad(self):
        from llm import mock_judge
        cands = merge_duplicates(filter_recent(parse(SAMPLE, 2026), TODAY))
        self.assertEqual(mock_judge(cands, "반도체 투자"), [])     # 관련 없으면 비워 둠

    def test_no_key_means_mock(self):
        import llm
        os.environ.pop("ANTHROPIC_API_KEY", None)
        cwd = os.getcwd(); os.chdir(os.path.dirname(__file__))   # .env가 없는 폴더에서
        try:
            self.assertIs(llm.get_judge(), llm.mock_judge)
        finally:
            os.chdir(cwd)


if __name__ == "__main__":
    unittest.main()
