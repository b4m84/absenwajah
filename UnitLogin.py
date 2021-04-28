# =========================== USES =============================================
from tkinter import messagebox,Tk,Menu,mainloop,Toplevel,Label,Entry,Button
from PIL import Image,ImageTk
import sqlite3
import hashlib
from UnitMainMenu import FormMainMenu

# ============================ END USES ========================================

def FormLogin():
    def proses(a,b):
        try:
            print (entry_username.get())
            sqliteConnection = sqlite3.connect('database.db')
            cursor = sqliteConnection.cursor()

            sqlite_select_query = """SELECT * from m_user where username = ? and password=?"""
            cursor.execute(sqlite_select_query,(a,b,))
            print (sqlite_select_query + a + b)
            records = cursor.fetchall()
            for row in records:
                print(row[0])

            if len(records) > 0:
                messagebox.showinfo("Information", "Login Sukses")
                master.destroy()
                FormMainMenu()
            else:
                messagebox.showinfo("Information", "Login Gagal ")
                entry_username.insert(0,'')
                entry_password.insert(0,'')
                entry_username.focus

            cursor.close()
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

    global img_login,root

    master=Tk()
    master.title('Login Page')
    master.resizable(False, False)  # This code helps to disable windows from resizing
    master.iconbitmap('image/favicon.ico')

    window_height = 450
    window_width = 440

    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    master.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    master.focus

    # creating label widget
    img_login = ImageTk.PhotoImage(Image.open("image/login.png"))
    label_img_login = Label(master,image=img_login,width=400,height=320)
    label_username = Label(master, text="Username   :" ,anchor='w')
    label_password = Label(master, text="Password   :", anchor='w')
    entry_username = Entry(master,width=40)
    entry_password = Entry(master,width=40, show="*")
    button_submit = Button(master, text="Login",padx=30, command=lambda:proses(entry_username.get(),hashlib.md5(entry_password.get().encode('utf-8')).hexdigest()))
    button_reset = Button(master, text="Batal",padx=30, command=master.destroy)

    # Showing it into screen
    entry_username.focus
    label_img_login.grid(row=0,column=0,sticky='w',columnspan=3,padx=20)
    label_username.grid(row=1, column=0,padx=10)
    label_password.grid(row=2, column=0,padx=10)
    entry_username.grid(row=1, column=1,columnspan=2,sticky='w',pady=10)
    entry_password.grid(row=2,column=1,columnspan=2,sticky='w',pady=10)
    button_submit.grid(row=3, column=1,sticky='w')
    button_reset.grid(row=3,column=2,sticky='w')