import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql


#UX START

#WINDOW

win = tk.Tk()
win.geometry("1360x768+0+0")
win.state('zoomed')
win.title("Student management System")
win.config(bg="grey")

title_label = tk.Label(win,text="Student Management System",font=("Times New Roman",30,"bold"),border=12,relief=tk.GROOVE,bg="darkviolet",foreground="white")
title_label.pack(side=tk.TOP,fill=tk.X)

detail_frame = tk.LabelFrame(win,text="Enter Details",font=("Times New Roman",20),bg="lightblue",foreground = "black")
detail_frame.place(x=20,y=80,width=420,height=600)

data_frame = tk.Frame(win,bd=12,bg="lightblue",relief=tk.GROOVE)
data_frame.place(x=450,y=80,width=880,height=590)

# UX END

# VARIABLE START

name=tk.StringVar()
fname=tk.StringVar()
rollno=tk.StringVar()
gender=tk.StringVar()
dob=tk.StringVar()
dept=tk.StringVar()
section=tk.StringVar()
batch=tk.StringVar()
contact=tk.StringVar()
email=tk.StringVar()
address=tk.StringVar()

search_by=tk.StringVar()



# VARIABLE END


# FUNTIONS START

# DATA

def fetch_data():
    conn = pymysql.connect(host="localhost",user="root",password="",database="stm1")
    curr = conn.cursor()
    curr.execute("SELECT * FROM data")
    rows = curr.fetchall()
    if len(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('',tk.END,values=row)
        conn.commit()
    conn.close()

#BUTTONS FUNCTION START

# ADD
def add_func():
    if name.get() == "" or rollno.get() == "" or section.get() == "":
        messagebox.showerror("Error!","Please Fill All The Fields !")
    else:
        conn = pymysql.connect(host="localhost",user="root",password="",database="stm1")
        curr = conn.cursor()
        curr.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name.get(),fname.get(),rollno.get(),gender.get(),dob.get(),dept.get(),section.get(),batch.get(),contact.get(),email.get(),address.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Record has been inserted")
        clear()
        fetch_data()  #---this is used for instantly update data

# CLEAR
def clear():
    name.set("")
    fname.set("")
    rollno.set("")
    gender.set("")
    dob.set("")
    dept.set("")
    section.set("")
    batch.set("")
    contact.set("")
    email.set("")
    address.set("")

# FETCH FOCUS/SLECTION

def get_cursor(event):
    cursor_row = student_table.focus()
    contents=student_table.item(cursor_row)
    row = contents['values']
    
    name.set(row[0])
    fname.set(row[1])
    rollno.set(row[2])
    gender.set(row[3])
    dob.set(row[4])
    dept.set(row[5])
    section.set(row[6])
    batch.set(row[7])
    contact.set(row[8])
    email.set(row[9])
    address.set(row[10])


    # UPDATE

def update_data():
    conn = pymysql.connect(host="localhost",user="root",password="",database="stm1")
    curr = conn.cursor()
    curr.execute(
        "UPDATE data SET name=%s, fname=%s, rollno=%s, gender=%s, dob=%s, dept=%s, section=%s, batch=%s, contact=%s, email=%s, address=%s WHERE rollno=%s",
        (name.get(), fname.get(), rollno.get(), gender.get(), dob.get(), dept.get(), section.get(), batch.get(), contact.get(), email.get(), address.get(), rollno.get()))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Record has been updated")
    fetch_data()
    clear()
    
    #DELETE
def delete_data():
    conn = pymysql.connect(host="localhost",user="root",password="",database="stm1")
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE rollno=%s",rollno.get())
    conn.commit()
    conn.close()
    messagebox.showinfo("Success","Record has been Deleted")
    clear()
    fetch_data() 


    # SEARCH
def search_data():
    conn = pymysql.connect(host="localhost",user="root",password="",database="stm1")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data WHERE " + str(search_by.get() +" Like'%" + str(txt_search.get()) + "%'" ))
    rows= cur.fetchall()
    if len(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('',tk.END,values=row)
        conn.commit()
    conn.close()
    

    #SEARCH ALL


#BUTTONS FUNCTION END

# FUNCTIONS END


#DETAILS FRAME START

#Name
name_label=tk.Label(detail_frame,text="Name",font=("Times New Roman",17),bg="lightblue")
name_label.grid(row=0,column=0,padx=2,pady=2,sticky=tk.W)

name_enter=tk.Entry(detail_frame,border=7,font=("Times New Roman",17),textvariable=name)
name_enter.grid(row=0,column=1,padx=2,pady=2,)

#Father Name
fname_label=tk.Label(detail_frame,text="Father's Name",font=("Times New Roman",17),bg="lightblue")
fname_label.grid(row=1,column=0,padx=2,pady=2,sticky=tk.W)

fname_enter=tk.Entry(detail_frame,border=7,font=("Times New Roman",17),textvariable=fname)
fname_enter.grid(row=1,column=1,padx=2,pady=2,)

#Rollno

rollno_label=tk.Label(detail_frame,text="Roll number",font=("Times New Roman",17),bg="lightblue")
rollno_label.grid(row=2,column=0,padx=2,pady=2,sticky=tk.W)

rollno_enter=tk.Entry(detail_frame,border=7,font=("Times New Roman",17),textvariable=rollno)
rollno_enter.grid(row=2,column=1,padx=2,pady=2)

#gender

gender_label=tk.Label(detail_frame,text="Gender",font=("Times New Roman",17),bg="lightblue")
gender_label.grid(row=3,column=0,padx=2,pady=2,sticky=tk.W)

gender_enter=ttk.Combobox(detail_frame,font=("Times New Roman",17),state="readonly", textvariable=gender)
gender_enter['values']=("Male","Female","Others")
gender_enter.grid(row=3,column=1,padx=2,pady=2)
#dob

dob_label=tk.Label(detail_frame,text="Date of Birth",font=("Times New Roman",17),bg="lightblue")
dob_label.grid(row=4,column=0,padx=2,pady=2,sticky=tk.W)

dob_enter=tk.Entry(detail_frame,bd=7,font=("Times New Roman",17), textvariable=dob)
dob_enter.grid(row=4,column=1,padx=2,pady=2)

#dept

dept_label=tk.Label(detail_frame,text="Department",font=("Times New Roman",17),bg="lightblue")
dept_label.grid(row=5,column=0,padx=2,pady=2,sticky=tk.W)

dept_enter=tk.Entry(detail_frame,border=7,font=("Times New Roman",17), textvariable=dept)
dept_enter.grid(row=5,column=1,padx=2,pady=2,)

#section

section_label=tk.Label(detail_frame,text="Section",font=("Times New Roman",17),bg="lightblue")
section_label.grid(row=6,column=0,padx=2,pady=2,sticky=tk.W)

section_enter=tk.Entry(detail_frame,border=7,font=("Times New Roman",17), textvariable=section)
section_enter.grid(row=6,column=1,padx=2,pady=2,)

#batch

batch_label=tk.Label(detail_frame,text="Batch",font=("Times New Roman",17),bg="lightblue")
batch_label.grid(row=7,column=0,padx=2,pady=2,sticky=tk.W)

batch_enter=tk.Entry(detail_frame,border=7,font=("Times New Roman",17), textvariable=batch)
batch_enter.grid(row=7,column=1,padx=2,pady=2,)

#contact

contact_label=tk.Label(detail_frame,text="Contact",font=("Times New Roman",17),bg="lightblue")
contact_label.grid(row=8,column=0,padx=2,pady=2,sticky=tk.W)

contact_enter=tk.Entry(detail_frame,border=7,font=("Times New Roman",17), textvariable=contact)
contact_enter.grid(row=8,column=1,padx=2,pady=2,)

#email

email_label=tk.Label(detail_frame,text="Email",font=("Times New Roman",17),bg="lightblue")
email_label.grid(row=9,column=0,padx=2,pady=2,sticky=tk.W)

email_enter=tk.Entry(detail_frame,border=7,font=("Times New Roman",17), textvariable=email)
email_enter.grid(row=9,column=1,padx=2,pady=2,)

#address

address_label=tk.Label(detail_frame,text="Address",font=("Times New Roman",17),bg="lightblue")
address_label.grid(row=10,column=0,padx=2,pady=2,sticky=tk.W)

address_enter=tk.Entry(detail_frame,border=7,font=("Times New Roman",17), textvariable=address)
address_enter.grid(row=10,column=1,padx=1,pady=2,)



#DETAILS FRAME END

#BUTTONS START

btn_frame=tk.Frame(detail_frame,bg="red",border=5,relief=tk.GROOVE)
btn_frame.place(x=8,y=500,width=400,height=60)


add_btn=tk.Button(btn_frame,bg="maroon",text="Add",bd=7,font=("New Times Roman",11),width=7,command=add_func)
add_btn.grid(row=0,column=0,padx=7,pady=2)

update_btn=tk.Button(btn_frame,bg="maroon",text="Update",bd=7,font=("New Times Roman",11),width=7,command=update_data)
update_btn.grid(row=0,column=1,padx=7,pady=2)

delete_btn=tk.Button(btn_frame,bg="maroon",text="Delete",bd=7,font=("New Times Roman",11),width=7,command=delete_data)
delete_btn.grid(row=0,column=2,padx=7,pady=2)

clear_btn=tk.Button(btn_frame,bg="maroon",text="Clear",bd=7,font=("New Times Roman",11),width=7,command=clear)
clear_btn.grid(row=0,column=3,padx=7,pady=2)

#BUTTONS END




#SEARCH START

search_frame=tk.Frame(data_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X,padx=7,pady=8)

search_label= tk.Label(search_frame,text="Search",bg="lightgrey",font=("Times New Roman",15))
search_label.grid(row=0,column=0,padx=2,pady=2)

search_in= ttk.Combobox(search_frame,font=("Times New Roman",15),state="readonly", textvariable=search_by)
search_in['values']=("Name","Rollno","Father Name","Gender","Batch","Section","Contact")
search_in.grid(row=0,column=1,padx=12,pady=2)

txt_search=tk.Entry(search_frame,font=("Times New Roman",15),width=20,bd=5,relief=tk.GROOVE)
txt_search.grid(row=0,column=2,padx=12,pady=2)

search_btn=tk.Button(search_frame,text="Search",font=("Times New Roman",11),bd=7,width=12,bg="maroon",command=search_data)
search_btn.grid(row=0,column=3,padx=12,pady=2)

showall_btn=tk.Button(search_frame,text="Show All",font=("Times New Roman",11),bd=7,width=12,bg="maroon",command=fetch_data)
showall_btn.grid(row=0,column=4,padx=12,pady=2) 


#SEARCH END

#DATA FRAME START

main_frame=tk.Frame(data_frame,bg="lightblue",bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll=tk.Scrollbar(main_frame,orient=tk.VERTICAL)
x_scroll=tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)

student_table=ttk.Treeview(main_frame,columns=("name","fname","rollno","gender","dob","dept","section","batch","contact","email","address"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

student_table.heading("name",text="Name")
student_table.heading("fname",text="Father Name")
student_table.heading("rollno",text="Roll No")
student_table.heading("gender", text="Gender")
student_table.heading("dob", text="D.O.B")
student_table.heading("dept", text="Dept")
student_table.heading("section", text="Section")
student_table.heading("batch", text="Batch")
student_table.heading("contact", text="Contact")
student_table.heading("email", text="Email")
student_table.heading("address", text="Address")


student_table['show']='headings'

student_table.column("name",width=100)
student_table.column("fname",width=100)
student_table.column("rollno",width=100)
student_table.column("gender",width=100)
student_table.column("dob",width=100)
student_table.column("dept", width=100)
student_table.column("section",width=100)
student_table.column("batch", width=100)
student_table.column("contact",width=100)
student_table.column("email",width=150)
student_table.column("address",width=150)


student_table.pack(fill=tk.BOTH,expand=True)
student_table.bind("<ButtonRelease-1>",get_cursor)


#DATA FRAME END



fetch_data()


win.mainloop()

