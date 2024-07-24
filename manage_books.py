import tkinter as tk
from tkinter import simpledialog, messagebox
import csv
import manage_categories
import manage_publishers

BOOKS_FILE = './csv/books.csv'

def center_window(window, width, height):
    # 윈도우의 중앙에 위치시키기 위한 함수
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

def addBook():
    def save_book():
        # 책 정보를 CSV 파일에 추가하는 함수
        title = entry_title.get()
        author = entry_author.get()
        publisher = entry_publisher.get()
        isbn = entry_isbn.get()
        year = entry_year.get()
        category = entry_category.get()

        with open(BOOKS_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([isbn, title, author, publisher, year, category])

        messagebox.showinfo("정보", f"도서 '{title}'이(가) 추가되었습니다.")
        add_book_window.destroy()

    def go_back():
        # 뒤로가기 버튼 클릭 시 창 닫기
        add_book_window.destroy()

    # 책 추가를 위한 새 창 생성
    add_book_window = tk.Toplevel()
    add_book_window.title("도서 추가")
    center_window(add_book_window, 210, 200) # 창을 화면 중앙에 배치

    # 입력 필드와 레이블 생성
    tk.Label(add_book_window, text="도서명").grid(row=0, column=0)
    entry_title = tk.Entry(add_book_window)
    entry_title.grid(row=0, column=1)

    tk.Label(add_book_window, text="저자명").grid(row=1, column=0)
    entry_author = tk.Entry(add_book_window)
    entry_author.grid(row=1, column=1)

    tk.Label(add_book_window, text="출판사").grid(row=2, column=0)
    entry_publisher = tk.Entry(add_book_window)
    entry_publisher.grid(row=2, column=1)

    tk.Label(add_book_window, text="ISBN").grid(row=3, column=0)
    entry_isbn = tk.Entry(add_book_window)
    entry_isbn.grid(row=3, column=1)

    tk.Label(add_book_window, text="발행년도").grid(row=4, column=0)
    entry_year = tk.Entry(add_book_window)
    entry_year.grid(row=4, column=1)

    tk.Label(add_book_window, text="카테고리").grid(row=5, column=0)
    entry_category = tk.Entry(add_book_window)
    entry_category.grid(row=5, column=1)

    # 버튼 추가
    tk.Button(add_book_window, text="저장", command=save_book, width=8, height=1).grid(row=6, columnspan=2)
    tk.Button(add_book_window, text="뒤로가기", command=go_back, width=8, height=1).grid(row=7, columnspan=2)

def delBook():
    def go_back():
        # 뒤로가기 버튼 클릭 시 창 닫기
        del_book_window.destroy()

    # 삭제할 책의 ISBN을 입력받아 삭제
    isbn_to_delete = simpledialog.askstring("도서 삭제", "삭제할 도서의 ISBN:")
    if isbn_to_delete:
        # 기존 책 목록을 읽어와서 삭제할 ISBN을 가진 항목 제외
        with open(BOOKS_FILE, 'r') as file:
            lines = list(csv.reader(file))

        with open(BOOKS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            for line in lines:
                if line[0] != isbn_to_delete:
                    writer.writerow(line)

        messagebox.showinfo("정보", f"도서 ISBN '{isbn_to_delete}'이(가) 삭제되었습니다.")

     # 책 삭제를 위한 새 창 생성
    del_book_window = tk.Toplevel()
    del_book_window.title("도서 삭제")
    center_window(del_book_window, 300, 200) # 창을 화면 중앙에 배치

    tk.Button(del_book_window, text="뒤로가기", command=go_back).pack()

def searchBook():
    def search():
        # 검색 쿼리를 입력받아 책 정보를 찾고 결과를 표시
        query = entry_query.get().lower()
        result_text.delete(1.0, tk.END)
        with open(BOOKS_FILE, 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                selected_menu = menu_var.get()
                query_lower = query.lower()
                
                if selected_menu == "도서명":
                    if query_lower in line[1].lower():
                        result_text.insert(tk.END, ','.join(line) + '\n')
                elif selected_menu == "저자명":
                    if query_lower in line[2].lower():
                        result_text.insert(tk.END, ','.join(line) + '\n')
                elif selected_menu == "출판사":
                    if query_lower in line[3].lower():
                        result_text.insert(tk.END, ','.join(line) + '\n')
                elif selected_menu == "ISBN":
                    if query in line[0]:
                        result_text.insert(tk.END, ','.join(line) + '\n')
                elif selected_menu == "발행년도":
                    if query in line[4]:
                        result_text.insert(tk.END, ','.join(line) + '\n')
                elif selected_menu == "카테고리":
                    if query_lower in line[5].lower():
                        result_text.insert(tk.END, ','.join(line) + '\n')

    def go_back():
        # 뒤로가기 버튼 클릭 시 창 닫기
        search_book_window.destroy()

     # 책 검색을 위한 새 창 생성
    search_book_window = tk.Toplevel()
    search_book_window.title("도서 검색")
    center_window(search_book_window, 580, 350)  # 창을 화면 중앙에 배치

    # 검색 조건을 선택할 수 있는 드롭다운 메뉴와 검색 입력 필드
    menu_var = tk.StringVar(value="도서명")
    options = ["도서명", "저자명", "출판사", "ISBN", "발행년도", "카테고리"]
    tk.OptionMenu(search_book_window, menu_var, *options).grid(row=0, column=0)
    entry_query = tk.Entry(search_book_window)
    entry_query.grid(row=0, column=1)
    tk.Button(search_book_window, text="검색", command=search).grid(row=0, column=2)

    # 검색 결과를 표시할 텍스트 영역
    result_text = tk.Text(search_book_window, width=80, height=20)
    result_text.grid(row=1, columnspan=3)

    tk.Button(search_book_window, text="뒤로가기", command=go_back).grid(row=2, columnspan=3)

def manageBooks(root):
    def go_back():
        # 뒤로가기 버튼 클릭 시 창 닫기
        manage_books_window.destroy()

    # 책 관리 기능을 제공하는 새 창 생성
    manage_books_window = tk.Toplevel(root)
    manage_books_window.title("도서정보 관리")
    center_window(manage_books_window, 400, 300)  # 창을 화면 중앙에 배치

    # 책 추가, 삭제, 검색 버튼 추가
    tk.Button(manage_books_window, text="도서 추가", command=addBook).pack(pady=5)
    tk.Button(manage_books_window, text="도서 삭제", command=delBook).pack(pady=5)
    tk.Button(manage_books_window, text="도서 검색", command=searchBook).pack(pady=5)
    tk.Button(manage_books_window, text="카테고리 관리", command=manage_categories.manageCategories).pack(pady=5)
    tk.Button(manage_books_window, text="출판사 관리", command=manage_publishers.managePublishers).pack(pady=5)
    tk.Button(manage_books_window, text="뒤로가기", command=go_back).pack(pady=5)
