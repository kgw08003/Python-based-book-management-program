import tkinter as tk
from tkinter import simpledialog, messagebox
import csv

BORROW_RECORDS_FILE = './csv/borrow_records.csv'

def center_window(window, width, height):
     # 윈도우의 중앙에 위치시키기 위한 함수
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

def addBorrowRecord():
    def save_record():
        # 대출 기록을 CSV 파일에 추가하는 함수
        isbn = entry_isbn.get()
        member_id = entry_member_id.get()
        borrow_date = entry_borrow_date.get()
        return_date = entry_return_date.get()

        with open(BORROW_RECORDS_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([isbn, member_id, borrow_date, return_date])

        messagebox.showinfo("정보", "대출 기록이 추가되었습니다.")
        add_record_window.destroy()

    def go_back():
        # 뒤로가기 버튼 클릭 시 창 닫기
        add_record_window.destroy()

    # 대출 기록 추가를 위한 새 창 생성
    add_record_window = tk.Toplevel()
    add_record_window.title("대출 기록 추가")
    center_window(add_record_window, 200, 150)  # 창을 화면 중앙에 배치

    # 입력 필드와 레이블 생성
    tk.Label(add_record_window, text="ISBN").grid(row=0, column=0)
    entry_isbn = tk.Entry(add_record_window)
    entry_isbn.grid(row=0, column=1)

    tk.Label(add_record_window, text="회원 ID").grid(row=1, column=0)
    entry_member_id = tk.Entry(add_record_window)
    entry_member_id.grid(row=1, column=1)

    tk.Label(add_record_window, text="대출일").grid(row=2, column=0)
    entry_borrow_date = tk.Entry(add_record_window)
    entry_borrow_date.grid(row=2, column=1)

    tk.Label(add_record_window, text="반납일").grid(row=3, column=0)
    entry_return_date = tk.Entry(add_record_window)
    entry_return_date.grid(row=3, column=1)

    # 버튼 추가
    tk.Button(add_record_window, text="저장", command=save_record, width=8, height=1).grid(row=4, columnspan=2)
    tk.Button(add_record_window, text="뒤로가기", command=go_back, width=8, height=1).grid(row=5, columnspan=2)

def delBorrowRecord():
    def go_back():
        # 뒤로가기 버튼 클릭 시 창 닫기
        del_record_window.destroy()

    # 삭제할 대출 기록의 ISBN을 입력받아 삭제
    isbn_to_delete = simpledialog.askstring("대출 기록 삭제", "삭제할 대출 기록의 ISBN:")
    if isbn_to_delete:
        # 기존 대출 기록을 읽어와서 삭제할 ISBN을 가진 항목 제외
        with open(BORROW_RECORDS_FILE, 'r') as file:
            lines = list(csv.reader(file))

        with open(BORROW_RECORDS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            for line in lines:
                if line[0] != isbn_to_delete:
                    writer.writerow(line)

        messagebox.showinfo("정보", f"대출 기록 ISBN '{isbn_to_delete}'이(가) 삭제되었습니다.")
    
    # 대출 기록 삭제를 위한 새 창 생성
    del_record_window = tk.Toplevel()
    del_record_window.title("대출 기록 삭제")
    center_window(del_record_window, 300, 200) # 창을 화면 중앙에 배치

    tk.Button(del_record_window, text="뒤로가기", command=go_back).pack()

def searchBorrowRecord():
    def search():
        # 검색 쿼리를 입력받아 대출 기록을 찾고 결과를 표시
        query = entry_query.get().lower()
        result_text.delete(1.0, tk.END)
        with open(BORROW_RECORDS_FILE, 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                if menu_var.get() == "ISBN" and query in line[0]:
                    result_text.insert(tk.END, ','.join(line) + '\n')
                elif menu_var.get() == "회원 ID" and query in line[1]:
                    result_text.insert(tk.END, ','.join(line) + '\n')
                elif menu_var.get() == "대출일" and query in line[2]:
                    result_text.insert(tk.END, ','.join(line) + '\n')
                elif menu_var.get() == "반납일" and query in line[3]:
                    result_text.insert(tk.END, ','.join(line) + '\n')

    def go_back():
        # 뒤로가기 버튼 클릭 시 창 닫기
        search_record_window.destroy()

    # 대출 기록 검색을 위한 새 창 생성
    search_record_window = tk.Toplevel()
    search_record_window.title("대출 기록 검색")
    center_window(search_record_window, 580, 350)  # 창을 화면 중앙에 배치

    # 검색 조건을 선택할 수 있는 드롭다운 메뉴와 검색 입력 필드
    menu_var = tk.StringVar(value="ISBN")
    options = ["ISBN", "회원 ID", "대출일", "반납일"]
    tk.OptionMenu(search_record_window, menu_var, *options).grid(row=0, column=0)
    entry_query = tk.Entry(search_record_window)
    entry_query.grid(row=0, column=1)
    tk.Button(search_record_window, text="검색", command=search).grid(row=0, column=2)

     # 검색 결과를 표시할 텍스트 영역
    result_text = tk.Text(search_record_window, width=80, height=20)
    result_text.grid(row=1, columnspan=3)

    tk.Button(search_record_window, text="뒤로가기", command=go_back).grid(row=2, columnspan=3)

def manageBorrowRecords(root):
    def go_back():
        # 뒤로가기 버튼 클릭 시 창 닫기
        manage_borrow_records_window.destroy()

    # 대출 기록 관리 기능을 제공하는 새 창 생성
    manage_borrow_records_window = tk.Toplevel(root)
    manage_borrow_records_window.title("대출 기록 관리")
    center_window(manage_borrow_records_window, 400, 300) # 창을 화면 중앙에 배치

     # 대출 기록 추가, 삭제, 검색 버튼
    tk.Button(manage_borrow_records_window, text="대출 기록 추가", command=addBorrowRecord).pack(pady=5)
    tk.Button(manage_borrow_records_window, text="대출 기록 삭제", command=delBorrowRecord).pack(pady=5)
    tk.Button(manage_borrow_records_window, text="대출 기록 검색", command=searchBorrowRecord).pack(pady=5)
    tk.Button(manage_borrow_records_window, text="뒤로가기", command=go_back).pack(pady=5)
