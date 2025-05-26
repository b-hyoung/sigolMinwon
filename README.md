## 추가목록
### 공무원
- api 현장작업중 을 클릭하면 조치자 이름 보내줄 것(일단미뤄)


# 🧾 의성군 스마트 생활도우미

**AI가 민원을 정리해주는 시골형 스마트 민원 접수 시스템**

> 주민이 입력한 자유 민원을 AI가 요약·분류하고, 위치와 함께 DB에 저장하여  
> 공무원이 쉽게 확인·처리할 수 있도록 만든 민원 자동화 플랫폼입니다.

---

## 🛠 기술 스택

| 구분 | 기술 |
|------|------|
| 프론트엔드 | React, TailwindCSS |
| 백엔드 | FastAPI |
| AI 분석 | Gemini API (Google) |
| DB | Firebase Firestore ( 미정) |
| 위치 기반 | 네이버 지도 API |
| 인증 시스템 | 아임포트 휴대폰 본인인증 |
| 개발환경 | Docker (컨테이너 기반 개발 및 배포) |
| 디자인 |[피그마](https://www.figma.com/design/UkxLT3g3P5suimQzgmGCqq/Untitled?node-id=0-1) / 클릭 시 이동
---
## 👥 기여자 및 프로젝트 인원

| 이름 | 역할 | GitHub |
|------|------|--------|
| 박형석 | 기획, 프론트엔드, 구조 설계 | [@b-hyoung](https://github.com/b-hyoung) |
| (미정) | 백엔드 개발 (FastAPI, Firestore 연동) | - |
| (미정) | AI 분석 모델 연동 (Gemini API 설계 및 처리) | - |
| (미정) | 모바일 UI 및 반응형 최적화 | - |
| (미정) | 관리자 페이지 UX 설계 및 데이터 시각화 | - |
| (미정) | QA 및 테스트 자동화 | - |

## 📊 핵심 기능 요약

- **AI 기반 민원 요약 및 카테고리 분류**
- **민원 위치 자동 수집 및 지도 시각화**
- **민원 작성, 수정, 삭제 및 상태 확인 (처리/미처리)**
- **공무원 전용 관리자 페이지 (민원 목록 + 지도 기반 확인)**
- **유사 민원 자동 추천 및 우선순위 표시**
- **악성 민원 신고 및 제재 시스템**
- **향후 커뮤니티 기능 (좋아요, 댓글 등)**

---

## 🔁 사용자 흐름 시나리오

```txt
1. 민원인이 “가로등 고장났어요” 입력
2. AI가 자동 요약 → “가로등 고장”, 카테고리: 조명
3. 위치 수집 → Firestore 저장
4. 공무원은 지도 기반으로 확인 → 클릭 시 민원 상세 정보 확인
```
---

## 🧑‍💼 역할/화면 구조

### 🙋 민원인

- 로그인 / 회원가입 (휴대폰 본인인증)
- 민원 작성 (내용 + 이미지 + 위치)
- AI 자동 요약 및 카테고리 분류 확인
- 내가 작성한 민원 리스트 보기 (수정/삭제)


### 🧑‍💼 공무원

- 로그인 / 회원가입 (공무원 인증 포함) / 휴대폰 인증
- Google Maps 기반 민원 위치 확인 (위급도 핀 표시)
- AI 기반 우선순위/유사도/긴급도 자동 추천
- 민원 해결 처리 (내용/이미지 첨부)

## 추후 추가 목록
- 악성 민원 사용자 경고 표시 + 신고 처리 기능
- 향후: 민원 커뮤니티에서 좋아요/댓글 참여
---

## 🔒 인증 API 요약

| 기능 | Method | 경로 | 요청 | 응답 |
|------|--------|------|------|------|
| 회원가입 | POST | `/api/sign` | id, password, name, role | success, user |
| ID 중복검사 | GET | `/api/auth/check-id?id=user123` | query | available, message |
| 본인 인증 확인 | POST | `/api/sign` | imp_uid | token, user |
| 로그인 | POST | `/api/login` | id, password | token, user |

> 회원가입 시 IMP 인증 성공 후 imp_uid와 함께 요청 필요
<details>
  
## 🔐 회원가입 / 로그인 API 정리

### 📋 회원가입 흐름

1. ID 중복 확인 → `/api/auth/check-id?id=user123`
2. 휴대폰 인증 (아임포트 IMP 사용)
   - 인증 성공 시 `imp_uid` 수신
3. 최종 회원가입 → `/api/sign`
   - 성공 시 `token` + `user` 정보 수신

---

### 🧾 [회원가입 API]

**POST** `/api/sign`

#### 요청 예시:
```json
{
  "id": "gimilhyung",
  "password": "P@ssword123",
  "password2": "P@ssword123",
  "name": "김일형",
  "role": "user" // 또는 "admin"
}
```

> ✅ `id`는 3자 이상,  
> ✅ `password`는 8자 이상 + 특수문자 포함,  
> ❌ `password2` 불일치 시 오류 반환

#### 응답 (성공):
```json
{
  "success": true,
  "message": "회원가입이 완료되었습니다.",
  "user": {
    "id": "user123",
    "name": "김민수"
  }
}
```

#### 응답 (실패 예시):
```json
{
  "success": false,
  "message": "비밀번호가 일치하지 않습니다."
}
```

---

### 🔍 [ID 중복 검사]

**GET** `/api/auth/check-id?id=user123`

#### 응답 (중복 아님):
```json
{
  "available": true,
  "message": "사용 가능한 아이디입니다."
}
```

#### 응답 (중복됨):
```json
{
  "available": false,
  "message": "이미 사용 중인 아이디입니다."
}
```

---

### 🔐 [로그인 API]

**POST** `/api/login`

#### 요청:
```json
{
  "id": "rlaqkq",
  "password": "password"
}
```

#### 응답:
```json
{
  "success": true,
  "message": "로그인 성공",
  "token": "JWT토큰값",
  "user": {
    "id": "rlaqkq",
    "name": "홍길동",
    "role": "user" // 또는 "admin"
  }
}
```

> 모든 인증 API 요청 시, 이후 요청 헤더에 `Authorization: Bearer <token>` 필요

</details>


## 📮 민원 API 명세

| 기능 | Method | 경로 | 요청 | 응답 |
|------|--------|------|------|------|
| 민원 등록 | POST | `/api/complaints` | content, img, location | title, summary, category, priorityScore |
| 전체 조회 | GET | `/api/complaints` | category, status (optional) | 민원 리스트 |
| 상세 조회 | GET | `/api/complaint/:id` | param | 민원 상세 정보 |
| 수정 | PATCH | `/api/complaint/edit/:id` | content, image | success, id |
| 삭제 | DELETE | `/api/complaint/delete/:id` | param | success, id |
| 처리 완료 | PATCH | `/api/complaint/resolve/:id` | - | 처리 상세 응답 |

> 모든 민원 API 요청은 `Authorization: Bearer <token>` 헤더 필요
---
<details>
  ## 📨 민원 관련 API 정리

> 모든 요청은 인증된 사용자만 접근 가능하며, `Authorization: Bearer <JWT>` 헤더 필요

---

### 🆕 민원 생성

**POST** `/api/complaints`

```json
요청:
{
  "content": "○○동 하수구에서 악취가 심하게 납니다. 확인 부탁드립니다.",
  "img": "data:image/png;base64,...",
  "location": {
    "lat": 36.3390,
    "lng": 128.6957,
    "address": "경북 의성군 금성면 ○○길"
  }
}
```

```json
응답 (AI 분석 포함):
{
  "title": "하수구 악취 문제",
  "img": "data:image/png;base64,...",
  "summary": "○○동 하수구 악취 민원 발생",
  "category": "환경",
  "priorityScore": 4
}
```

---

### 📋 민원 전체 조회

**GET** `/api/complaints`

**Query Parameters (선택):**
- `category=환경`
- `status=pending` 또는 `status=resolved`

```json
응답:
[
  {
    "id": 42,
    "title": "하수구 악취 문제",
    "category": "환경",
    "status": "pending",
    "img": "base64",
    "createdAt": "2025-05-20",
    "priorityScore": 4,
    "location": {
      "lat": 36.3390,
      "lng": 128.6957,
      "address": "경북 의성군 금성면 ○○길"
    }
  },
  {
    "id": 43,
    "title": "가로등이 꺼져 있어요",
    "category": "조명",
    "status": "resolved",
    "createdAt": "2025-05-18",
    "priorityScore": 2,
    "location": {
      "lat": 36.3390,
      "lng": 128.6957,
      "address": "경북 의성군 금성면 ○○길"
    }
  }
]
```

---

### 🔎 민원 상세 조회

**GET** `/api/complaint/:id`

```json
응답:
{
  "id": 42,
  "title": "하수구 악취 문제",
  "content": "하수구 악취문제가 너무 심합니다.",
  "category": "환경",
  "status": "pending",
  "createdAt": "2025-05-20",
  "location": {
    "lat": 36.3390,
    "lng": 128.6957,
    "address": "경북 의성군 금성면 ○○길"
  }
}
```

---

### 🛠 민원 수정

**PATCH** `/api/complaint/edit/:id`

```json
요청:
{
  "content": "냄새가 더 심해졌습니다. 빠른 처리 부탁드립니다.",
  "image": "data:image/png;base64,..."
}
```

```json
응답:
{
  "success": true,
  "message": "민원 수정 완료",
  "id": 42
}
```

---

### ❌ 민원 삭제

**DELETE** `/api/complaint/delete/:id`

```json
응답:
{
  "success": true,
  "message": "민원 삭제 완료",
  "id": 42
}
```

---

### ✅ 민원 해결 처리 (기본 버전)

**PATCH** `/api/complaint/resolve/:id`

```json
응답:
{
  "id": 42,
  "resolvedBy": "공무원 홍길동",
  "resolutionContent": "막힌 하수구 청소 완료. 주변 악취 해소됨.",
  "resolutionImage": "https://cdn.site.com/resolved/42.jpg",
  "resolutionDate": "2025-05-20"
}
```

```json
요약 응답:
{
  "success": true,
  "message": "민원 처리 완료로 변경되었습니다.",
  "id": 42,
  "status": "resolved"
}
```

---

### 🆕 민원 해결 처리 (이미지/내용 포함 POST 방식)

**POST** `/api/complaint/resolved/:id`

```json
요청:
{
  "content": "민원 해결 완료했습니다.",
  "img": "data:image/png;base64,...",
  "location": {
    "lat": 36.3390,
    "lng": 128.6957,
    "address": "경북 의성군 금성면 ○○길"
  }
}
```

```json
응답:
{
  "success": true,
  "message": "민원 해결 완료",
  "id": 42
}
```

</details>

## 🤖 AI 처리 예시 (Gemini API)

**요청**

```json
{
  "content": "○○동 골목 하수구가 막혀서 악취가 너무 심해요.",
  "image": "data:image/png;base64,..."
}
