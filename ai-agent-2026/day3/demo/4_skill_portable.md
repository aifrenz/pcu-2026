# 장면 4 · 스킬은 들고 다닌다 — Hermes가 만든 스킬을 Claude · ChatGPT에서 쓰기

**스킬(Skill)** 은 '이런 일은 이렇게 한다'를 적은 **파일 하나(`SKILL.md`)** 입니다. Hermes는 일을 끝낸 뒤 그 방법을 스스로 스킬 파일로 저장합니다. 이 파일은 공개 표준(agentskills.io) 형식이라 **Claude에 그대로 올리거나, ChatGPT · Gemini에는 지시문으로 붙여 넣어** 같은 방법으로 일하게 할 수 있습니다.

| | 오늘 A0에서 쓴 지시문 | 스킬 |
| --- | --- | --- |
| 생김새 | 프로젝트의 지시문 칸에 쓴 글 | `SKILL.md` 파일 (이름 · 설명 + 절차 · 주의 · 확인) |
| 누가 만드나 | 내가 씀 | 내가 쓰거나, **Hermes가 일하면서 스스로** 만듦 |
| 언제 쓰이나 | 그 프로젝트 안에서 항상 | AI가 **설명을 보고 필요할 때 꺼내 씀** |
| 옮기기 | 복사해 붙여 넣기 | 파일째 옮김 (Claude는 업로드, 나머지는 붙여 넣기) |

```
강사 시연 (5분): ① Hermes가 스킬 만들기 → ② 파일 열어 보기 → ③ 다듬어 압축 → ④ Claude에 올리기 → ⑤ ChatGPT에 붙여 넣기
수강생 실습 (선택 10분): 예시 스킬을 내 AI에 넣고 회의록으로 시험 → (더 해 보기) 내 A0 지시문을 스킬로 바꾸기
```

---

## 강사 시연

### ① Hermes가 스킬을 만들게 하기

오프닝에서 디스코드로 맡긴 '브리핑' 일을 이어서 씁니다 ([장면 0](0_messenger_connect.md)).

- **저절로:** `브리핑`을 두세 번 시키면서 피드백을 줍니다 (예: `다음부터는 2개만, 맨 아래 '이번 주 한 줄'도`). Hermes는 반복할 가치가 있는 작업 · 사용자의 고침을 스킬로 저장하도록 되어 있습니다.
- **바로 만들기:** 같은 대화에 이렇게 보냅니다.

```
/learn 방금 한 브리핑 작업을 다음에도 같은 방식으로 할 수 있게 스킬로 저장해 줘. 이름은 ai-news-briefing.
```

### ② 스킬 파일 열어 보기 (WSL 터미널)

```bash
ls -lt ~/.hermes/skills | head                      # 최근에 생긴 것이 위
find ~/.hermes/skills -name SKILL.md -mmin -120     # 2시간 안에 생기거나 바뀐 스킬
cat ~/.hermes/skills/<분류>/ai-news-briefing/SKILL.md
```

**보여 줄 것:** 맨 위 `name` · `description`(언제 쓰는지), 아래 **When to Use · Procedure · Pitfalls · Verification**. "내가 준 피드백이 Procedure에 들어갔다"를 짚습니다.

### ③ 옮길 수 있게 다듬고 압축하기

Hermes 스킬에는 Hermes 전용 정보가 함께 들어 있을 수 있습니다. 다른 AI로 옮길 때는 **복사본을 만들어** 다듬습니다.

```bash
mkdir -p ~/export && cp -r ~/.hermes/skills/<분류>/ai-news-briefing ~/export/
nano ~/export/ai-news-briefing/SKILL.md
```

| 다듬을 것 | 이유 |
| --- | --- |
| 맨 위(`---` 사이)는 `name`, `description` 두 줄만 남기고 `version` · `metadata:` 아래는 지움 | Claude가 읽는 것은 이름과 설명 |
| `name`은 영어 소문자 · 숫자 · 하이픈만 (예: `ai-news-briefing`) | Claude 스킬 이름 규칙 |
| `description`은 짧게, **언제 쓰는지**가 들어가게 | AI가 이 설명을 보고 스킬을 꺼냄 |
| 본문의 Hermes 도구 이름(예: 특정 검색 도구)은 "웹 검색으로"처럼 일반 말로 | 다른 AI에는 그 도구가 없음 |
| 개인정보 · 키 · 내부 주소가 들어 있으면 지움 | 파일째 남에게 넘어갈 수 있음 |

