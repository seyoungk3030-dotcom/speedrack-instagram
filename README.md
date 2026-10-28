# speedrack-instagram

@speedrack_official 자동 업로드. 매일 12:00 카드뉴스, 20:00 릴스 (KST).

- `schedule.json`: 게시 일정과 캡션. 게시물마다 `"approved": true`일 때만 실제로 올라가요 (주마다 SY 확인 후 승인).
- `media/`: 게시물 이미지·영상 (raw.githubusercontent.com 주소로 인스타가 가져가요).
- `published.json`: 올라간 게시물 기록 (같은 게시물이 두 번 올라가지 않게).
- 토큰은 매달 1일·15일 자동 갱신돼요.

필요한 Secrets (Settings → Secrets and variables → Actions):
`IG_ACCESS_TOKEN`, `IG_USER_ID`, `GH_PAT` (이 저장소 Secrets 읽기·쓰기 권한의 fine-grained 토큰).
