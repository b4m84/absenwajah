from tkinter import *
from tkinter import ttk

root =Tk()
root.title('Codemy.Com')
root.title('Codemy.Com -- TREE view')
root.geometry("500x600")

my_tree = ttk.Treeview(root)
#Define Our Columns
my_tree['columns'] = ("Name","ID","Favorite Pizza")
#Formate Our Columns
my_tree.column("#0",width=120,minwidth=25)
my_tree.column("Name",anchor=W,width=120)
my_tree.column("ID",anchor=CENTER,width=80)
my_tree.column("Favorite Pizza",anchor=W,width=140)
#Create Heading
my_tree.heading('#0',text="Label",anchor=W)
my_tree.heading('Name',text="Name",anchor=W)
my_tree.heading('ID',text="ID",anchor=CENTER)
my_tree.heading('Favorite Pizza',text="Favorite Pizza",anchor=W)
#Add Data
data = [
    ["John",1,"Pepperoni"],
    ["John",2, "Pepperoni"],
    ["John",3, "Pepperoni"],
    ["John",4, "Pepperoni"],
    ["John",5,"Pepperoni"],
]
global count
count=0
for record in data:
    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]))
    count += 1
'''
my_tree.insert(parent='', index='end',iid=0,text="Parent",values=('John',1,'Papperoni'))
my_tree.insert(parent='', index='end',iid=1,text="Parent",values=('John',2,'Papperoni'))
my_tree.insert(parent='', index='end',iid=2,text="Parent",values=('John',3,'Papperoni'))
my_tree.insert(parent='', index='end',iid=3,text="Parent",values=('John',4,'Papperoni'))
my_tree.insert(parent='', index='end',iid=4,text="Parent",values=('John',5,'Papperoni'))
my_tree.insert(parent='', index='end',iid=5,text="Parent",values=('John',6,'Papperoni'))
#add child
my_tree.insert(parent='' , index='end',iid=6,text="Child",values=('6','John','Papperoni'))
my_tree.move('6','0','0')
'''
my_tree.pack(pady=20)

add_frame = Frame(root)
add_frame.pack(pady=20)

nl = Label(add_frame,text="Name")
nl.grid(row=0,column=0)

il = Label(add_frame,text="ID")
il.grid(row=0,column=1)

tl = Label(add_frame,text="Toping")
tl.grid(row=0,column=2)

#Entry Boxes
name_box =Entry(add_frame)
name_box.grid(row=1,column=0)

id_box = Entry(add_frame)
id_box.grid(row=1,column=1)

topping_box = Entry(add_frame)
topping_box.grid(row=1,column=2)

#add record
def add_record():
    global count
    my_tree.insert(parent='',index='end',iid=count,text='',values=(name_box.get(),id_box.get(),topping_box.get()))
    count += 1
    #clear box
    name_box.delete(0,END)
    id_box.delete(0,END)
    topping_box.delete(0,END)

def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)

def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)

def remove_many():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)


#button
add_record = Button(root,text="Add Record",command=add_record)
add_record.pack(pady=20)

#Remove All
remove_all = Button(root, text="Remove All",command=remove_all)
remove_all.pack(pady=10)

#Remove One
remove_one = Button(root,text="Remove One Selected",command=remove_one)
remove_one.pack(pady=10)

#Remove Many Selected
remove_many=Button(root,text="Remove Many",command=remove_many)
remove_many.pack(pady=10)
root.mainloop()