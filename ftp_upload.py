from ftplib import FTP

# FTP 서버 정보
ftp_host = " -- "  # 닷홈의 FTP 호스트
ftp_user = " -- "            # FTP 아이디
ftp_password = " -- "  # FTP 비밀번호

# 로컬 파일 경로 및 서버 업로드 경로
local_file = " -- "  # 업데이트할 파일 경로
remote_path = " -- "  # 서버에 저장될 경로

def upload_file():
    try:
        # FTP 연결
        with FTP(ftp_host) as ftp:
            ftp.login(ftp_user, ftp_password)
            print("FTP 서버에 연결되었습니다.")

            # 디렉토리 확인 및 생성
            try:
                ftp.cwd('/public_html')
            except Exception as e:
                print("디렉토리가 존재하지 않습니다. 생성 중...")
                ftp.mkd('/public_html')
                ftp.cwd('/public_html')

            # 파일 업로드
            with open(local_file, "rb") as file:
                ftp.storbinary(f"STOR {remote_path}", file)
                print(f"{local_file} 파일이 {remote_path}에 업로드되었습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    upload_file()