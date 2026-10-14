# 심화 1 · OpenClaw 또는 Hermes 직접 설치

강의에서 강사가 시연한 개인 AI 비서를 **본인 노트북의 Docker 안에서** 직접 띄워 봅니다. 둘 중 하나만 하면 됩니다.

| 항목 | OpenClaw | Hermes Agent |
| --- | --- | --- |
| 설치 | `git clone https://github.com/openclaw/openclaw.git` 후 `./docker-setup.sh` ([안내](https://github.com/rohitg00/awesome-openclaw)) | `git clone https://github.com/NousResearch/hermes-agent.git` 후 Docker 또는 설치 스크립트 ([안내](https://www.virtua.cloud/learn/en/tutorials/self-host-hermes-agent-vps)) |
| 모델 연결 | 개인 API 키, 또는 ChatGPT 구독 로그인 ([공식 문서](https://docs.openclaw.ai/providers/openai)) | 개인 API 키, 또는 `hermes setup --portal`로 Nous Portal |
| 메신저 | 텔레그램 @BotFather에서 봇 토큰 발급 후 등록 | 텔레그램 봇 등록 후 `hermes gateway start` |
| 확인 | 내 봇에 시나리오 카드의 일을 말로 시켜 보기 | 일을 끝낸 뒤 새 스킬 파일이 생겼는지 확인 |

- Claude 구독(Pro·Max)으로는 연결할 수 없습니다. Claude 모델은 API 키로 연결합니다.
- 텔레그램 봇 토큰도 비밀번호입니다. 화면 공유 중에 띄우지 않습니다.

## 봇에게 처음 보낼 말 (빈칸 예시)

시나리오 카드가 있으면 프로젝트 지시문을 그대로 보내면 됩니다. 막막하면 아래 중 하나를 보내세요.

```
너는 내 개인 비서야. 앞으로 내가 "브리핑"이라고 하면, 최근 7일 AI 에이전트 뉴스 중 [공공 행정] 실무자에게 중요한 3개를 골라 제목 · 한 줄 이유 · 링크로 알려 줘. 출처 없는 내용은 쓰지 마.
```

```
너는 내 회의 정리 비서야. 내가 회의록을 보내면 결정 사항, 결정하지 못한 사항, 할 일(담당·마감)을 표로 정리해 줘. 회의록에 없는 담당·마감은 '미정'으로 둬.
```

**기억 확인:** 한참 뒤에 `브리핑`이라고만 보내 보세요. 처음 설명한 형식대로 나오면 비서가 기억하고 있는 것입니다. Hermes라면 이때 새 스킬 파일이 생겼는지도 봅니다.

## 끝내기

실습이 끝나면 컨테이너를 멈추고(`docker compose down` 등), 쓰지 않는 봇 토큰과 API 키를 폐기합니다.
