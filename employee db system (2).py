
# coding: utf-8

# In[ ]:

#EMPLOYEE MANAGEMENT SYSTEM
import pymysql
from tkinter import *
from tkinter import messagebox
def search():
    try:
        con=pymysql.connect("localhost","root","","python_demo")
        cur=con.cursor()
        sql="select * from employee where employee_id='%s'"%employee_id.get()
        cur.execute(sql)
        result=cur.fetchone()
        employee_name.set(result[1])
        employee_salary.set(result[2])
        employee_age.set(result[3])
        employee_hiredate.set(result[4])
        employee_address.set(result[5])
        e1.configure(state='disabled')
        con.close()
    except:
        messagebox.showinfo('No Data','No such data available...')
        clear()
def clear():
    employee_id.set('')
    employee_name.set('')
    employee_salary.set('')
    employee_age.set('')
    employee_hiredate.set('')
    employee_address.set('')
    e1.configure(state='normal')
def add():
    try:
        con=pymysql.connect("localhost","root","","python_demo")
        cur=con.cursor()
        sql="insert into employee values (%s,'%s',%s,%s,'%s','%s')"        %(employee_id.get(),employee_name.get(),employee_salary.get(),employee_age.get(),employee_hiredate.get(),employee_address.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('Success','Record saved...')
    except:
        messagebox.showinfo('Error','Error in data entry...')
    finally:
        clear()
def update():
    try:
        con=pymysql.connect("localhost","root","","python_demo")
        cur=con.cursor()
        sql="update employee set employee_name='%s',employee_salary=%s,employee_age=%s,employee_hiredate='%s',employee_address='%s'where employee_id=%s"        %(employee_name.get(),employee_age.get(),employee_hiredate.get(),employee_address.get(),employee_id.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('Success','Record updated...')
    except:
        messagebox.showinfo('Error','Error occured...')
    finally:
        clear()
def delete():
    try:
        con=pymysql.connect("localhost","root","","python_demo")
        cur=con.cursor()
        sql="delete from student where employee_id=%s"        %(employee_id.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('Success','Record deleted...')
    except:
        messagebox.showinfo('Error','Error occured...')
    finally:
        clear()
w1=Tk()
w1.title('My app')
w1.geometry('500x500')
ptitle=Label(w1,text='''Employee Database Management System''')
ptitle.grid(row=0,column=0,columnspan=2)



employee_id=StringVar()
employee_name=StringVar()
employee_salary=StringVar()
employee_age=StringVar()
employee_hiredate=StringVar()
employee_address=StringVar()


l1=Label(w1,text='EMPLOYEE ID')
e1=Entry(w1,textvariable=employee_id)
l2=Label(w1,text='EMPLOYEE_NAME')
e2=Entry(w1,textvariable=employee_name)
l3=Label(w1,text='EMPLOYEE_SALARY')
e3=Entry(w1,textvariable=employee_salary)
l4=Label(w1,text='EMPLOYEE_AGE')
e4=Entry(w1,textvariable=employee_age)
l5=Label(w1,text='EMPLOYEE_HIREDATE')
e5=Entry(w1,textvariable=employee_hiredate)
l6=Label(w1,text='EMPLOYEE_ADDRESS')
e6=Entry(w1,textvariable=employee_address)

b1=Button(w1,text='Search',command=search)
b2=Button(w1,text='Add',command=add)
b3=Button(w1,text='Update',command=update)
b4=Button(w1,text='Delete',command=delete)
b5=Button(w1,text='Clear',command=clear)

l1.grid(row=1,column=0)
e1.grid(row=1,column=1)
b1.grid(row=1,column=2)
l2.grid(row=2,column=0)
e2.grid(row=2,column=1)
l3.grid(row=3,column=0)
e3.grid(row=3,column=1)
l4.grid(row=4,column=0)
e4.grid(row=4,column=1)
l5.grid(row=5,column=0)
e5.grid(row=5,column=1)
l6.grid(row=6,column=0)
e6.grid(row=6,column=1)

b2.grid(row=7,column=0)
b3.grid(row=7,column=1)
b4.grid(row=8,column=0)
b5.grid(row=8,column=1)    
w1.mainloop()
        
        
       

