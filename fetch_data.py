import serial  # 시리얼 통신 라이브러리
import csv
from datetime import datetime

# 시리얼 포트 설정 (보드에 맞게 수정)
SERIAL_PORT = '/dev/ttyUSB0'  # 예: COM3 (Windows) 또는 /dev/ttyUSB0 (Linux/Mac)
BAUD_RATE = 9600

# 데이터 수집 및 CSV 저장
def fetch_data_from_board():
    try:
        # 시리얼 통신 시작
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            print("보드로부터 데이터를 수신 중...")
            data_list = []

            # 데이터를 10초 동안 수신
            end_time = datetime.now().timestamp() + 10
            while datetime.now().timestamp() < end_time:
                if ser.in_waiting:
                    line = ser.readline().decode('utf-8').strip()
                    print(f"수신된 데이터: {line}")
                    date_str, count = line.split(',')  # 예: "2024-11-20,5"
                    data_list.append((date_str, int(count)))

            # CSV 파일 저장
            csv_file = './static/data/data.csv'
            with open(csv_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['date', 'count'])
                writer.writerows(data_list)
            print(f"데이터가 {csv_file}에 저장되었습니다.")

    except Exception as e:
        print(f"오류 발생: {e}")

# 실행
if __name__ == "__main__":
    fetch_data_from_board()