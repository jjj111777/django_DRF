# 스파르타 마켓 (Sparta Market)

스파르타 마켓은 중고 물품 거래 플랫폼입니다. 이 프로젝트는 Django REST Framework(DRF)를 사용하여 백엔드 API를 구현했습니다. 사용자들은 상품을 등록하고, 수정하고, 삭제할 수 있습니다. 또한, 사용자 회원가입, 로그인, 프로필 조회 기능을 제공합니다.

## 기능
1. **회원가입**
   - 사용자 이름, 이메일, 비밀번호 등으로 회원가입을 할 수 있습니다.
   - 성공적인 회원가입 후, 인증 토큰을 제공합니다.

2. **로그인**
   - 사용자 이름과 비밀번호로 로그인하여 인증 토큰을 받습니다.
   - 로그인 후, API 요청 시 이 토큰을 사용하여 인증합니다.

3. **상품 등록**
   - 사용자는 상품을 등록할 수 있습니다.
   - 상품에는 제목, 설명, 이미지가 포함됩니다.

4. **상품 목록 조회**
   - 모든 사용자는 등록된 상품 목록을 조회

5. **상품 수정**
   - 사용자는 자신이 등록한 상품만 수정

6. **상품 삭제**
   - 사용자는 자신이 등록한 상품만 삭제

## 설치 방법
1. Git을 이용해 프로젝트를 클론론

   ```bash
   git clone https://github.com/jjj111777/django_DRF.git
