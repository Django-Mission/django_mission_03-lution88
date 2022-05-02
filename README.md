# django_mission_03-lution88

## BASIC MISSION
### 미션 내용 : 고객센터 관리자 페이지 구성하기

- 고객센터 앱의 모델을 관리자페이지에 등록 구성

### 목표

- Models 기반으로 Admin 페이지 구성

- 자주묻는질문(`Faq`)
    - 목록페이지 출력 필드 : 제목, 카테고리, 최종 수정 일시
    - 검색 필드 : 제목
    - 필터 필드 : 카테고리

    ![image](https://user-images.githubusercontent.com/78908697/166296737-a5051021-52f3-4a67-b2c7-e64ee58ff208.png)
 

    ![basic_faq](https://user-images.githubusercontent.com/78908697/166300990-8ed6e121-2698-4e0b-b131-6d19a903eab5.gif)

- 1:1문의(`Inquiry`)
    - 목록페이지 출력 필드 : 질문 제목, 카테고리, 생성 일시, 생성자
    - 검색 필드 : 제목, 이메일, 전화번호
    - 필터 필드 : 카테고리
    - 인라인모델 : 답변(`Answer`)

- 답변(`Answer`)
    - 1:1문의 모델에 인라인모델로 추가

    ![basic_inquiry](https://user-images.githubusercontent.com/78908697/166303191-5e3e3522-698b-443b-ac83-a2d498b96c70.gif)


## ADVANCED MISSION
### 미션 내용 : 기본 관리자 페이지의 사용성 개선 및 답변 상태 관리 기능 추가

### 목표

- 고객센터 담당자 업무 효율을 위한 사용성 개선
- 1:1문의 상태관리를 통한 고객응대 효율 향상

### 요구사항

- 1:1문의(`Inquiry`) 모델의 “상태” 필드 추가
    - 상태 : 문의 등록, 접수 완료, 답변 완료
    - ![image](https://user-images.githubusercontent.com/78908697/166298672-fd224f3e-cadd-47be-a5fa-f802c9f6d0ce.png)
- 1:1문의(`Inquiry`) 목록, 필터에 상태 추가
- ![image](https://user-images.githubusercontent.com/78908697/166298524-7a73de87-b26a-47d7-938f-97af85fb0a09.png)
- 1:1문의 검색 필드 추가 : 사용자 모델의 `username`, `phone`, `email`
- 1:1문의 답변 완료 안내 발송 기능 추가
    - 관리자 페이지 체크된 문의 안내 발송
    - 1:1문의의 is_email, is_phone가 True인 경우 email, phone 데이터 `print()` 출력
        ※ action을 추가 학습을 위한 목적으로 실제 문자, 메일은 발송하지 않습니다.

    ![advanced_inquiry](https://user-images.githubusercontent.com/78908697/166305529-f6d7d97c-0fe8-40b0-bcec-b1f2cb37570d.gif)


