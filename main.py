import tkinter as tk
import manage_books
import manage_members
import manage_borrow_records

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

def open_books():
    manage_books.manageBooks(root)

def open_members():
    manage_members.manageMembers(root)

def open_borrow_records():
    manage_borrow_records.manageBorrowRecords(root)

def main():
    global root
    root = tk.Tk()
    root.title("도서관리 프로그램 ver. 0.2.0")
    center_window(root, 600, 400)  # 메인 사이즈

    tk.Label(root, text="도서관리 프로그램 ver. 0.2.0", font=("Arial", 24)).pack(pady=10)
    # 버튼 추가
    tk.Button(root, text="도서정보 관리", command=open_books, width=30, height=3).pack(pady=10)
    tk.Button(root, text="회원 정보 관리", command=open_members, width=30, height=3).pack(pady=10)
    tk.Button(root, text="대출 기록 관리", command=open_borrow_records, width=30, height=3).pack(pady=10)
    tk.Button(root, text="종료", command=root.quit, width=30, height=3).pack(pady=10)

    root.mainloop()

if __name__ == '__main__':
    main()
