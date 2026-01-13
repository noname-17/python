
# a simple project using simple python , mysql.connector module and mysql querries
import mysql.connector as my
ob=my.connect(host="localhost",user="root",database="cbse202312b",passwd="mysql")
c=ob.cursor()
c.execute('create database if not exists sales;')
c.execute('use sales;')
c.execute('create table if not exists login(username varchar(25) not null,password varchar(25) not null);')
c.execute('create table if not exists purchase(odate date not null,name varchar(25) not null,pcode int not null,amount int not null);')
c.execute('create table if not exists stock(pcode int not null,pname varchar(25) not null,quantity int not null,price int not null);')
ob.commit()
z=0
c.execute('select *from login;')
for i in c:
    z+=1
if z==0:
    c.execute("insert into login values('username','rj')")
    ob.commit()
while True:
    print('''
1.Admin
2.Customer
3.Exit''')
    ch=int(input('enter your choice'))
    if ch==1:
       passs=input('enter password:')
       c.execute("select * from login")
       for i in c:
           username,password=i
       if passs==password:
           print('welcome')
           loop2='y'
           if loop2=='y' or loop2=='Y':
              print('''
1.add new item
2.updating price 
3.Deleting Item
4.Display All Items
5.To change the password
6.Log Out''')
       ch1=int(input("Enter your choice: "))
       if ch1==1:
           loop='y'
           while loop=='y' or loop=='Y':
               pcode=int(input("Enter product code: "))
               pname=input("Enter product name: ")
               quantity=int(input("Enter product quantity: "))
               price=int(input("Enter product price: "))
               c.execute("insert into stock values({},'{}',{},{})".format(pcode,pname,quantity,price))
               ob.commit()
               print("Record Successfully Inserted...")
               loop=input("Do you want to enter more items(y/n): ")      
           loop2=input("Do You want to continue editing stock(y/n): ")
       elif ch1==2: 
           loop='y'
           while(loop=='y' or loop== 'Y'):        
               pcode=int(input("Enter product code: "))           
               new_price=int(input("Enter new price: "))           
               c.execute("update stock set price={} where pcode={}".format(new_price,pcode))            
               ob.commit()
               loop=input('do you want to change price of any other item y/n')
           loop2=input('do you want to continue editing stock y/n')
       elif ch1==3:
            loop='y'            
            while loop=='y' or loop=='Y':            
                pcode=int(input("Enter product code: "))            
                c.execute("delete from stock where pcode={}".format(pcode))            
                ob.commit()            
                loop=input("Do you want to delete any other data(y/n):")
            loop2=input("Do you want to continue editing stock(y/n): ")
       elif ch1==4:
            c.execute("select * from stock")  
            print("(pcode,pmame,quantity,price)")           
            print(c)
       elif ch1==5 :
            old_passs=input("Enter old password: ")
            c.execute("select * from login")
            for i in c:
                username, password=i
            if old_passs==password:
               new_passs=input("Enter new Password: ")
               c.execute("update login set password={}".format(new_passs))
               ob.commit()  
       elif ch1==6:
           break
       else:
           print("wrong password")
    elif ch==2:
       print('''1. Item Bucket
2. Payment
3. View Available Items
4. Go Back
''')
       ch2=int(input("Enter your choice:"))
       if ch2==1:
          name=input("Enter your name: ")
          pcode=int(input("Enter product code: "))
          quantity=int(input("Enter product quantity: "))
          c.execute("select * from stock where pcode={}".format(pcode))
          for i in c:
              t_code,t_name,t_quan,t_price=i
          amount=t_price*quantity
          net_quan=t_quan-quantity
          c.execute("update stock set quantity={} where pcode={}".format(net_quan,pcode))
          c.execute("insert into purchase values(now(),'{}',{},{})".format(name,pcode,amount))
          ob.commit()         
       elif ch2==2:
          print("amount to be paid {}".format(amount))
       elif ch2==3:
           print("CODE    NAME    PRICE")
           c.execute("select * from stock")
           for i in c:
               print(i)
       elif ch2==4:
         break    
    elif ch==3:

        break
