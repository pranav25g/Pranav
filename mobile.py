from tkinter import *
root=Tk()
count=0
def addrec():
    f=open('mobile.txt','a')
    brand=s1.get()
    price=s2.get()
    model=s3.get()
    manf=s4.get()
    avl=s5.get()
    f.writelines(brand.ljust(20)+price.ljust(10)+model.ljust(30)+manf.ljust(15)+avl.ljust(15)+"\n")
    f.close()
def nextrec():
    i=0
    f=open('mobile.txt','r')
    global count
    while(i<=count-1):
        l=f.readline()
        i=i+1
    k = l.split()
    s1.set(k[0])	
    s2.set(k[1])
    s3.set(k[2])
    s4.set(k[3])
    s5.set(k[4])
    count=count+1
    f.close()
def prev():
    f=open('mobile.txt','r')
    i=0
    global count
    count=count-1
    while(i<=count-1):
        l=f.readline()
        i=i+1
    l1 = l.split()
    s1.set(l1[0])	
    s2.set(l1[1])
    s3.set(l1[2])
    s4.set(l1[3])
    s5.set(l1[4])
    
    f.close()  
def update():
    brand=s1.get()
    price=s2.get()
    model=s3.get()
    manf=s4.get()
    avl=s5.get()
    f=open("mobile.txt","r")
    h=f.readlines()
    f.close()
    f=open("mobile.txt","w")
    flag=0
    for i in h:
        j=i.split()
        if(j[0]!=brand):
            f.writelines(j[0].ljust(20)+j[1].ljust(10)+j[2].ljust(30)+j[3].ljust(15)+j[4].ljust(15)+"\n")
        else :
            f.writelines(brand.ljust(20)+price.ljust(10)+model.ljust(30)+manf.ljust(15)+avl.ljust(15)+"\n")
            flag=1
    f.close()
def delete():
    k=[s1.get(), s2.get(), s3.get(), s4.get(), s5.get()]
    f=open("mobile.txt","r")
    h=f.readlines()
    f.close()
    f=open("mobile.txt","w")
    for i in h:
        j=i.split()
        if(j!=k):
            f.writelines(j[0].ljust(20)+j[1].ljust(10)+j[2].ljust(30)+j[3].ljust(15)+j[4].ljust(15)+"\n")
    f.close()
def search():
    k=s1.get()
    f=open("mobile.txt","r")
    h=f.readlines()
    for i in h:
        j=i.split()
        if(j[0]==k):
            s1.set(j[0])
            s2.set(j[1])
            s3.set(j[2])
            s4.set(j[3])
            s5.set(j[4])
    f.close()
def lr():
    
    f=open('mobile.txt','r')
    a=0
    b=0
    for i in f:
        a=a+1
    f.seek(0)
    h=f.readlines()
    l=list(h)
    l1=l[a-1].split()
    s1.set(l1[0])	
    s2.set(l1[1])
    s3.set(l1[2])
    s4.set(l1[3])
    s5.set(l1[4])
    f.close()
def fr():
    f=open('mobile.txt','r')
    a=0
    b=0
    for i in f:
        a=a+1
    f.seek(0)
    h=f.readlines()
    l=list(h)
    l1=l[0].split()
    s1.set(l1[0])	
    s2.set(l1[1])
    s3.set(l1[2])
    s4.set(l1[3])
    s5.set(l1[4])
    f.close()
s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()

left = Frame(root, width=800, height=720, bg='lightgreen')
left.pack()

heading =Label(root, text="Tech Mobiles", font=('arial 40 bold'), fg='black', bg='lightgreen')
heading.place(x=0,y=0)
       
name =Label(root, text="Brand", font=('arial 18 bold'), fg='black', bg='lightgreen')
name.place(x=0, y=100)

price =Label(root, text="Price", font=('arial 18 bold'), fg='black', bg='lightgreen')
price.place(x=0, y=140)

model =Label(root, text="Model No.", font=('arial 18 bold'), fg='black', bg='lightgreen')
model.place(x=0, y=180)

manf =Label(root, text="Manf. Date", font=('arial 18 bold'), fg='black', bg='lightgreen')
manf.place(x=0, y=220)

avl =Label(root, text="Availability", font=('arial 18 bold'), fg='black', bg='lightgreen')
avl.place(x=0, y=260)

t1 =Entry(left, width=30,textvariable=s1)

t2 =Entry(left, width=30,textvariable=s2)

t3 =Entry(left, width=30,textvariable=s3)

t4 =Entry(left, width=30,textvariable=s4)

t5 =Entry(left, width=30,textvariable=s5)


t1.place(x=250, y=100)
t2.place(x=250, y=140)
t3.place(x=250, y=180)
t4.place(x=250, y=220)
t5.place(x=250, y=260)

b1=Button(root,width=20, height=2, bg='steelblue',text=">", command=nextrec)
b2=Button(root,width=20, height=2, bg='steelblue',text="Add", command=addrec)
b3=Button(root,width=20, height=2, bg='steelblue',text="Delete", command=delete)
b4=Button(root,width=20, height=2, bg='steelblue',text="Search", command=search)
b5=Button(root,width=20, height=2, bg='steelblue',text="Update", command=update)
b7=Button(root,width=20, height=2, bg='steelblue',text=">|", command=lr)
b6=Button(root,width=20, height=2, bg='steelblue',text="|<", command=fr)
b8=Button(root,width=20, height=2, bg='steelblue',text="<", command=prev)

b1.place(x=300, y=340)
b2.place(x=300, y=400)
b3.place(x=500, y=400)
b4.place(x=500, y=340)
b5.place(x=500, y=480)
b6.place(x=300, y=500)
b7.place(x=300, y=600)
b8.place(x=300, y=290)


root.mainloop()


