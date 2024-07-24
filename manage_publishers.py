import tkinter as tk
from tkinter import simpledialog, messagebox
import csv

PUBLISHERS_FILE = './csv/publishers.csv'

def center_window(window, width, height):
    #주어진 Tkinter 창을 화면의 중앙에 배치
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

def addPublisher():
    # 출판사 이름을 입력받아 CSV 파일에 추가하는 함수
    publisher_name = simpledialog.askstring("출판사 추가", "출판사 이름:")
    if publisher_name:
        # 출판사 이름을 CSV 파일에 추가
        with open(PUBLISHERS_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([publisher_name])
        # 성공 메시지 표시
        messagebox.showinfo("정보", f"출판사 '{publisher_name}'이(가) 추가되었습니다.")

def delPublisher():
    # 삭제할 출판사 이름을 입력받아 CSV 파일에서 제거하는 함수
    publisher_name = simpledialog.askstring("출판사 삭제", "삭제할 출판사 이름:")
    if publisher_name:
        # 기존 출판사 목록을 읽어와서 삭제할 출판사를 제외
        with open(PUBLISHERS_FILE, 'r') as file:
            lines = list(csv.reader(file))

        with open(PUBLISHERS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            for line in lines:
                if line[0] != publisher_name:
                    writer.writerow(line)

        # 성공 메시지 표시
        messagebox.showinfo("정보", f"출판사 '{publisher_name}'이(가) 삭제되었습니다.")

def managePublishers():
    # 출판사 관리 기능을 제공하는 새 창 생성
    manage_publishers_window = tk.Toplevel()
    manage_publishers_window.title("출판사 관리")
    center_window(manage_publishers_window, 400, 300)  # 창 크기 및 중앙 배치

    # 출판사 추가 버튼
    tk.Button(manage_publishers_window, text="출판사 추가", command=addPublisher).pack(pady=5)
    # 출판사 삭제 버튼
    tk.Button(manage_publishers_window, text="출판사 삭제", command=delPublisher).pack(pady=5)
    # 뒤로가기 버튼
    tk.Button(manage_publishers_window, text="뒤로가기", command=manage_publishers_window.destroy).pack(pady=5)
