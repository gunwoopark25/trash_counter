# trash_counter
울산대학교 임베디드 시스템때 stm보드를 활용한 파이썬 코드

파이썬을 통해 stm 보드를 통해 받은 데이터를 pc에 저장한 후 계산하여 html을 통해 홈페이지에 업로드하는 형식
아래는 너의 디렉토리 구조를 README.md에 그대로 넣을 수 있는 마크다운(Markdown) 형식으로 정리한 예야. 복사해서 README.md에 붙여넣기만 하면 돼.

## 📁 Project Directory Structure

```
PROJECT/
├── static/
│   ├── data/
│   │   ├── data.csv
│   │   └── updata.csv
│   ├── output/
│   │   └── monthly_trash_chart.png
│   ├── script.js
│   └── style.css
├── templates/
│   └── index.html
├── fetch_data.py
├── ftp_upload.py
├── import csv.py
├── main.py
└── output.html
```

### 📌 Description of Key Components

- `static/`: 정적 파일(css, js, 이미지 등)을 보관
  - `data/`: 입력 데이터 (CSV 형식)
  - `output/`: 시각화 결과물 이미지
- `templates/`: HTML 템플릿 파일 (Flask 등 백엔드 프레임워크 연동용)
- `main.py`: 메인 실행 스크립트
- `fetch_data.py`: 외부에서 데이터 가져오는 스크립트
- `ftp_upload.py`: FTP 업로드 기능 스크립트
- `output.html`: 결과 HTML 파일
