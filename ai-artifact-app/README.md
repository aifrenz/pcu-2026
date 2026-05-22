# AI Artifact App — WebView 래핑 실습

생성형 AI 강의 실습용 프로젝트입니다.
**웹앱(Claude Artifact)을 스마트폰 앱 화면 안에서 실행되도록 감싸는** 모바일 프로토타입입니다.

> ⚠️ 이 실습은 새 앱을 처음부터 개발하는 것이 아닙니다.
> 이미 있는 웹 URL을 Expo + React Native WebView라는 "앱 껍데기"로 감싸는 **하이브리드 앱** 방식입니다.
> 빠르게 데모할 수 있지만, 인터넷이 끊기면 동작하지 않고 카메라·푸시 같은 네이티브 기능은 쓸 수 없습니다.

---

## 0. 준비물

| 항목 | 설명 |
|---|---|
| Windows PC | Node.js / npm 설치 완료 (강사가 미리 확인) |
| 스마트폰 | **Expo Go** 앱 설치 (Android: Play 스토어 / iPhone: App Store) |
| Wi-Fi | PC와 스마트폰이 **같은 Wi-Fi**에 연결되어 있어야 함 |
| Expo 계정 | APK 빌드 단계(6장 이후)에서만 필요 — [expo.dev](https://expo.dev) 무료 가입 |

> 💡 **명령어를 입력하는 곳**: VSCode 화면 아래쪽의 **터미널(PowerShell)** 입니다.
> 메뉴 `Terminal → New Terminal` 로 열 수 있습니다.

---

## 1. 프로젝트 폴더로 이동하기

터미널을 열면 가장 먼저 실습 폴더 안으로 들어가야 합니다.

```powershell
cd ai-artifact-app
```

- `cd` 는 "폴더 이동(change directory)" 명령입니다.
- 이동에 성공하면 터미널 줄 앞의 경로가 `...\ai-artifact-app` 으로 바뀝니다.
- 앞으로 나오는 모든 명령은 **이 폴더 안에서** 실행합니다.

---

## 2. 의존성 설치하기 (`npm install`)

이 앱은 `expo`, `react-native-webview` 같은 **외부 부품(패키지)** 을 사용합니다.
그 부품들이 모인 `node_modules` 폴더가 있어야 앱이 실행됩니다.

### 내 폴더에 `node_modules` 폴더가 있나요?

VSCode 왼쪽 파일 목록에서 `node_modules` 폴더가 보이는지 확인하세요.

| 상황 | 해야 할 일 |
|---|---|
| **`node_modules` 폴더가 없음** (GitHub/ZIP으로 받은 경우 대부분 여기 해당) | 아래 `npm install` **반드시 실행** |
| **`node_modules` 폴더가 이미 있음** (강사가 통째로 복사해 준 경우) | `npm install` **생략 가능**, 바로 3장으로 |

```powershell
npm install
```

- `package.json` 파일에 적힌 부품 목록을 보고, 인터넷에서 자동으로 내려받습니다.
- 처음에는 수백 MB라 **1~5분** 정도 걸릴 수 있습니다. (인터넷 속도에 따라 다름)
- `added 470 packages` 같은 메시지가 나오고 다시 입력 줄이 보이면 완료입니다.
- ⚠️ 이 단계를 건너뛰면 3장에서 `Unable to resolve "react-native-webview"` 오류가 납니다.

> 강의장 인터넷이 느릴 수 있으니, **수업 시작 전에 미리** 실행해 두는 것을 권장합니다.

---

## 3. 스마트폰에서 실행하기 (Expo Go) — 가장 먼저 해 볼 것

PC와 스마트폰이 **같은 Wi-Fi**에 연결되어 있는지 다시 확인한 뒤 실행합니다.

```powershell
npx expo start
```

- 우리가 만든 앱 코드를 PC에서 컴파일해 폰으로 보내주는 **개발 서버**를 켜는 명령입니다.
- 실행하면 터미널에 **QR 코드**가 나타납니다.

QR 코드를 스캔해 앱을 엽니다.

- **Android**: Expo Go 앱 실행 → `Scan QR code` → 터미널의 QR 코드 스캔
- **iPhone**: 폰의 **기본 카메라** 앱으로 QR 코드 스캔 → 뜨는 알림을 눌러 Expo Go로 열기

폰 화면에서 다음 순서로 보이면 **성공**입니다.

1. "앱을 불러오는 중입니다..." 메시지 (로딩)
2. 웹 서비스 화면 표시

테스트를 끝내려면 터미널에서 **`Ctrl + C`** 를 누릅니다 (개발 서버 종료).

> **연결이 안 될 때**: 같은 Wi-Fi인데도 폰에서 앱이 안 열리면 아래 명령으로 다시 시도하세요.
> ```powershell
> npx expo start --tunnel
> ```
> (속도는 조금 느리지만 네트워크 제약을 우회합니다.)

### (선택) 폰 없이 PC 브라우저로 빠르게 확인

```powershell
npx expo start --web
```

브라우저가 자동으로 열립니다. 단, 웹 모드에서는 WebView가 iframe으로 동작해 실제 폰과 다를 수 있으니 **빠른 확인용**으로만 사용하세요.

---

## 4. 실행 화면 점검 체크리스트

앱이 떴다면 아래 항목을 직접 확인해 보세요.

- [ ] 로딩 메시지("앱을 불러오는 중입니다...")가 잠깐 보였는가
- [ ] 웹 서비스 화면이 정상적으로 표시되는가
- [ ] 화면 위쪽(시계·배터리 영역)에 내용이 가려지지 않는가
- [ ] 웹앱 안의 버튼·입력 등이 정상 동작하는가
- [ ] 인터넷을 끄면 오류 메시지가 뜨는가 (의도된 동작)

---

## 5. (참고) 이 프로젝트는 이렇게 만들어졌습니다

이미 완성된 폴더를 받았다면 이 장은 읽기만 해도 됩니다. 직접 처음부터 만들고 싶을 때 참고하세요.

```powershell
# (1) Expo + TypeScript 프로젝트 생성
npx create-expo-app@latest ai-artifact-app --template expo-template-blank-typescript

# (2) WebView 패키지 설치
cd ai-artifact-app
npx expo install react-native-webview react-native-safe-area-context
```

- 화면 코드: [App.tsx](App.tsx) — 보여줄 웹 주소는 맨 위 `ARTIFACT_URL` 상수에 있습니다.
- 앱 이름 설정: [app.json](app.json) 의 `"name"`, `"android.package"`

---

## 6. APK 만들기 — EAS CLI 설치 및 로그인

여기서부터는 폰에 직접 설치할 수 있는 **APK 파일**을 만드는 단계입니다.
APK는 Expo 클라우드 빌드 서비스(EAS)로 만듭니다. **PC에 Android 개발 도구를 설치할 필요가 없습니다.**

```powershell
# (1) EAS CLI 설치 — PC에 한 번만 하면 됩니다
npm install -g eas-cli

# (2) Expo 계정 로그인 (먼저 https://expo.dev 에서 무료 가입)
eas login
```

- `npm install -g eas-cli` : APK 빌드를 지시하는 도구를 PC 전체에 설치합니다. (`-g` = 전역 설치)
- `eas login` : 가입한 Expo 아이디·비밀번호를 입력합니다. 빌드는 내 계정으로 진행됩니다.

---

## 7. eas.json — 빌드 설정 파일

이 프로젝트에는 [eas.json](eas.json) 이 **이미 포함**되어 있어 따로 만들 필요가 없습니다.

- 핵심 설정은 `"android": { "buildType": "apk" }` 입니다.
- 이 설정 덕분에 폰에 바로 설치 가능한 `.apk` 파일이 만들어집니다. (없으면 스토어 업로드용 `.aab`가 생성됨)
- 실습에서는 **`preview`** 프로필을 사용합니다.

---

## 8. APK 빌드 명령어

```powershell
eas build --platform android --profile preview
```

- `--platform android` : 안드로이드용으로 빌드
- `--profile preview` : eas.json의 `preview` 설정(= APK 생성)을 사용
- 빌드는 **Expo 클라우드 서버**에서 진행됩니다 (내 PC 성능과 무관, 약 **10~20분** 소요).
- 완료되면 터미널에 **APK 다운로드 링크**가 표시됩니다. [expo.dev](https://expo.dev) 프로젝트 페이지에서도 받을 수 있습니다.
- 그 링크를 폰에서 열어 APK를 내려받아 설치합니다.

---

## 9. APK 설치 시 주의사항

1. **알 수 없는 앱 설치 허용**: Play 스토어를 거치지 않으므로, Android 설정 →
   앱 → 특수 권한 → "알 수 없는 앱 설치"를 허용해야 설치됩니다.
2. **인터넷 연결 필수**: 웹앱을 실시간으로 불러오므로 오프라인에서는 동작하지 않습니다.
3. **공유 URL 접근 권한 (가장 중요)**: Claude Artifact 주소가 비공개이거나
   접근이 제한되면 WebView가 빈 화면/오류를 보일 수 있습니다.
   실습 전에 PC 브라우저 **시크릿 모드**로 URL이 로그인 없이 열리는지 확인하세요.

---

## 10. 자주 발생하는 오류와 해결 방법

| 증상 | 원인 | 해결 |
|---|---|---|
| `Unable to resolve "react-native-webview"` | 2장 `npm install`을 안 함 | `npm install` 실행 후 다시 시도 |
| `'npx'은(는) ... 인식할 수 없습니다` | Node.js 미설치 | Node.js 설치 후 터미널 재시작 |
| 흰 화면만 보임 | URL이 비공개/차단됨 | 시크릿 모드로 URL 확인, Artifact를 공개 공유로 설정 |
| "웹앱을 불러오지 못했습니다" | 인터넷 끊김 / URL 오타 | 네트워크 확인, App.tsx의 `ARTIFACT_URL` 점검 |
| QR 스캔해도 폰에서 안 열림 | PC·폰이 다른 네트워크 | 같은 Wi-Fi 연결, 안 되면 `npx expo start --tunnel` |
| `eas: command not found` | EAS CLI 미설치 | `npm install -g eas-cli` 실행 |
| 빌드가 `.aab`만 생성됨 | eas.json 설정 누락 | `"buildType": "apk"` 설정 확인 |
| APK "앱이 설치되지 않음" | 알 수 없는 앱 설치 차단 | Android 설정에서 설치 권한 허용 |
| 코드를 고쳤는데 화면에 반영 안 됨 | 캐시 문제 | `npx expo start -c` (캐시 초기화 후 재시작) |