압축해서 Windows 쪽으로 꺼냅니다 (WSL에서는 `C:` 드라이브가 `/mnt/c`).

```bash
sudo apt install -y zip                                  # 처음 한 번
cd ~/export && zip -r ai-news-briefing.zip ai-news-briefing
cp ai-news-briefing.zip /mnt/c/Users/<윈도우사용자이름>/Downloads/
```

zip 안에는 **폴더 하나(`ai-news-briefing/`)와 그 안의 `SKILL.md`** 가 들어 있어야 합니다.

### ④ Claude에 올리기 (Pro · Max · Team · Enterprise)

1. claude.ai → **설정 → 기능(Capabilities)** → **코드 실행 및 파일 생성**이 켜져 있는지 확인 (스킬에 필요)
2. 같은 화면의 **Skills** → **Upload skill** → ③의 zip 선택 → 목록에 생기면 **켜기**
3. **새 대화**에서 `브리핑` 또는 `브리핑 스킬로 이번 주 소식 정리해 줘`
4. 답하는 과정에 스킬을 불러온 표시가 보이면 성공입니다. 안 쓰면 "ai-news-briefing 스킬을 써서"라고 이름을 말해 줍니다.

**Claude 무료 플랜**은 스킬 업로드가 없습니다. 대신 프로젝트를 만들고 `SKILL.md`의 본문(`---` 아래)을 **지시문 칸에 붙여 넣으면** 같은 방식으로 일합니다.

### ⑤ ChatGPT · Gemini에서 쓰기

| 서비스 · 플랜 | 방법 |
| --- | --- |
| ChatGPT 무료 · Plus · Pro | 스킬 업로드 기능이 없습니다(2026년 10월 확인 기준 Business · Enterprise · Edu 전용). **새 프로젝트 → 지침**에 `SKILL.md` 본문을 붙여 넣습니다 |
| ChatGPT Business · Enterprise · Edu | 왼쪽 **Plugins → Skills → Create → Upload from your computer**로 파일 업로드 |
| Gemini | **Gem(또는 Skills) → 지침**에 `SKILL.md` 본문을 붙여 넣습니다 |

**연결 문장:** "Hermes가 디스코드에서 일하며 배운 방법을, 파일 하나로 Claude와 ChatGPT에 옮겼습니다. **일하는 방법은 특정 AI가 아니라 파일에 남습니다.**"

---

## 수강생 실습 (선택 · 10분) — 예시 스킬을 내 AI에 넣어 보기

A0 회의록 정리기를 끝낸 분이 해 봅니다. 아래 예시 스킬은 **Hermes가 만드는 스킬과 같은 형식으로 강사가 작성한 것**입니다 (오늘 A0 회의록 정리기의 지시문을 스킬로 옮긴 것).

| 예시 스킬 | 파일 보기 | Claude 업로드용 zip |
| --- | --- | --- |
| 회의록 정리기 `meeting-todo` | [`SKILL.md`](../skills/meeting-todo/SKILL.md) | [`meeting-todo.zip`](../skills/meeting-todo.zip) |
| AI 뉴스 브리핑 `ai-news-briefing` | [`SKILL.md`](../skills/ai-news-briefing/SKILL.md) | [`ai-news-briefing.zip`](../skills/ai-news-briefing.zip) |

zip은 링크를 연 뒤 오른쪽 위 **다운로드(↓, Download raw file)** 단추로 받습니다.

### 1단계 · 넣기 (내 서비스에 맞는 줄 하나만)

| 내 AI | 이렇게 |
| --- | --- |
| **Claude Pro 이상** | `meeting-todo.zip` 받기 → claude.ai **설정 → 기능 → Skills → Upload skill** → 켜기 |
| Claude 무료 · ChatGPT · Gemini | `SKILL.md` 링크를 열고 오른쪽 위 **복사(Copy raw file)** → **새 프로젝트(Gem)의 지시문 칸**에 붙여 넣기 → 저장 |

### 2단계 · 시험

새 대화에서 아래를 보냅니다 (A0 테스트 회의록을 짧게 줄인 것).

