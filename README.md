# micro-ROS 로봇

**ROS 2와 Raspberry Pi Pico 2 W로 만드는 micro-ROS 로봇**

Embedded C·FreeRTOS·micro-ROS로 배우는 고정형 로봇·이족보행형 로봇 설계와 제작

저자 **최수길** · 출판사 **마담** · **집필 중**

독자가 임무를 정하고 작은 로봇 한 대를 설계·제작·검증하는 책입니다. 현재 **6부 24장 본문 초안**을 작성했으며, [1–3장 무료 샘플 PDF](samples/micro-ros-robot-ch01-03-sample.pdf)를 공개합니다. ISBN과 발행일은 미정입니다.

**이 공개 저장소는 안내 문서와 샘플을 제공합니다. 실행 가능한 교육용 통합 펌웨어와 ROS 2 호스트 패키지는 아직 포함하지 않습니다.** PC 논리 검사와 ROS 2 호스트 시험 기록이 있지만, 보드·Agent 통신과 실물 로봇의 통합 검증은 완료되지 않았습니다.

[책 소개](BOOK.md) · [24장 학습 목차](docs/chapters.md) · [시작 안내](docs/getting-started.md) · [무료 샘플 안내](samples/README.md) · [기준 코드](docs/references.md) · [검증 현황](docs/validation.md)

## 준비 중인 실습

로컬 제어 → FreeRTOS → ROS 2 연결 → 기구 제작 → 장애 시험·재현 순으로 배웁니다. 기본 경로는 두 팔과 터치·표시 장치로 반응하는 고정형 로봇이며, 선택 경로는 네 관절을 제어하는 이족보행형 로봇입니다. 두 경로의 최종 예제·BOM·배선·기구와 동작 조건은 실물 검증 후 확정합니다.

## 자료 구성

- firmware/: 교육용 보드 펌웨어 안내 (실행 코드 미공개)
- host_ws/src/: ROS 2 호스트 패키지용 자리 (실행 코드 미공개)
- hardware/: 배선·핀맵·부품 안내 (검증 자료 준비 중)
- config/: 실제 접속 정보 없는 설정 예제
- tests/: 보드·호스트 검증 절차 안내 (실행 가능한 통합 시험 미공개)
- docs/: 목차·시작 안내·출처·검증 기록
- samples/: 1–3장 무료 샘플 PDF와 이용 안내

기준 코드는 [https://github.com/freshmea/micro_ros_pico_dev](https://github.com/freshmea/micro_ros_pico_dev)입니다. 현재 저장소는 원본 코드의 미러가 아닙니다. 버전 정리와 재현 검증을 거쳐 필요한 예제를 순서대로 공개합니다.

공개 범위는 책 소개·24장 목차·검증 현황과 1–3장 샘플입니다. 전체 원고·전체 도서·표지와 그림 원본은 포함하지 않습니다. [이용과 출처](NOTICE)를 확인하세요.
