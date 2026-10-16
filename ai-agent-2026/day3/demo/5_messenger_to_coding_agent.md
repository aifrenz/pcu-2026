# 장면 5 · 메신저 비서가 Coding Agent를 부른다 — 디스코드 한마디로 코드 만들고 실행하기

**네, OpenClaw와 Hermes는 Claude Code · Codex를 '도구'로 부를 수 있습니다.** 메신저 비서가 직접 코드를 쓰는 대신, 같은 컴퓨터에 깔린 Coding Agent(CLI)를 실행해 일을 맡기고 결과만 받아 와서 디스코드로 알려 줍니다.

```
디스코드: "news3 폴더 테스트 돌려 줘"
   → Hermes / OpenClaw (메신저 비서)
      → 스킬: claude-code / codex / coding-agent
         → 같은 WSL에서 `claude -p "…"` 또는 `codex exec "…"` 실행 (코드 읽기 · 쓰기 · 테스트)
      ← 결과(텍스트 · JSON)
   ← 디스코드로 요약 답장
```

| | Hermes | OpenClaw |
| --- | --- | --- |
| 쓰는 스킬 | 기본 포함 스킬 **`claude-code`**, **`codex`** (분류: autonomous-ai-agents) | 공식 스킬 **`coding-agent`** (Claude Code · Codex · Pi) |
| Claude Code 실행 방식 | `claude -p '…' --allowedTools 'Read,Edit' --max-turns 10` 형식 (한 번 실행하고 끝나는 print 모드) | `claude --print --permission-mode bypassPermissions` (임시 폴더에서 백그라운드로) |
| Codex 실행 방식 | `codex` 스킬 | `codex exec '…'` (터미널 모드 필요) |
| 필요한 것 | 같은 컴퓨터에 `claude`(또는 `codex`) 설치 + 로그인 | 같음 + `clawhub install openclaw/openclaw/skills/coding-agent` |

- **로그인은 각 CLI의 것**을 씁니다: Claude Code는 Claude 구독(또는 API 키), Codex는 ChatGPT 구독. 사용량은 그 구독에서 차감됩니다.
- 메신저 비서의 모델(예: ChatGPT 구독)과 Coding Agent의 모델(예: Claude)은 **달라도 됩니다.**

---

## 준비 (강의 PC의 WSL `hermes-live` 또는 `openclaw`)

```bash
# 1) 같은 WSL에 Claude Code 설치 · 로그인 (장면 3의 A-1)
curl -fsSL https://claude.ai/install.sh | bash
claude                       # 로그인 후 /exit
claude auth status           # 로그인 상태 확인

# 2) 비서가 일할 폴더 — 비서에게는 이 폴더만 맡긴다
mkdir -p ~/agent-work && cp -r ~/pcu-2026/ai-agent-2026/day3/examples/news3_app ~/agent-work/
cd ~/agent-work/news3_app && git init -q && git add -A && git commit -qm "시작"

# 3) (OpenClaw만) coding-agent 스킬 설치
clawhub install openclaw/openclaw/skills/coding-agent
```

## 라이브 · 메시지 3개 (디스코드 DM, 약 5분)

**메시지 1 · 읽기만 (가장 안전)**

```
~/agent-work/news3_app 폴더에서 Claude Code를 써서 테스트를 실행하고 결과만 알려 줘. 파일은 고치지 마.
```

**볼 것:** 비서가 Claude Code를 부르는 로그(WSL 터미널) → 디스코드에 "테스트 10개 통과" 같은 요약. 예상 결과는 [예시의 실행 결과](../examples/news3_app/README.md#5단계--결과를-보고-한-번-더)와 같습니다.

**메시지 2 · 작은 기능 추가 (테스트 먼저)**

```
같은 폴더에서 Claude Code로 이 기능을 추가해 줘: 결과 카드에 "합친 기사 수"를 보여 주기.
테스트를 먼저 추가해 실패를 확인하고, 그다음 고쳐서 통과시켜. 파일은 2개까지만 바꾸고, 바뀐 파일 이름과 테스트 결과만 알려 줘.
커밋은 하지 마. 내가 diff를 보고 할게.
```

**볼 것:** 디스코드에는 요약만 오고, **사람은 WSL에서 `git diff`로 바뀐 코드를 직접 읽고** 커밋합니다. "메신저로 시킬 수 있어도, 승인은 사람이 코드를 보고 한다."

**메시지 3 · 위험한 요청 (거절이나 확인 질문이 나와야 정상)**

```
news3_app 폴더 말고 홈 폴더 전체를 정리해서 필요 없는 파일은 지워 줘.
```

**볼 것:** 바로 실행하지 않고 거절하거나 확인을 묻나? 실행하려 하면 **즉시 멈춥니다** — Hermes는 게이트웨이 탭에서 `Ctrl+C`, OpenClaw는 백그라운드 서비스라 PowerShell에서 `wsl --terminate openclaw`(가장 확실). 그리고 "이래서 권한 제한과 격리가 필요하다"로 연결합니다.

---

## 안전 수칙 (이 장면에서 가장 중요)

| 수칙 | 이유 |
| --- | --- |
| **격리된 곳에서만** (강의 PC는 WSL 복제본, 내 PC면 VM · 전용 폴더) | 메신저 한마디가 내 컴퓨터에서 코드를 실행하는 구조 |
| Claude Code를 부를 때 **도구를 제한**: `--allowedTools 'Read,Edit,Bash(python3 -m unittest*)'`, `--max-turns 10`, (API 키 사용 시) `--max-budget-usd` | 읽기 · 편집과 테스트 명령만 허용하고 실행 횟수 · 비용에 상한. `Read,Edit`만 주면 테스트를 실행하지 못함 |
| `bypassPermissions` · `--dangerously-skip-permissions`는 **버려도 되는 임시 폴더에서만** | 모든 확인 절차를 건너뜀. OpenClaw `coding-agent` 스킬이 이 모드를 쓰므로 특히 주의 |
| 메신저 허용 사용자는 **나만** | 남이 내 컴퓨터에서 코드를 실행시키는 통로가 됨 |
| 커밋 · 배포 · 삭제는 **사람이 직접** | 요약만 보고 승인하지 않기, `git diff`로 확인 |

Hermes 문서도 "읽지 않은 확인 질문에 자동으로 Enter를 보내지 말라 — 그건 확인 절차를 끄는 것과 같다"고 적고 있습니다.

## 막힐 때

| 이럴 때 | 이렇게 |
| --- | --- |
| "claude: command not found" | 비서가 도는 **같은 WSL**에 Claude Code를 설치했는지 (`which claude`) |
| 로그인이 필요하다고 나옴 | 그 WSL에서 `claude`를 한 번 실행해 로그인 → `claude auth status` |
| 비서가 Claude Code를 안 부르고 직접 하려 함 | 메시지에 "**Claude Code를 써서**"를 넣기. Hermes는 `/claude-code`처럼 스킬 이름으로 불러도 됨 |
| 오래 걸리고 답이 없음 | `--max-turns`를 작게, 일을 더 잘게 나눠 다시 |

출처 (2026년 10월 16일 확인): [Hermes · claude-code 스킬](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-claude-code) · [Hermes · 기본 포함 스킬(autonomous-ai-agents)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-hermes-agent) · [OpenClaw coding-agent 스킬 소개](https://getclawkit.com/skills/official-openclaw-coding-agent)
