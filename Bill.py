from tkinter import* #GUI creation module and thin OO Layer
import random 
import time;
import cx_Oracle
con = cx_Oracle.connect("system/admin@localhost/xe")
cur=con.cursor()

root = Tk() #root window is created
root.geometry("1600x1000") #(length,width)
root.title("Restaurant Management Systems") #title of the window

text_Input=StringVar() #create a Tkinter variable, call the corresponding constructor
operator=""

Tops=Frame(root,width=1600,height=50,bg="powderblue",relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN) #uses rectangular areas in the screen to organize the layout and to provide padding of these widgets'''
f1.pack(side=LEFT)

f2=Frame(root,width=300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
#=================================Time=======================
localtime=time.asctime(time.localtime(time.time()))
#=================================Info=======================
lblInfo=Label(Tops,font=('arial',50,'bold'),text="Restaurant Management Systems",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
#==============================calculator=====================
def btnClick(numbers):
    global operator
    operator = operator+str(numbers)
    text_Input.set(operator)  #set the value, call the set method

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")
def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
    
def Ref():
    x=random.randint(10908,50863)
    randomRef= str(x)
    rand.set(randomRef)
    d={'Fries':Fries.get(),'Drink':Drinks.get()}
    Ser_Charge=0
    cus=con.cursor()
    cus.execute("""select name from menu""")
    for row in cus:
        s3=row[0]
        c=con.cursor()
        c.execute("""select price from menu where name=:param1""",{'param1':s3})
        CostofFries=float(d[s3])*float(*c.fetchone())
        Ser_Charge=Ser_Charge+(CostofFries)
    Service="Rs",str('%.2f' % Ser_Charge)
    ServiceCost.set(Service)
def qExit():
    con.close()
    root.destroy()
	
def Reset():
    rand.set("")
    Fries.set(0)
    Drinks.set(0)
    ServiceCost.set(0)



def ok():
        s1=int(e2.get())
        s2=e1.get()
        cu=con.cursor()
        cu.execute("""update menu set price=:param1 where name=:param2""",{'param1':s1,'param2':s2})
        con.commit()
    
def Update():
    master = Tk()
    Label(master, text="Item Name").grid(row=0)
    Label(master, text="Price").grid(row=1)
    global e1
    e1 = Entry(master)
    global e2
    e2 = Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    
    Button(master, text='ok', command=ok).grid(row=3, column=0, sticky=W, pady=4)
    

    master.mainloop( )


    

    
txtDisplay=Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue",justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="7",bg="powder blue",command=lambda: btnClick(7)).grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="8",bg="powder blue",command=lambda: btnClick(8)).grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="9",bg="powder blue",command=lambda: btnClick(9)).grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="+",bg="powder blue",command=lambda: btnClick("+")).grid(row=2,column=3)

btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="4",bg="powder blue",command=lambda: btnClick(4)).grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="5",bg="powder blue",command=lambda: btnClick(5)).grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="6",bg="powder blue",command=lambda: btnClick(6)).grid(row=3,column=2)

Subraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="-",bg="powder blue",command=lambda: btnClick("-")).grid(row=3,column=3)

btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="1",bg="powder blue",command=lambda: btnClick(1)).grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="2",bg="powder blue",command=lambda: btnClick(2)).grid(row=4,column=1)
btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="3",bg="powder blue",command=lambda: btnClick(3)).grid(row=4,column=2)

Multiply=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="*",bg="powder blue",command=lambda: btnClick("*")).grid(row=4,column=3)

btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="0",bg="powder blue",command=lambda: btnClick(0)).grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="C",bg="powder blue",command=btnClearDisplay).grid(row=5,column=1)
btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="=",bg="powder blue",command=btnEqualsInput).grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="/",bg="powder blue",command=lambda: btnClick("/")).grid(row=5,column=3)

#-----------------------Restaurent info 1 -----------
rand=StringVar()
Fries=StringVar(root, value=0)

lblReference = Label(f1,font=('arial',16,'bold'),text="Reference",bd=16,anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right',)
txtReference.grid(row=0,column=1)


lblfries = Label(f1,font=('arial',16,'bold'),text="LargeFries",bd=16,anchor='w')
lblfries.grid(row=1,column=0)
txtfries=Entry(f1,font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtfries.grid(row=1,column=1)

#-----------------------Restaurent info 2 -----------

Drinks=StringVar(root, value=0)
ServiceCost=StringVar(root, value=0)

lblDrinks = Label(f1,font=('arial',16,'bold'),text="Drinks",bd=16,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f1,font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=3)


lblServiceCost = Label(f1,font=('arial',16,'bold'),text="ServiceCost",bd=16,anchor='w')
lblServiceCost.grid(row=1,column=2)
txtServiceCost=Entry(f1,font=('arial',16,'bold'),textvariable=ServiceCost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtServiceCost.grid(row=1,column=3)


#-----------------buttons----------------

btnTotal=Button(f1,padx=16,pady=16,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command= Ref).grid(row=4,column=1)


btnReset=Button(f1,padx=16,pady=16,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command= Reset).grid(row=4,column=2)

btnUpdate=Button(f1,padx=16,pady=16,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Update",bg="powder blue",command= Update).grid(row=4,column=3)


btnExit=Button(f1,padx=16,pady=16,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command= qExit).grid(row=5,column=2)

root.mainloop() #show the root window and begin the main loop
