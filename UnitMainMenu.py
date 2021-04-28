# =========================== USES =============================================
from tkinter import messagebox,Tk,Menu,mainloop,Toplevel,Label,Entry,Button
from UnitInputID import FormInputID
from UnitPegawai import FormPegawai
from UnitUser import FormUser
from UnitKenalWajah import FormKenalWajah
from UnitDeteksiWajah import FormDeteksiWajah
# ============================ END USES ========================================
def FormMainMenu():
    # isi nama root
    root = Tk()
    # set windows auto size with window
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.iconbitmap('image/favicon.ico')
    root.title('Aplikasi Absensi Mengunakan Wajah')

    # membuat main menu
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label='System', menu=filemenu)
    filemenu.add_command(label='Exit', command=root.destroy)

    filemenu1 = Menu(menu)
    menu.add_cascade(label='Master', menu=filemenu1)
    filemenu1.add_command(label='User' , command=lambda:FormUser())
    filemenu1.add_command(label='Pegawai', command=lambda:FormPegawai())

    filemenu2 = Menu(menu)
    menu.add_cascade(label='Transaksi', menu=filemenu2)
    filemenu2.add_command(label='Ambil Data Wajah', command=lambda:FormInputID())
    filemenu2.add_command(label='Pelajari Wajah', command=lambda:FormKenalWajah())
    filemenu2.add_command(label='Deteksi Wajah', command=lambda:FormDeteksiWajah())

    helpmenu = Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About',command=lambda:messagebox.showinfo("Information", "Internal Software PT MUA"))