```
회의록 정리해 줘. 오늘은 10월 16일이야.

[회의록] 교내 AI 활용 경진대회 준비 2차 회의 (10월 12일 월)
참석: 한서연(위원장), 박도윤, 이하린, 정민재, 최유진
- 대회 날짜는 11월 21일(토)로 확정.
- 상금은 처음 300만 원으로 얘기했으나 예산 확인 후 총 250만 원으로 줄이기로 함.
- 포스터 시안은 이하린이 만들기로 함. 마감은 정하지 않음.
- 후원사 섭외는 다음 회의에서 다시 논의.
- 참가 신청 폼은 이번 주 안에 열기로 했는데 담당은 정하지 않음.
```

**볼 것**

| 확인 | 잘 된 결과라면 |
| --- | --- |
| 형식 | 결정 사항 · 할 일 표 · 미정 사항 · 메일 초안 네 부분 |
| 바뀐 내용 | 상금은 250만 원만 결정으로 (300만 원은 바뀐 과정 한 줄) |
| '미정' 처리 | 포스터 마감 · 폼 담당은 `미정`, '이번 주 안'은 날짜로 바꾸지 않음 |
| Claude 스킬 | 답하는 과정에 `meeting-todo` 스킬을 불러온 표시 |

**실제로 돌려 본 결과** (Claude Sonnet에 `meeting-todo` 본문을 지시문으로 주고 위 회의록을 넣음, 2026년 10월 16일)

| 확인 | 결과 | 판정 |
| --- | --- | --- |
| 형식 | 결정 사항 · 할 일 표 · 미정 사항 · 메일 초안(발송하지 않음) 네 부분 | 맞음 |
| 바뀐 내용 | "상금은 총 250만 원으로 확정 (처음 300만 원으로 논의했으나 예산 확인 후 줄임)" | 맞음 |
| '미정' 처리 | 포스터 마감 · 폼 담당 `미정`, 폼 마감은 "이번 주 안"을 그대로 두고 "오늘이 그 주 금요일이라 담당부터 정하라"고 덧붙임 | 맞음 · 기대보다 더 짚음 |

### 3단계 · 더 해 보기 · 내 A0 지시문을 스킬로 바꾸기

오늘 5단계에서 '내 것으로 한 칸 바꾼' 지시문을 들고 다닐 수 있게 스킬 파일로 만듭니다. AI에게 이렇게 보냅니다.

```
아래 지시문을 다른 AI에서도 쓸 수 있는 스킬 파일(SKILL.md)로 바꿔 줘.
- 맨 위에 --- 로 감싼 두 줄: name(영어 소문자와 하이픈), description(무엇을 하고 언제 쓰는지 한두 문장)
- 본문은 제목 다음에 When to Use / Procedure(번호 목록) / Pitfalls / Verification 네 부분
- 지시문에 없는 규칙은 지어내지 말 것
- 결과는 코드 블록 하나로

[지시문]
(여기에 내 A0 지시문을 붙여 넣기)
```

나온 내용을 메모장에 `SKILL.md`로 저장해 두면, 다음에 어떤 AI를 쓰든 이 파일 하나로 같은 비서를 다시 만들 수 있습니다. Claude Pro라면 폴더에 넣어 zip으로 압축해 업로드합니다.

---

## 주의

- **남이 만든 스킬은 열어 보고 씁니다.** 스킬은 AI에게 주는 지시라서, 안에 엉뚱한 지시나 실행 파일(`scripts/`)이 숨어 있을 수 있습니다. 회의록 속 지시를 막았던 것처럼 스킬도 출처를 확인합니다.
- 스킬 파일에 **개인정보 · API 키 · 내부 주소를 넣지 않습니다.** 파일째 공유되기 쉽습니다.
- Claude에 올린 스킬은 **내 계정에서만** 보입니다.
- Hermes에서 스킬이 바로 저장되는 것이 걱정되면 설정의 `skills.write_approval: true`로 **저장 전에 승인**을 받게 할 수 있습니다 (`/skills pending` · `/skills approve`).

출처 (2026년 10월 16일 확인): [Hermes Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) · [Claude · Using Skills](https://support.claude.com/en/articles/12512180-using-skills-in-claude) · [ChatGPT · Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
