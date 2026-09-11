# micro-ROS 로봇

**ROS 2와 Raspberry Pi Pico 2 W로 만드는 micro-ROS 로봇**

FreeRTOS·Wi-Fi·rclc·Embedded C로 배우는 실전 로봇 제어

책의 공개 실습 자료를 준비하는 저장소입니다. **현재는 초기 안내와 폴더 구조만 제공하며, 실행 가능한 교육용 펌웨어와 도서 샘플은 아직 없습니다.**

[책 소개](BOOK.md) · [학습 목차](docs/chapters.md) · [시작 안내](docs/getting-started.md) · [기준 코드](docs/references.md) · [검증 현황](docs/validation.md)

## 준비 중인 실습

FreeRTOS 태스크, micro-ROS Agent 연결, Wi-Fi 사용자 정의 전송 계층, rclc 통신, 서보·터치·버저·OLED·WS2812를 거쳐 통합 로봇을 구성할 예정입니다.

## 자료 구성

- firmware/: 교육용 보드 펌웨어 (구현 예정)
- host_ws/src/: ROS 2 호스트 패키지 (구현 예정)
- hardware/: 검증된 배선·핀맵·부품 안내 (작성 예정)
- config/: 실제 접속 정보 없는 설정 예제
- tests/: 보드·호스트 검증 절차 (작성 예정)
- docs/: 목차·시작 안내·출처·검증 기록
- samples/: 별도 공개 결정 후 무료 샘플 제공

기준 코드는 [https://github.com/freshmea/micro_ros_pico_dev](https://github.com/freshmea/micro_ros_pico_dev)입니다. 현재 저장소는 원본 코드의 미러가 아닙니다. 버전 정리와 재현 검증을 거쳐 필요한 예제를 순서대로 공개합니다.

원고·전체 도서·표지 원본은 포함하지 않습니다. [이용과 출처](NOTICE)를 확인하세요.
