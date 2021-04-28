from tkinter import *
from tkinter import ttk , Frame
import sqlite3
import hashlib

def FormUser():

    def TampilData():
        global my_tree,entry_username,entry_password,idx
        style = ttk.Style()
        style.theme_use("default")
        # Configure our treview Color

        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white")
        # change selected color
        style.map('Treeview', background=[('selected', 'blue')])

        # Create Treview FRame
        tree_frame = Frame(master)
        tree_frame.pack(pady=10)
        # create treeview scrolbar
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y, )

        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
        # configure the scrollbar
        tree_scroll.config(command=my_tree.yview)

        # Define Our Columns
        my_tree['columns'] = ("No", "User", "Password")
        # Formate Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("No", anchor=W, width=50)
        my_tree.column("User", anchor=W, width=150)
        my_tree.column("Password", anchor=W, width=300)
        # Create Heading
        my_tree.heading('#0', text="", anchor=W)
        my_tree.heading('No', text="No", anchor=W)
        my_tree.heading('User', text="User", anchor=W)
        my_tree.heading('Password', text="Password", anchor=W)
        # Add Data
        # Create a database or connect to one
        conn = sqlite3.connect('database.db')

        # Create Cursor
        c = conn.cursor()

        # Query The Database
        c.execute("SELECT * FROM m_user")
        records = c.fetchall()

        #Create Striped row tags
        my_tree.tag_configure('oddrow',background="white")
        my_tree.tag_configure('evenrow',background="lightblue")
        global count
        count = 0
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, values=(record[0], record[1], record[2]),tags=('evenrow'))
            else:
                my_tree.insert(parent='', index='end', iid=count, values=(record[0], record[1], record[2]),tags=('oddrow'))


            count += 1

        # commit changes
        conn.commit


        # Close connection
        conn.close

        my_tree.pack(pady=10)

    #add record
    def add_record():
        # Create a database or connect to one
        conn = sqlite3.connect('database.db')

        # Create Cursor
        c = conn.cursor()

        # Insert Into Table

        c.execute(
            "INSERT INTO m_user (username, password) VALUES (:a, :b);",
            {'a': entry_username.get(),
             'b': hashlib.md5(entry_password.get().encode('utf-8')).hexdigest(),
             })

        # commit changes
        conn.commit()

        # Close connection
        conn.close()

        global count
        #Create Striped row tags
        my_tree.tag_configure('oddrow',background="white")
        my_tree.tag_configure('evenrow',background="lightblue")
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count,tags=('evenrow'), values=('', entry_username.get(),hashlib.md5(entry_password.get().encode('utf-8')).hexdigest()))
        else:
            my_tree.insert(parent='', index='end', iid=count,tags=('oddrow'), values=('',  entry_username.get(),hashlib.md5(entry_password.get().encode('utf-8')).hexdigest()))

        count += 1

        #clear box
        entry_username.delete(0,END)
        entry_password.delete(0,END)


    def remove_one():
        # Create a database or connect to one
        conn = sqlite3.connect('database.db')

        # Create Cursor
        c = conn.cursor()

        # Insert Into Table
        selected = my_tree.focus()
        #grab record values
        values = my_tree.item(selected,'values')

        c.execute(
            "delete from m_user where idx = :a",
            {'a': values[0]
             })

        print (
            "delete from m_user where idx = :a",
            {'a': values[0]
             })

        # commit changes
        conn.commit()

        # Close connection
        conn.close()

        x = my_tree.selection()[0]
        my_tree.delete(x)

    def select_record():
        entry_username.delete(0,END)
        entry_password.delete(0,END)
        #grab record number
        selected = my_tree.focus()
        #grab record values
        values = my_tree.item(selected,'values')
        #temp_label.config(text=values[0])
        #Output to entry boxes
        entry_username.insert(0,values[1])
        entry_password.insert(0,values[2])
        idx.config(text=values[0])


    def update_record():
        # Create a database or connect to one
        conn = sqlite3.connect('database.db')

        # Create Cursor
        c = conn.cursor()
        print (
            "update m_user set username = :a,password = :b where idx = :c",
            {'a': entry_username.get(),
             'b' : hashlib.md5(entry_password.get().encode('utf-8')).hexdigest(),
             'c' : idx.cget("text"),
             })

        c.execute(
            "update m_user set username = :a,password = :b where idx = :c",
            {'a': entry_username.get(),
             'b' : hashlib.md5(entry_password.get().encode('utf-8')).hexdigest(),
             'c' : idx.cget("text"),
             })

        # commit changes
        conn.commit()

        # Close connection
        conn.close()

        #GRab Record Number
        selected = my_tree.focus()
        #Save New Data
        my_tree.item(selected,text="",values=(idx.cget("text"),entry_username.get(),hashlib.md5(entry_password.get().encode('utf-8')).hexdigest()))

#===================== MAIN UNIT

    master =Toplevel()
    master.title('Master User')
    master.resizable(False, False)  # This code helps to disable windows from resizing
    master.iconbitmap('image/favicon.ico')
    window_height = 500
    window_width = 600

    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    master.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    TampilData()

    add_frame = LabelFrame(master)
    add_frame.pack(pady=10,padx=10,ipadx=10,anchor='c')

    nl = Label(add_frame,text="Username")
    nl.grid(row=0,column=0,sticky='w',pady=5,padx=5)

    il = Label(add_frame,text="Password")
    il.grid(row=1,column=0,sticky='w',pady=5,padx=5)


    nl2 = Label(add_frame,text=":")
    nl2.grid(row=0,column=1,sticky='w',pady=5,padx=5)

    il2 = Label(add_frame,text=":")
    il2.grid(row=1,column=1,sticky='w',pady=5,padx=5)

    #Entry Boxes
    entry_username =Entry(add_frame,width=50)
    entry_username.grid(row=0,column=2,columnspan="3",sticky='w',pady=5)

    entry_password = Entry(add_frame,width=50, show="*")
    entry_password.grid(row=1,column=2,columnspan="3",sticky='w',pady=5)

    #button
    add_record = Button(add_frame,text="Simpan Baru",command=add_record,width =12)
    add_record.grid(row=3,column=2, sticky='w',padx=5,pady=5)

    #Remove One
    remove_one = Button(add_frame,text="Hapus Data",command=remove_one,width=12)
    remove_one.grid(row=3,column=3,sticky='e',padx=5,pady=5)

    #update
    select_button = Button(add_frame,width=12,text="Pilih Data",command=select_record )
    select_button.grid(row=3,column=4,sticky='e',padx=5,pady=5)

    update_button = Button(add_frame,width=12,text="Simpan Update",command=update_record)
    update_button.grid(row=3,column=5,sticky='e',padx=5,pady=5)

    idx = Label(master, text='')
    idx.pack()