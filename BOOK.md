# micro-ROS 로봇

**ROS 2와 Raspberry Pi Pico 2 W로 만드는 micro-ROS 로봇**

Embedded C·FreeRTOS·micro-ROS로 배우는 고정형 로봇·이족보행형 로봇 설계와 제작

**집필 중입니다.** 6부 24장 본문 초안을 작성했으며, 로컬 제어에서 FreeRTOS·ROS 2 연결·기구 제작·장애 시험·재현으로 이어지는 제작 중심 구성을 갖춥니다. 기본 경로는 고정형 로봇, 선택 경로는 이족보행형 로봇입니다.

[1–3장 무료 샘플 PDF](samples/micro-ros-robot-ch01-03-sample.pdf)에서 임무 설계, 개발 환경, Embedded C 학습을 미리 볼 수 있습니다. 전체 초안의 24장에는 AI와 함께 문제를 검토하는 학습 활동을 두었습니다. 현재 공개된 본문은 이 샘플 범위입니다.

집필 과정에서 PC 논리 예제와 ROS 2 호스트 왕복을 시험했습니다. 이 결과는 보드·Agent·직렬·Wi-Fi·FreeRTOS 통합이나 실물 제작·보행 검증을 뜻하지 않습니다. 교육용 통합 코드·최종 도면·실물 검증은 후속 작업이며, 공개 저장소에는 완성된 펌웨어·호스트 패키지가 없습니다. 자세한 범위는 [검증 현황](docs/validation.md)을 확인하세요.

- 대상 보드: Raspberry Pi Pico 2 W
- 핵심 주제: ROS 2, micro-ROS, FreeRTOS, Wi-Fi, rclc, Embedded C
- 기준 코드: [https://github.com/freshmea/micro_ros_pico_dev](https://github.com/freshmea/micro_ros_pico_dev)
- 기준 커밋: `393f96b6e484b5c70245b821dddd3aca2d7cc1fc`
- ROS 배포판·Pico SDK·FreeRTOS·툴체인 버전: 통합 검증 후 확정
- 저자: 최수길
- 출판사: 마담
- 집필 상태: 6부 24장 본문 초안, 집필·검증 진행 중
- ISBN: 미정
- 발행일: 미정
- 구매 링크: 미정

[24장 학습 목차](docs/chapters.md) · [시작 안내](docs/getting-started.md) · [샘플 이용 안내](samples/README.md)
