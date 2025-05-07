import csv
import matplotlib.pyplot as plt
import os
import calendar
from collections import defaultdict
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from datetime import datetime

# CSV 파일 경로
updata_file = r" -- " # 개인 지정
data_file = r" -- " # 개인 지정

# 그래프 저장 경로
output_dir = r" -- " # 개인 지정
output_file = os.path.join(output_dir, "monthly_trash_chart.png")

# 출력 디렉토리 확인
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"출력 디렉토리를 생성했습니다: {output_dir}")

# 데이터 CSV 초기 설정
if not os.path.exists(data_file):
    with open(data_file, 'w') as f:
        f.write("날짜,상태\n")
    print(f"데이터 파일이 생성되었습니다: {data_file}")

# updata.csv에서 데이터를 읽어 data.csv에 추가하는 함수
def update_data():
    if os.path.exists(updata_file):
        with open(updata_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # 헤더 건너뛰기

            with open(data_file, 'a') as data:
                writer = csv.writer(data)
                for row in reader:
                    if row[1].strip().lower() == "on":
                        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        writer.writerow([current_time, 'on'])
                        print(f"새로운 데이터 추가: {current_time}, on")

# data.csv 파일을 읽고 일별 및 월별 데이터를 추출하는 함수
def read_data():
    daily_data = defaultdict(int)
    monthly_data = defaultdict(int)

    with open(data_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            date, count = row
            year, month, day = map(int, date.split('-')[:3])
            daily_data[(year, month, day)] += 1
            monthly_data[month] += 1

    return daily_data, monthly_data

# 그래프 생성 함수
def generate_graph(monthly_data):
    months = range(1, 13)
    counts = [monthly_data[month] for month in months]

    plt.bar(months, counts, color='skyblue')
    plt.title('Monthly Trash Count')
    plt.xlabel('Month')
    plt.ylabel('Trash Count')
    plt.xticks(months)

    plt.savefig(output_file)
    print(f"그래프가 저장되었습니다: {output_file}")
    plt.show()

# 캘린더 출력 함수
def print_calendar(year, month, daily_data):
    print(f"\n{year}년 {month}월")
    print(calendar.month(year, month))

    cal = calendar.monthcalendar(year, month)
    print("쓰레기 버린 횟수 캘린더")
    for week in cal:
        week_with_data = [
            f"{day}({daily_data.get((year, month, day), 0)})" if day != 0 else "   "
            for day in week
        ]
        print(" ".join(week_with_data))

# 파일 변경 감지 핸들러
class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == updata_file:
            print(f"{updata_file} 파일이 변경되었습니다. 데이터를 갱신합니다.")
            update_data()
            daily_data, monthly_data = read_data()

            for month in range(1, 13):
                print_calendar(2024, month, daily_data)

            generate_graph(monthly_data)

# 파일 변경 감지 설정
event_handler = FileChangeHandler()
observer = Observer()
observer.schedule(event_handler, path=os.path.dirname(updata_file), recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)  # 파일 변경 감지를 계속 실행
except KeyboardInterrupt:
    print("프로그램을 종료합니다.")
    observer.stop()

observer.join()