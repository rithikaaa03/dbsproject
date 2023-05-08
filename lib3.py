from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        #=======================================variable=============================
        self.member_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()

        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

        #=======================================DataFrameLeft=============================

        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type", font=("arial",12,"bold"),padx=2,pady=6) 
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("arial",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)


        lblIDNO=Label(DataFrameLeft,font=("arial",12,"bold"),text="ID No:",padx=2,pady=6,bg="powder blue")
        lblIDNO.grid(row=1,column=0,sticky=W)
        txtIDNO=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.id_var,width=29)
        txtIDNO.grid(row=1,column=1)

        lblFirstName=Label(DataFrameLeft,font=("arial",12,"bold"),text="First Name:",padx=2,pady=6,bg="powder blue")
        lblFirstName.grid(row=2,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=2,column=1)

        lblLastName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Last Name:",padx=2,pady=6,bg="powder blue")
        lblLastName.grid(row=3,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=3,column=1)

        lblAddress1=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address 1:",padx=2,pady=6,bg="powder blue")
        lblAddress1.grid(row=4,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=4,column=1)

        lblAddress2=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address 2:",padx=2,pady=6,bg="powder blue")
        lblAddress2.grid(row=5,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=5,column=1)


        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mobile:",padx=2,pady=6,bg="powder blue")
        lblMobile.grid(row=6,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=6,column=1)

        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Id:",padx=2,pady=6,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Title:",padx=2,pady=6,bg="powder blue")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,font=("arial",12,"bold"),text="Author Name:",padx=2,pady=6,bg="powder blue")
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.author_var,width=29)
        txtAuthor.grid(row=2,column=3)

        lblActualPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Actual Price:",padx=2,pady=6,bg="powder blue")
        lblActualPrice.grid(row=3,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.finalprice_var,width=29)
        txtActualPrice.grid(row=3,column=3)

        lblDateBorrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Borrowed",padx=2,pady=6,bg="powder blue")
        lblDateBorrowed.grid(row=4,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=4,column=3)

        lblDateDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Due:",padx=2,pady=6,bg="powder blue")
        lblDateDue.grid(row=5,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=5,column=3)


        lblDateOverdate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Return Date:",padx=2,pady=6,bg="powder blue")
        lblDateOverdate.grid(row=6,column=2,sticky=W)
        txtDateOverdate=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateoverdue_var,width=29)
        txtDateOverdate.grid(row=6,column=3)



        #=======================================DataFrame Right=============================

        DataFrameRight=LabelFrame(frame,padx=20,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("arial",12,"bold"))
        DataFrameRight.place(x=870,y=5,width=580,height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Introduction to Computer Science Using Python','C language programming','Introduction to Algorithms','Structure and Interpretation of Computer Programs','C++ Programming Language','Computer Organization and Design','Effective Java','Compilers: Principles, Techniques and Tools','Data Structures and Algorithms','Operating System Concepts','Database System Concepts']
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Introduction to Computer Science Using Python"):
                self.bookid_var.set("BKID101")
                self.booktitle_var.set("Introduction to Computer Science Using Python")
                self.author_var.set("Charles Dierbach")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dateoverdue_var.set("")
                self.finalprice_var.set("Rs.569")

            elif (x=="C language programming"):
                self.bookid_var.set("BKID102")
                self.booktitle_var.set("C language programming")
                self.author_var.set("Brian W. Kernighan")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dateoverdue_var.set("")
                self.finalprice_var.set("Rs.761")

            elif (x=="Introduction to Algorithms"):
                self.bookid_var.set("BKID103")
                self.booktitle_var.set("Introduction to Algorithms")
                self.author_var.set("Thomas H. Cormen")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dateoverdue_var.set("")
                self.finalprice_var.set("Rs.899")

            elif (x=="Structure and Interpretation of Computer Programs"):
                self.bookid_var.set("BKID104")
                self.booktitle_var.set("Structure and Interpretation of Computer Programs")
                self.author_var.set("Harold Abelson")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dateoverdue_var.set("")
                self.finalprice_var.set("Rs.590")

            elif (x=="C++ Programming Language"):
                self.bookid_var.set("BKID105")
                self.booktitle_var.set("C++ Programming Language")
                self.author_var.set("Bjarne Stroustrup")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dateoverdue_var.set("")
                self.finalprice_var.set("Rs.554")

            elif (x=="Computer Organization and Design"):
                self.bookid_var.set("BKID106")
                self.booktitle_var.set("Computer Organization and Design")
                self.author_var.set("David A. Patterson")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dateoverdue_var.set("")
                self.finalprice_var.set("Rs.569")

            elif (x=="Effective Java"):
                self.bookid_var.set("BKID107")
                self.booktitle_var.set("Effective Java")
                self.author_var.set("Joshua Bloch")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dateoverdue_var.set("")
                self.finalprice_var.set("Rs.569")

            elif (x=="Compilers: Principles, Techniques and Tools"):
                self.bookid_var.set("BKID108")
                self.booktitle_var.set("Compilers: Principles, Techniques and Tools")
                self.author_var.set("Alfred V. Aho")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dateoverdue_var.set("")
                self.finalprice_var.set("Rs.575")

            elif (x=="Data Structures and Algorithms"):
                self.bookid_var.set("BKID109")
                self.booktitle_var.set("Data Structures and Algorithms")
                self.author_var.set("Jeffrey D. Ullman")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dateoverdue_var.set("")
                self.finalprice_var.set("Rs.679")

            elif (x=="Operating System Concepts"):
                self.bookid_var.set("BKID110")
                self.booktitle_var.set("Operating System Concepts")
                self.author_var.set("Abraham Silberschatz")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dateoverdue_var.set("")
                self.finalprice_var.set("Rs.969")

            elif (x=="Database System Concepts"):
                self.bookid_var.set("BKID111")
                self.booktitle_var.set("Database System Concepts")
                self.author_var.set("Abraham Silberschatz")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dateoverdue_var.set("")
                self.finalprice_var.set("Rs.869")


        
        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)

        #=======================================Buttons Frame=============================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(Framebutton,command=self.adda_data,text="Add person",font=("arial",12,"bold"),width=12,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)
        btnAddData=Button(Framebutton,command=self.adda1_data,text="Add book",font=("arial",12,"bold"),width=11,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.showData,text="Show person",font=("arial",12,"bold"),width=12,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)
        btnAddData=Button(Framebutton,command=self.showData,text="Show book",font=("arial",12,"bold"),width=11,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.update,text="Update person",font=("arial",12,"bold"),width=12,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)
        btnAddData=Button(Framebutton,command=self.update,text="Update book",font=("arial",12,"bold"),width=11,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete person",font=("arial",12,"bold"),width=12,bg="blue",fg="white")
        btnAddData.grid(row=0,column=6)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete book",font=("arial",12,"bold"),width=11,bg="blue",fg="white")
        btnAddData.grid(row=0,column=7)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=8)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=9)

        #=======================================information Frame=============================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=590,width=1530,height=210)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("membertype","idno","firstname","lastname","address1","address2","mobile","bookid","booktitle","author","dateborrowed","datedue","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)


        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("idno",text="ID No.")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address 1")
        self.library_table.heading("address2",text="Address 2")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date of Borrowing")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("dateoverdue",text="Date Returned")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("idno",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="mydata2")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into person values(%s,%s,%s,%s,%s,%s,%s)",
                          (self.member_var.get(),self.id_var.get(),self.firstname_var.get(),self.lastname_var.get(),
                           self.address1_var.get(),self.address2_var.get(),self.mobile_var.get()))
        my_cursor.execute("insert into borrow values(%s,%s,%s,%s,%s)",self.id_var.get(),self.bookid_var.get(),
                           self.dateborrowed_var.get(),self.datedue_var.get(),self.dateoverdue_var.get())
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("success","member has been inserted successfully")
    def adda1_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="mydata2")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                          (self.member_var.get(),self.id_var.get(),self.firstname_var.get(),self.lastname_var.get(),
                           self.address1_var.get(),self.address2_var.get(),self.mobile_var.get(),self.bookid_var.get(),self.booktitle_var.get(),self.author_var.get(),
                           self.dateborrowed_var.get(),self.datedue_var.get(),self.dateoverdue_var.get(),self.finalprice_var.get()))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("success","member has been inserted successfully")

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="mydata2")
        my_cursor=conn.cursor()
        my_cursor.execute("update person set Member=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,Mobile=%s where idno=%s",
                          (self.member_var.get(),self.firstname_var.get(),self.lastname_var.get(),
                           self.address1_var.get(),self.address2_var.get(),self.mobile_var.get(),self.id_var.get()))

        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()    
        messagebox.showinfo("Success","member has been updated")
                        

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="mydata2")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from person natural join book natural join borrow")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.id_var.set(row[1]),
        self.firstname_var.set(row[2]),
        self.lastname_var.set(row[3]),
        self.address1_var.set(row[4]),
        self.address2_var.set(row[5]),
        self.mobile_var.set(row[6]),
        self.bookid_var.set(row[7]),
        self.booktitle_var.set(row[8]),
        self.author_var.set(row[9]),
        self.dateborrowed_var.set(row[10]),
        self.datedue_var.set(row[11]),
        self.dateoverdue_var.set(row[12]),
        self.finalprice_var.set(row[13])
    
    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END,"ID No:\t\t"+self.id_var.get()+"\n")
        self.txtBox.insert(END,"First Name:\t\t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"Last Name:\t\t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address1:\t\t"+self.address1_var.get()+"\n")
        self.txtBox.insert(END,"Address2:\t\t"+self.address2_var.get()+"\n")
        self.txtBox.insert(END,"Mobile No:\t\t"+self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book Id:\t\t"+self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Title:\t\t"+self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Author:\t\t"+self.author_var.get()+"\n")
        self.txtBox.insert(END,"Date Borrowed:\t\t"+self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"Date Due:\t\t"+self.datedue_var.get()+"\n")
        self.txtBox.insert(END,"Return Date:\t\t"+self.dateoverdue_var.get()+"\n")
        self.txtBox.insert(END,"Final Price:\t\t"+self.finalprice_var.get()+"\n")
     
    def reset(self):
        self.member_var.set("")
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set("")
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit?")
        if iExit>0:
            self.root.destroy()
            return
    def delete(self):
        if self.id_var.get()=="":
            messagebox.showerror("Error","first select the member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="mydata2")
            my_cursor=conn.cursor()
            query="delete from person where idno=%s"
            value=(self.id_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","member has been deleted")

if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()