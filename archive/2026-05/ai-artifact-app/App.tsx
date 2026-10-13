// App.tsx
// "AI Artifact App" - 웹앱(Claude Artifact)을 WebView로 감싸는 프로토타입 앱
// 핵심 개념: 새 앱을 개발하는 것이 아니라, 기존 웹앱을 앱 화면 안에 띄우는 방식입니다.

import React, { useState } from 'react';
import { ActivityIndicator, StyleSheet, Text, View } from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { SafeAreaProvider, SafeAreaView } from 'react-native-safe-area-context';
import { WebView } from 'react-native-webview';

// 웹 서비스 주소는 service-url.json 파일에 분리되어 있습니다.
// 주소를 바꿀 때는 이 코드가 아니라 service-url.json 의 "url" 값만 수정하세요.
import serviceConfig from './service-url.json';

// service-url.json 에서 읽어온 웹 서비스 주소
const ARTIFACT_URL = serviceConfig.url;

export default function App() {
  // 로딩 중 여부 (true면 로딩 메시지 표시)
  const [isLoading, setIsLoading] = useState<boolean>(true);

  // 오류 발생 여부 (true면 오류 메시지 표시)
  const [hasError, setHasError] = useState<boolean>(false);

  return (
    // SafeAreaProvider: SafeAreaView가 정상 동작하기 위한 최상위 래퍼
    <SafeAreaProvider>
      {/* [요구사항 5] 상태표시줄(시계/배터리 영역) 설정 */}
      <StatusBar style="dark" />

      {/* [요구사항 4] SafeAreaView: 노치/상태표시줄에 화면이 가려지지 않도록 처리 */}
      <SafeAreaView style={styles.container}>
        {hasError ? (
          // [요구사항 7] 오류가 났을 때 보여줄 화면
          <View style={styles.messageContainer}>
            <Text style={styles.errorText}>
              웹앱을 불러오지 못했습니다.{'\n'}
              인터넷 연결 또는 공유 URL을 확인하세요.
            </Text>
          </View>
        ) : (
          // 오류가 없으면 WebView로 웹앱을 표시
          <>
            {/* [요구사항 3] WebView로 ARTIFACT_URL 로드 */}
            <WebView
              // [요구사항 10] WebView가 화면 전체를 채우도록 스타일 적용
              style={styles.webview}
              source={{ uri: ARTIFACT_URL }}
              // [요구사항 8] 웹앱 내부의 JavaScript 실행 허용
              javaScriptEnabled={true}
              // [요구사항 9] DOM Storage(localStorage 등) 허용
              domStorageEnabled={true}
              // 로딩이 시작되면 로딩 상태로 전환
              onLoadStart={() => setIsLoading(true)}
              // 로딩이 끝나면 로딩 상태 해제
              onLoadEnd={() => setIsLoading(false)}
              // 페이지 로드 자체가 실패한 경우 오류 처리
              onError={() => {
                setIsLoading(false);
                setHasError(true);
              }}
              // 서버가 4xx/5xx 같은 오류 응답을 준 경우도 오류 처리
              onHttpError={() => {
                setIsLoading(false);
                setHasError(true);
              }}
            />

            {/* [요구사항 6] 로딩 중일 때 화면 위에 겹쳐서 메시지 표시 */}
            {isLoading && (
              <View style={styles.loadingOverlay}>
                <ActivityIndicator size="large" />
                <Text style={styles.loadingText}>앱을 불러오는 중입니다...</Text>
              </View>
            )}
          </>
        )}
      </SafeAreaView>
    </SafeAreaProvider>
  );
}

// 화면 스타일 정의
const styles = StyleSheet.create({
  // 전체 화면을 채우는 컨테이너
  container: {
    flex: 1,
    backgroundColor: '#ffffff',
  },
  // WebView가 남은 공간을 모두 차지하도록 설정
  webview: {
    flex: 1,
  },
  // 로딩/오류 메시지를 화면 가운데에 표시하기 위한 컨테이너
  messageContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 24,
  },
  // 로딩 중 화면 전체를 덮는 반투명 오버레이 (부모 영역 전체를 덮음)
  loadingOverlay: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'rgba(255, 255, 255, 0.9)',
  },
  // 로딩 메시지 텍스트 스타일
  loadingText: {
    marginTop: 12,
    fontSize: 16,
    color: '#333333',
  },
  // 오류 메시지 텍스트 스타일
  errorText: {
    fontSize: 16,
    color: '#cc0000',
    textAlign: 'center',
    lineHeight: 24,
  },
});
