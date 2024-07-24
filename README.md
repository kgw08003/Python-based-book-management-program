# 파이썬 기반 도서관 출납 프로그램

### 멋쟁이사자처럼 python 백엔드 스쿨 첫번째 프로젝트

- 개발기간 2024.07.22 ~ 2024.07.24

사전 구상 다이어그램

![image](https://github.com/user-attachments/assets/5f848cd3-fe38-47a6-ae89-8748fb7ba39e)

#### ver. 0.1.0
- 수업에서 배운것 처럼 함수만을 이용해서 cmd창에서만 동작하도록 GUI 사용하지 않은 버전으로 제작
- 각 해당하는 txt 파일을 만들어서 txt 파일을 통해서 해당 내용 저장 및 불러오기를 이용하였다.
- https://kgw08003.tistory.com/40  해당 블로그 참조


### ver. 0.2.0
- 해당 버전은 깃허브에 저장되어있는 부분
- tkinter를 사용하여 GUI 추가
- txt 파일 대신 csv파일을 이용해서 파일 처리

## 동작 설명
#### main.py
- 역할: 프로그램의 시작 화면을 설정

#### manage_boosk.py
- 역할: 도서 정보 관리
  - 도서 추가 : 새로운 도서 추가하는 창
  - 도서 삭제 : 선택한 도서 삭제, ISBN 기준
  - 도서 검색 : 도서 검색 기능
  - 관리 창 : 도서 관리 기능

#### manage_members.py
- 역할: 회원 정보를 관리
  - 회원 추가 : 새로운 회원 추가 창
  - 회원 삭제 : 선택한 회원 삭제
  - 회원 검색 : 회원 정보 검색 기능
  - 관리 창 : 회원 관리 기능

#### manage_boorrow_records.py
- 역할: 대출 기록 관리
  - 대출 기록 추가 : 새로운 대출기록 추가 창
  - 대출 기록 삭제 : 선택한 대출기록 삭제
  - 대출 기록 검색 : 대출기록 검색 기능
  - 관리 창 : 대출 기록 관리 기능

#### manage_categories.py
- 역할: 도서 카테고리 관리
  - 카테고리 추가 : 카테고리 추가 창
  - 카테고리 삭제 : 선택한 카테고리 삭제

#### manage_publishers.py
- 역할: 출판사 정보 관리
  - 출판사 추가 : 새출판사 추가 창
  - 출판사 삭제 : 선택한 출판사 삭제
-각각 뒤로가기 버튼을 추가해서 뒤로가기 기능 제공

## 처음 동작 UI
![image](https://github.com/user-attachments/assets/42455bab-39ab-4756-9c79-4c4f178fa28e)

파이썬 부트캠프 진행하면서 처음 만든 프로젝트여서 많은 시간을 들여서 만들었지만 많이 미숙함...

