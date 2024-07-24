import tkinter as tk
from tkinter import simpledialog, messagebox
import csv

CATEGORIES_FILE = './csv/categories.csv'

def center_window(window, width, height):
    # 창을 화면 중앙에 배치하는 함수
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

def addCategory():
    def save_category():
        # 카테고리를 파일에 저장하는 함수
        category = entry_category.get()
        with open(CATEGORIES_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([category])
        messagebox.showinfo("정보", f"카테고리 '{category}'이(가) 추가되었습니다.")
        add_category_window.destroy()

    def go_back():
        # 뒤로가기 버튼 동작 정의
        add_category_window.destroy()

    # 카테고리 추가 창 생성
    add_category_window = tk.Toplevel()
    add_category_window.title("카테고리 추가")
    center_window(add_category_window, 225, 100)  # 카테고리 추가 창 크기 및 중앙 배치

    # 위젯 배치
    tk.Label(add_category_window, text="카테고리명").grid(row=0, column=0)
    entry_category = tk.Entry(add_category_window)
    entry_category.grid(row=0, column=1)

    tk.Button(add_category_window, text="저장", command=save_category).grid(row=1, columnspan=2)
    tk.Button(add_category_window, text="뒤로가기", command=go_back).grid(row=2, columnspan=2)

def delCategory():
    def go_back():
        # 뒤로가기 버튼 동작 정의
        del_category_window.destroy()

    # 삭제할 카테고리명 입력 받기
    category_to_delete = simpledialog.askstring("카테고리 삭제", "삭제할 카테고리명:")
    if category_to_delete:
        # 카테고리 파일에서 해당 카테고리를 삭제
        with open(CATEGORIES_FILE, 'r') as file:
            lines = list(csv.reader(file))

        with open(CATEGORIES_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            for line in lines:
                if line[0] != category_to_delete:
                    writer.writerow(line)

        messagebox.showinfo("정보", f"카테고리 '{category_to_delete}'이(가) 삭제되었습니다.")

    # 카테고리 삭제 창 생성
    del_category_window = tk.Toplevel()
    del_category_window.title("카테고리 삭제")
    center_window(del_category_window, 300, 200)  # 카테고리 삭제 창 크기 및 중앙 배치

    tk.Button(del_category_window, text="뒤로가기", command=go_back).pack()

def manageCategories():
    # 카테고리 관리 창 생성
    manage_categories_window = tk.Toplevel()
    manage_categories_window.title("카테고리 관리")
    center_window(manage_categories_window, 400, 300)  # 카테고리 관리 창 크기 및 중앙 배치

    # 위젯 배치
    tk.Button(manage_categories_window, text="카테고리 추가", command=addCategory).pack(pady=5)
    tk.Button(manage_categories_window, text="카테고리 삭제", command=delCategory).pack(pady=5)
    tk.Button(manage_categories_window, text="뒤로가기", command=manage_categories_window.destroy).pack(pady=5)
