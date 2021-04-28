from tkinter import messagebox,Tk,Menu,mainloop,Toplevel,Label,Entry,Button
from UnitDaftarWajah import FormDaftarWajah

# function buka window input id pegawai
def FormInputID():
    def submit_fields():
        FormDaftarWajah(entry1.get())
        master.destroy


    master=Toplevel()
    master.title('Masukkan ID Pegawai')
    master.resizable(False, False)  # This code helps to disable windows from resizing
    master.iconbitmap('image/favicon.ico')

    window_height = 100
    window_width = 300

    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    master.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    Label(master, text="ID Pegawai").grid(row=0)
    entry1 = Entry(master)
    entry1.grid(row=0, column=1)
    Button(master, text='Quit', command=master.destroy,width=10).grid(row=3, column=0,padx=20, pady=4)
    Button(master, text='Submit', command=submit_fields,width=10).grid(row=3, column=1,padx=20, pady=4)
