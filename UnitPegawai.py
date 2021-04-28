from tkinter import *
from tkinter import ttk , Frame
import sqlite3


def FormPegawai():

    def TampilData():
        global my_tree,name_box,nohp_box,clicked,id_pegawai
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
        my_tree['columns'] = ("No", "Name", "No_HP", "Gender")
        # Formate Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("No", anchor=W, width=50)
        my_tree.column("Name", anchor=W, width=250)
        my_tree.column("No_HP", anchor=CENTER, width=150)
        my_tree.column("Gender", anchor=W, width=75)
        # Create Heading
        my_tree.heading('#0', text="", anchor=W)
        my_tree.heading('No', text="No", anchor=W)
        my_tree.heading('Name', text="Name", anchor=W)
        my_tree.heading('No_HP', text="No HP", anchor=CENTER)
        my_tree.heading('Gender', text="Gender", anchor=W)
        # Add Data
        # Create a database or connect to one
        conn = sqlite3.connect('database.db')

        # Create Cursor
        c = conn.cursor()

        # Query The Database
        c.execute("SELECT * FROM m_pegawai")
        records = c.fetchall()

        #Create Striped row tags
        my_tree.tag_configure('oddrow',background="white")
        my_tree.tag_configure('evenrow',background="lightblue")
        global count
        count = 0
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, values=(record[0], record[1], record[2], record[3]),tags=('evenrow'))
            else:
                my_tree.insert(parent='', index='end', iid=count, values=(record[0], record[1], record[2], record[3]),tags=('oddrow'))


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
            "INSERT INTO m_pegawai (nama_pegawai, no_hp, jenis_kelamin) VALUES (:a, :b, :c);",
            {'a': name_box.get(),
             'b': nohp_box.get(),
             'c': clicked.get(),
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
            my_tree.insert(parent='', index='end', iid=count,tags=('evenrow'), values=('', name_box.get(), nohp_box.get(), clicked.get()))
        else:
            my_tree.insert(parent='', index='end', iid=count,tags=('oddrow'), values=('', name_box.get(), nohp_box.get(), clicked.get()))

        count += 1

        #clear box
        name_box.delete(0,END)
        nohp_box.delete(0,END)


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
            "delete from m_pegawai where id_pegawai = :a",
            {'a': values[0]
             })

        print (
            "delete from m_pegawai where id_pegawai = :a",
            {'a': values[0]
             })

        # commit changes
        conn.commit()

        # Close connection
        conn.close()

        x = my_tree.selection()[0]
        my_tree.delete(x)

    def select_record():
        name_box.delete(0,END)
        nohp_box.delete(0,END)
        #grab record number
        selected = my_tree.focus()
        #grab record values
        values = my_tree.item(selected,'values')
        #temp_label.config(text=values[0])
        #Output to entry boxes
        name_box.insert(0,values[1])
        nohp_box.insert(0,values[2])
        id_pegawai.config(text=values[0])


    def update_record():
        # Create a database or connect to one
        conn = sqlite3.connect('database.db')

        # Create Cursor
        c = conn.cursor()
        print (
            "update m_pegawai set nama_pegawai = :a,no_hp = :b,jenis_kelamin=:c where id_pegawai = :d",
            {'a': name_box.get(),
             'b' : nohp_box.get(),
             'c' : clicked.get(),
             'd' : id_pegawai.cget("text"),
             })

        c.execute(
            "update m_pegawai set nama_pegawai = :a,no_hp = :b,jenis_kelamin=:c where id_pegawai = :d;",
            {'a': name_box.get(),
             'b' : nohp_box.get(),
             'c' : clicked.get(),
             'd' : id_pegawai.cget("text"),
             })

        # commit changes
        conn.commit()

        # Close connection
        conn.close()

        #GRab Record Number
        selected = my_tree.focus()
        #Save New Data
        my_tree.item(selected,text="",values=(id_pegawai.cget("text"),name_box.get(),nohp_box.get(),clicked.get()))

#===================== MAIN UNIT

    master =Toplevel()
    master.title('Master Pegawai')
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

    nl = Label(add_frame,text="Name")
    nl.grid(row=0,column=0,sticky='w',pady=5,padx=5)

    il = Label(add_frame,text="No HP")
    il.grid(row=1,column=0,sticky='w',pady=5,padx=5)

    tl = Label(add_frame,text="Jenis Kelamin")
    tl.grid(row=2,column=0,sticky='w',pady=5,padx=5)

    nl2 = Label(add_frame,text=":")
    nl2.grid(row=0,column=1,sticky='w',pady=5,padx=5)

    il2 = Label(add_frame,text=":")
    il2.grid(row=1,column=1,sticky='w',pady=5,padx=5)

    tl2 = Label(add_frame,text=":",)
    tl2.grid(row=2,column=1,sticky='w',pady=5,padx=5)
    #Entry Boxes
    name_box =Entry(add_frame,width=50)
    name_box.grid(row=0,column=2,columnspan="3",sticky='w',pady=5)

    nohp_box = Entry(add_frame,width=30)
    nohp_box.grid(row=1,column=2,columnspan="3",sticky='w',pady=5)

    clicked = StringVar()
    clicked.set("L")
    options = [
        "L",
        "P"
    ]
    gender_box = OptionMenu(add_frame, clicked, *options)
    gender_box.grid(row=2,column=2,columnspan="3",sticky='w',pady=5)

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

    id_pegawai = Label(master, text='')
    id_pegawai.pack()