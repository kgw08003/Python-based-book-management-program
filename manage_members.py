import tkinter as tk
from tkinter import simpledialog, messagebox
import csv

MEMBERS_FILE = './csv/members.csv'

def center_window(window, width, height):
    # 윈도우의 중앙에 위치시키기 위한 함수
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

def addMember():
    def save_member():
        # 회원 정보를 CSV 파일에 추가하는 함수
        member_id = entry_member_id.get()
        name = entry_name.get()
        email = entry_email.get()

        with open(MEMBERS_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([member_id, name, email])

        messagebox.showinfo("정보", f"회원 '{name}'이(가) 추가되었습니다.")
        add_member_window.destroy()

    def go_back():
        # 뒤로가기 버튼 클릭 시 창 닫기
        add_member_window.destroy()

    # 회원 추가를 위한 새 창 생성
    add_member_window = tk.Toplevel()
    add_member_window.title("회원 추가")
    center_window(add_member_window, 400, 300)  # 창을 화면 중앙에 배치

    # 입력 필드와 레이블 생
    tk.Label(add_member_window, text="회원 ID").grid(row=0, column=0)
    entry_member_id = tk.Entry(add_member_window)
    entry_member_id.grid(row=0, column=1)

    tk.Label(add_member_window, text="이름").grid(row=1, column=0)
    entry_name = tk.Entry(add_member_window)
    entry_name.grid(row=1, column=1)

    tk.Label(add_member_window, text="이메일").grid(row=2, column=0)
    entry_email = tk.Entry(add_member_window)
    entry_email.grid(row=2, column=1)

    # 버튼 추가
    tk.Button(add_member_window, text="저장", command=save_member, width=8, height=1).grid(row=3, columnspan=2)
    tk.Button(add_member_window, text="뒤로가기", command=go_back, width=8, height=1).grid(row=4, columnspan=2)

def delMember():
    def go_back():
        # 뒤로가기 버튼 클릭 시 창 닫기
        del_member_window.destroy()

    # 삭제할 회원의 ID를 입력받아 삭제
    member_id_to_delete = simpledialog.askstring("회원 삭제", "삭제할 회원의 ID:")
    if member_id_to_delete:
        # 기존 회원 목록을 읽어와서 삭제할 ID를 가진 항목 제외
        with open(MEMBERS_FILE, 'r') as file:
            lines = list(csv.reader(file))

        with open(MEMBERS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            for line in lines:
                if line[0] != member_id_to_delete:
                    writer.writerow(line)

        messagebox.showinfo("정보", f"회원 ID '{member_id_to_delete}'이(가) 삭제되었습니다.")

     # 회원 삭제를 위한 새 창 생성
    del_member_window = tk.Toplevel()
    del_member_window.title("회원 삭제")
    center_window(del_member_window, 300, 200)   # 창을 화면 중앙에 배치

    tk.Button(del_member_window, text="뒤로가기", command=go_back).pack()

def searchMember():
    def search():
        # 검색 쿼리를 입력받아 회원 정보를 찾고 결과를 표시
        query = entry_query.get().lower()
        result_text.delete(1.0, tk.END)
        with open(MEMBERS_FILE, 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                selected_menu = menu_var.get()
                query_lower = query.lower()
                
                if selected_menu == "회원 ID":
                    if query in line[0]:
                        result_text.insert(tk.END, ','.join(line) + '\n')
                elif selected_menu == "이름":
                    if query_lower in line[1].lower():
                        result_text.insert(tk.END, ','.join(line) + '\n')
                elif selected_menu == "이메일":
                    if query_lower in line[2].lower():
                        result_text.insert(tk.END, ','.join(line) + '\n')


    def go_back():
        # 뒤로가기 버튼 클릭 시 창 닫기
        search_member_window.destroy()

     # 회원 검색을 위한 새 창 생성
    search_member_window = tk.Toplevel()
    search_member_window.title("회원 검색")
    center_window(search_member_window, 580, 350) # 창을 화면 중앙에 배

    # 검색 조건을 선택할 수 있는 드롭다운 메뉴와 검색 입력 필드
    menu_var = tk.StringVar(value="회원 ID")
    options = ["회원 ID", "이름", "이메일"]
    tk.OptionMenu(search_member_window, menu_var, *options).grid(row=0, column=0)
    entry_query = tk.Entry(search_member_window)
    entry_query.grid(row=0, column=1)
    tk.Button(search_member_window, text="검색", command=search).grid(row=0, column=2)

    # 검색 결과를 표시할 텍스트 영역
    result_text = tk.Text(search_member_window, width=80, height=20)
    result_text.grid(row=1, columnspan=3)

    tk.Button(search_member_window, text="뒤로가기", command=go_back).grid(row=2, columnspan=3)

def manageMembers(root):
    def go_back():
        # 뒤로가기 버튼 클릭 시 창 닫기
        manage_members_window.destroy()

    manage_members_window = tk.Toplevel(root)
    manage_members_window.title("회원 정보 관리")
    center_window(manage_members_window, 400, 300) # 창을 화면 중앙에 배치

    # 회원 추가, 삭제, 검색 버튼 추가
    tk.Button(manage_members_window, text="회원 추가", command=addMember).pack(pady=5)
    tk.Button(manage_members_window, text="회원 삭제", command=delMember).pack(pady=5)
    tk.Button(manage_members_window, text="회원 검색", command=searchMember).pack(pady=5)
    tk.Button(manage_members_window, text="뒤로가기", command=go_back).pack(pady=5)
