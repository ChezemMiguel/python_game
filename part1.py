from tkinter import *
from tkinter import ttk


class Student:
    def __init__(self, root):
        self.root=root
        self.root.title("student management system")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="stmm", font="Algerian", bg="blue", fg="white")
        title.pack(side=TOP, fill=X)

# ==========manage frame==============

        Manage_Frame=Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=20, y=1000, width=450, height=580)

        m_title=Label(Manage_Frame, text="Manage frame", bg=("crimson"), fg="white", font=("times new roman", 15))
        m_title.grid(row=0, column=2, pady=20)

        lb1_roll = Label(Manage_Frame, text="Roll No", bg=("crimson"), fg="white", font=("calibri"))
        lb1_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Roll = Entry(Manage_Frame, bd=5, relief=GROOVE, font=("bold", 15, "times new roman"))
        txt_Roll.grid(row=1, column=1, pady=20, sticky="w")

        lb1_name = Label(Manage_Frame, text="Name ", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lb1_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_Frame, bd=5, relief=GROOVE, font=("bold", 15, "times new roman"))
        txt_name.grid(row=2, column=1, pady=20, sticky="w")

        txt_Email = Entry(Manage_Frame, bd=5, relief=GROOVE, font=("bold", 15, "times new roman"))
        txt_Email.grid(row=3, column=1, pady=20, padx=10, sticky="w")

        lb1_Email = Label(Manage_Frame, text="Gender", bg=("crimson"), fg="white", font=("times new roman", 20, "bold"))
        lb1_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        lb1_gender = Label(Manage_Frame, text="Gender", bg=("crimson"), fg="white", font=("times new roman", 20, "bold"))
        lb1_gender.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame, font=("times new roman", 20, "bold"), state='readonly')
        combo_gender["values"] = ("male", "female", "other")
        combo_gender.grid(row=4, column=1, padx=20, pady=10)

        lb1_contact = Label(Manage_Frame, text="Contact", bg=("crimson"), fg="white", font=("times new roman", 20, "bold"))
        lb1_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_contact = Entry(Manage_Frame, bd=5, relief=GROOVE, font=("bold", 15, "times new roman"))
        txt_contact.grid(row=5, column=1, pady=20, padx=10, sticky="w")

        lb1_Dob = Label(Manage_Frame, text="D.o.b", bg=("crimson"), fg="white", font=("times new roman", 20, "bold"))
        lb1_Dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_Dob = Entry(Manage_Frame, bd=5, relief=GROOVE, font=("bold", 15, "times new roman"))
        txt_Dob.grid(row=6, column=1, pady=20, padx=10, sticky="w")

        lb1_Address = Label(Manage_Frame, text="Address", bg=("crimson"), fg="white", font=("times new roman", 20, "bold"))
        lb1_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_Address = Entry(Manage_Frame, width=30, height=4, font=(" ", 10))
        txt_Address.grid(row=7, column=1, pady=20, padx=10, sticky="w")

#==========Button Frame========
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=10, y=500, width=580)

        Addbtn=Button(btn_Frame, text="Add", width=10)
        Addbtn.grid(row=0, column=0, padx=10, pady=10)
        updatebtn = Button(btn_Frame, text="update", width=10)
        updatebtn.grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_Frame, text="delete", width=10)
        deletebtn.grid(row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(btn_Frame, text="Clear", width=10)
        Clearbtn.grid(row=0, column=3, padx=10, pady=10)


#==========detail frame==============

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=800, height=580)

        lb1_search = Label(Detail_Frame, text="Search by", bg=("crimson"), fg="white", font=("times new roman", 20, "bold"))
        lb1_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, width=10, font=("times new roman", 13, "bold"), state='readonly')
        combo_search["values"] = ("Roll", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(Detail_Frame, width=20, bd=5, relief=GROOVE, font=("bold", 15, "times new roman"))
        txt_search.grid(row=0, column=7, pady=20, padx=10, sticky="w")

        searchbtn = Button(Detail_Frame, text="search", width=10, pady=5)
        searchbtn.grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="showall", width=10, pady=5)
        showallbtn.grid(row=0, column=4, padx=10, pady=10)

#=======Table Frame=============
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        Detail_Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=800, height=580)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        Student_table = ttk.Treeview(Table_Frame, columns=("Roll", "Name", "Email", "Gender", "Contact", "Dob", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)
        Student_table.heading("Roll", text="Roll No")
        Student_table.heading("Name", text="Name")
        Student_table.heading("Email", text="Email")
        Student_table.heading("Gender", text="Gender")
        Student_table.heading("Contact", text="Contact")
        Student_table.heading("Dob", text="D.o.b")
        Student_table.heading("Address", text="Address")
        Student_table['show']='headinsg'
        Student_table.column("Name", width=150)
        Student_table.column("Email", width=100)
        Student_table.column("Gender", width=100)
        Student_table.column("Contact", width=100)
        Student_table.column("D.o.b", width=100)
        Student_table.column("Address", width=150)
        Student_table.pack(fill=BOTH, expand=1)


root = Tk()
ob = Student(root)
root.mainloop()