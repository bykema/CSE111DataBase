import sqlite3
from sqlite3 import Error
import sys
from datetime import date


def openConnection(_dbFile):
    

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        
    except Error as e:
        print(e)

    

    return conn

def closeConnection(_conn, _dbFile):
    

    try:
        _conn.close()
        
    except Error as e:
        print(e)

   





#creating database side



#creating tables in the database
def createTables(_conn):
    

    try:
        #sql = """DROP TABLE IF EXISTS cart;"""
        #_conn.execute(sql) #execute defined command

        sql = """CREATE TABLE cart (
            cart_id int,
            cart_name varchar not null, 
            cart_price decimal(2,2)
            );"""
        _conn.execute(sql) #execute defined command

        #sql = """DROP TABLE IF EXISTS products;"""
        #_conn.execute(sql) #execute defined command

        sql = """CREATE TABLE products (
            p_id int PRIMARY KEY,
            p_name varchar UNIQUE,
            p_onhand int NOT NULL,
            p_made int,
            p_shipped int,
            p_size int,
            p_unitweight int,
            p_desc string,
            p_price decimal(2,2) NOT NULL
            );
            """
        _conn.execute(sql) #execute defined command

        #sql = """DROP TABLE IF EXISTS orders;"""
        #_conn.execute(sql) #execute defined command

        sql = """CREATE TABLE orders(
            o_customer int,
            o_amount int,
            o_price int,
            o_product varchar(20),
            o_date str,
            o_shipdate string,
            o_recievedate string,
            o_id int PRIMARY KEY
            );
            """
        _conn.execute(sql) #execute defined command

        #sql = """DROP TABLE IF EXISTS customers;"""
        #_conn.execute(sql) #execute defined command

        sql = """CREATE TABLE customers(
            c_id int PRIMARY KEY,
            c_fname varchar,
            c_lname varchar(20) NOT NULL,
            c_email varchar,
            c_address string(40)
            );
            """
        _conn.execute(sql) #execute defined command

        #sql = """DROP TABLE IF EXISTS suppliers;"""
        #_conn.execute(sql) #execute defined command

        sql = """CREATE TABLE suppliers(
            s_id varchar PRIMARY KEY,
            s_name varchar,
            s_product
            );"""
        _conn.execute(sql) #execute defined command

        #sql = """DROP TABLE IF EXISTS payment;"""
        #_conn.execute(sql) #execute defined command

        sql = """CREATE TABLE payment(
            pay_customer,
            pay_id int PRIMARY KEY,
            pay_type varchar,
            pay_allowed varchar(20) NOT NULL,
            pay_orderid int
            );
            """
        _conn.execute(sql) #execute defined command

        #sql = """DROP TABLE IF EXISTS categories;"""
        #_conn.execute(sql) #execute defined command

        sql = """CREATE TABLE categories(
            cat_id varchar PRIMARY KEY,
            cat_name varchar UNIQUE,
            cat_desc varchar(20) NOT NULL
            );
            """
        _conn.execute(sql) #execute defined command        

        _conn.commit()
       
    except Error as e:
        _conn.rollback()
        print(e)

  


#populate tables
def populateTables(_conn):
    

    try:
        sql = """INSERT INTO products (
            p_id,
            p_name,
            p_desc,
            p_unitweight,
            p_onhand, 
            p_made,
            p_shipped,
            p_price
            )
            VALUES 
            (1, 'healing salve','herbal healing', 6, 10, 15, 5, 24.00),
            (2, 'Orange Cream', 'body butter', 6, 9, 15, 6, 16.00),
            (3, 'Cocao Baby', 'body butter', 6, 14, 15, 1, 16.00 ),
            (4, 'Turmeric', 'facial bar', 2, 9, 15, 9, 8.00),
            (5, 'Chlorella', 'body bar',2, 15, 15, 0, 12.00),
            (6, 'Himalayan Clay', 'body bar', 2, 15, 15, 0, 12.00),
            (7, 'Clay' ,'body bar', 2, 14, 15, 1, 12.00),
            (8, 'Rose', 'facial bar', 2, 7, 15, 8, 12.00),
            (9, 'Beard oil' ,' hair ', 4, 14, 15, 1, 22.00),
            (10, 'herbal hair growth' ,'hair', 4, 10, 15, 3, 32.00),
            (11, 'hungry hair' ,'hair', 6, 12, 15, 9, 20.00),
            (12, 'fresh' ,'lady parts', 2, 14, 15, 1, 8.00),
            (13, 'lady parts oil' ,'lady parts', 4, 8, 12, 4, 16.00),
            (14, 'bath bomb' ,'lady parts', 1, 14, 15, 1, 5.00),
            (15, 'steam' ,'lady parts', 2, 15, 20, 5, 5.00);
            """
        _conn.execute(sql) #execute defined command

        #sql = "INSERT INTO cart(cart_id, cart_name, cart_price) VALUES (1, 'healing salve', 1)  "
        #_conn.execute(sql) #execute defined command

        sql = """INSERT INTO orders(
            o_customer,
            o_price ,
            o_product, 
            o_amount,
            o_date,
            o_shipdate,
            o_recievedate,
            o_id
            )
            VALUES
            (07, 120, '2,3,5,7', 3, '10/25/2011', '10/26/2011', '10/30/2011', 1004),
            (09, 35, '2,8,5,1', 1, '07/25/2011', '07/26/2011', '07/30/2011', 1002),
            (10, 35, '15,14,12', 18, '08/25/2011', '8/26/2011', '08/30/2011', 1014),
            (03, 35, '2,8,5,1', 1, '09/25/2011', '09/26/2011', '09/30/2011', 1013),
            (07, 35, '2,8,5,1', 1, '10/25/2011', '10/26/2011', '10/30/2011', 1012),
            (03, 35, '2,8,5,1', 1, '11/25/2011', '11/26/2011', '11/30/2011', 1011),
            (03, 35, '2,8,5,1', 1, '12/25/2011', '12/26/2011', '12/30/2011', 1010),
            (11, 35, '2,8,5,1', 1, '01/25/2011', '01/26/2011', '01/30/2011', 1009),
            (09, 35, '2,8,5,1', 1, '02/25/2011', '02/26/2011', '02/30/2011', 1008),
            (19, 35, '2,8,5,1', 1, '03/25/2011', '03/26/2011', '03/30/2011', 1007),
            (05, 35, '2,8,5,1', 1, '07/25/2011', '07/26/2011', '07/30/2011', 1006),
            (01, 35, '2,8,5,1', 1, '04/25/2011', '04/26/2011', '04/30/2011', 1005),
            (03, 35, '2,8,5,1', 1, '05/25/2011', '05/26/2011', '05/30/2011', 1003),
            (05, 16, '2,5,5,5', 2, '02/25/2011', '02/26/2011', '02/30/2011', 1001)
            ;
            """
        _conn.execute(sql) #execute defined command

        sql = """INSERT INTO Customers (
            c_id,
            c_fname,
            c_lname,
            c_email,
            c_address
            )
            VALUES 
            (01, 'Alexa', 'Adams', 'aa11@gmail.com', '1234 Camino Ave'),
            (02, 'David', 'Dire', 'dd44@gmail.com', '3387 Overland Ave'),
            (03, 'Nathan', 'Night', 'nateman16@yahoo.com', '1224 1st St'),
            (04, 'Shantelle', 'Snow', 'ss1818@gmail.com', '2359 Yosemite Ave'),
            (05, 'Charles', 'Charleston', 'cc33@hotmail.com', '2466 Bear creek Rd'),
            (06, 'Preston', 'Prescott', 'pp1616@yahoo.com', '3321 Gun Club Rd'),
            (07, 'Estrella', 'Espinosa', 'ee890@gmail.com', '2399 Vera Cruz Rd'),
            (08, 'Britney', 'Bodea', 'bb22@gmail.com', '1776 America Ave'),
            (09, 'Jerome', 'Jakobs', 'jj1010@outlook.com', '3356 Main St'),
            (10, 'Fatima', 'Fastin', 'ff66@outlook.com', '9909 Pickle Ct'),
            (11, 'Dianne', 'Ellison', 'De72@gmail.com', '4420 Willowbrook dr'),
            (12, 'Chris', 'Gipson', 'cg54@outlook.com', '3199 vera lane'),
            (13, 'Destiny', 'Jakobs', 'Dj1010@outlook.com', '9961 lancaster St'),
            (14, 'Fatima', 'Fastin', 'ff66@outlook.com', '9909 Pickle Ct'),
            (15, 'Angel', 'Lupe', 'al1010@outlook.com', '9675 lucky ln'),
            (16, 'Daniel', 'Castro', 'dc1010@outlook.com', '3356 stormy St'),
            (17, 'Lala', 'Battle', 'lb1010@outlook.com', '3345 Minute circle'),
            (18, 'Jeremy', 'Hike', 'jh1010@outlook.com', '3564 university way'),
            (19, 'Terrence', 'Pasereti', 'tp1010@outlook.com', '3376 nemo St'),
            (20, 'Jerome', 'Stout', 'jj1010@outlook.com', '3356 martin St')
            ;
            """
        _conn.execute(sql) #execute defined command

        sql = """INSERT INTO Payment(
            pay_customer,
            pay_id, 
            pay_type, 
            pay_allowed,
            pay_orderid 
            )
            VALUES
            (7, 1, 'cashapp', 'yes', 1004),
            (9, 2, 'venmo', 'yes', 1002),
            (5, 3, 'paypal', 'no', 1001)
            ;
            """
        _conn.execute(sql) #execute defined command

        sql = """INSERT INTO Suppliers(
	        s_id,
	        s_name,
	        s_product
            )
            VALUES
            (1, 'Supplier A', 'Rose'),
            (2, 'Supplier B', 'Orange Cream'),
            (3, 'Supplier C', 'Tumeric'),
            (4, 'Supplier D', 'healing salve'),
            (5, 'Supplier E', 'Himalayan Clay')
            ;
            """
        _conn.execute(sql) #execute defined command

        sql = """INSERT INTO Categories(
            cat_id, 
            cat_name,
            cat_desc
            )
            VALUES 
            (007, 'body butter', 'whipped'),
            (009, 'healing', 'herbal'),
            (005, 'bar', 'detox')
            ;
            """
        _conn.execute(sql) #execute defined command

        _conn.commit()
        

    except Error as e:
        _conn.rollback()
        print(e)

    











#beginning of user interaction side

#customer interaction
def startAsCust(_conn):
    connect = _conn
    while 0 == 0:
        print("Hello! Thank you for coming to our store. What would you like to do?\n")
        print("1: Go to ordering menu?\n")
        print("2: Create an account?\n")
        print("3: Return to main menu\n")
        choice = input("Enter number for choice: ")
        if choice == 1:
            orderMenu(connect)
        elif choice == 2:
            accountMenu(connect)
        elif choice == 3:
            break
        else :
            print("Invalid Entry, please retry\n")

#ordering
def orderMenu(_conn):
    connect = _conn
    while 0 == 0:
        print("Welcome to ordering menu. What would you like to do?\n")
        print("1: Create your order\n")
        print("2: View your cart.\n")
        print("3: Return to previous menu\n")
        choice = input("Enter number for choice: ")
        if choice == 2:
            cartView(connect)
        elif choice == 1:
            createOrder(connect)
        elif choice == 3:
            break
        else :
            print("Invalid Entry, please retry\n")


def createOrder(_conn):
    connect = _conn
    while 0 == 0:
        print("Please browse our product list\n")
        try:
            sql = """SELECT p_id, p_name, p_desc, p_price, p_onhand 
                    FROM products"""
            cur = _conn.cursor()
            cur.execute(sql) #execute defined command

            l = '{:>10} {:>16} {:>19} {:>15} {:>15}'.format("Id", "Name", "Description", "Price", "Stock")
            print (l)
            rows = cur.fetchall()

            for row in rows:    
                l = '{:>10} {:>20} {:>15} {:>15} {:>15}'.format(row[0],row[1],row[2],row[3], row[4])
                print(l)
            _conn.commit()

        except Error as e:
            _conn.rollback()
            print(e)
        

        #need to add valid id safeguard using max p_id
        
        try:
            sql = """SELECT max(p_id)
                    from products"""
            cur = _conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            maxID = rows[0][0]
            _conn.commit

        except Error as e:
            _conn.rollback()
            print(e)
        
        print("\n")
        print("Please select the ID of the items you would like to purchase one by one. If you are done, press 0.\n")
        itemID = input()
        itemID = int(itemID)
        if itemID == 0:
            break
        elif itemID < 0:
            continue
        elif itemID > maxID:
            print("Please select a valid id\n")
            continue
        print("How many would you like?")
        itemCount = input()

        try:
            sql = """select p_onhand 
                    FROM products
                    WHERE p_id = ?"""
            args = [itemID]
            cur = _conn.cursor()
            cur.execute(sql, args) #execute defined command
            rows = cur.fetchall()
            stock = rows[0][0]
            _conn.commit()
        
        except Error as e:
            _conn.rollback()
            print(e)

        newstock = stock - itemCount
        if itemCount > stock:
            print("You are trying to purchase more items than we have in stock.\n Please enter a valid number.\n \n")
            continue
        
        try:
            sql = """select p_shipped 
                    FROM products
                    WHERE p_id = ?"""
            args = [itemID]
            cur = _conn.cursor()
            cur.execute(sql, args) #execute defined command
            rows = cur.fetchall()
            shipped = rows[0][0]
            _conn.commit()
        
        except Error as e:
            _conn.rollback()
            print(e)
        
        newShipped = shipped + itemCount
        

        try:
            sql = """SELECT p_id, p_name, p_price 
                    FROM products
                    WHERE p_id = ?
                    """
            args = [itemID]
            
            curr = _conn.cursor()
            curr.execute(sql, args) #execute defined command with input
            rows = curr.fetchall()
            
        

            while itemCount > 0:
                sqls = """INSERT INTO cart (
                        cart_id,
                        cart_name,  
                        cart_price
                        )
                        VALUES
                        (?,?,?)
                        """
                arg = [rows[0][0], rows[0][1], rows[0][2]]
                _conn.execute(sqls,arg)

                _conn.commit()
                itemCount = itemCount - 1
        except Error as e:
            _conn.rollback()
            print(e)


        try:
            sql = """update products
                    set p_onhand = ?
                    where p_id = ?""" 
            args = [newstock, itemID]
            _conn.execute(sql, args)
            _conn.commit()
        except Error as e:
            _conn.rollback()
            print(e)
        
        try:
            sql = """update products
                    set p_shipped = ?
                    where p_id = ?""" 
            args = [newShipped, itemID]
            _conn.execute(sql, args)
            _conn.commit()
        except Error as e:
            _conn.rollback()
            print(e)
        

def cartView(_conn):
    connect = _conn
    while 0 == 0:
        print("\n")
        print("\n")
        print("\n")
        print("This is your cart")
        print("\n")

        try:
            sql = """SELECT cart_id, cart_name, cart_price
                    FROM cart"""
            cur = _conn.cursor()
            cur.execute(sql) #execute defined command

            l = '{:>10} {:>16} {:>19}'.format("Id", "Name", "Price")
            print (l)
            rows = cur.fetchall()

            for row in rows:    
                l = '{:>10} {:>20} {:>15}'.format(row[0],row[1],row[2])
                print(l)
            _conn.commit()
            

        except Error as e:
            _conn.rollback()
            print(e)
        print("\n")
        print("\n")
        print("What would you like to do?\n")
        print("1: Get total\n")
        print("2: Finish and pay\n")
        print("3: Return to previous menu")
        choice = input()
        if choice == 1:
            try:
                sql = """SELECT SUM(cart_price) as Total
                        from cart"""
                cur = _conn.cursor()
                cur.execute(sql)
                l = '{:>10}'.format("Total")
                print (l)
                rows = cur.fetchall()

                for row in rows:  
                    l = '{:>1}'.format(row[0])
                    print "      $", l
                _conn.commit



            except Error as e:
                _conn.rollback()
                print(e)

        elif choice == 2:
            selectPayment(connect)
        elif choice == 3:
            break
        else :
            print("Invalid Entry, please retry\n")

#payment
def selectPayment(_conn):
    connect = _conn
    print("\n")
    print("Welcome to the payment menu. Your total is:")
    try:
        sql = """SELECT SUM(cart_price) as Total
                from cart"""
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:>10}'.format("Total")
        print (l)
        rows = cur.fetchall()

        for row in rows:  
            l = '{:>1}'.format(row[0])
            print "      $", l
        _conn.commit


    except Error as e:
        _conn.rollback()
        print(e)
    
    while 0 == 0:
        print("How would you like to pay?\n")
        print("1: Cashapp\n")
        print("2: Venmo\n")
        print("3: paypal\n")
        print("4: return to pevious menu without paying\n")
        choice = input()
        if choice == 1:
            payType = 'Cashapp'
            payForCart(connect, payType)
            break
        elif choice == 2:
            payType = 'Venmo'
            payForCart(connect, payType)
            break
        elif choice == 3:
            payType = 'Paypal'
            payForCart(connect, payType)
            break
        elif choice == 4:
            break
        else :
            print("Invalid entry, please retry\n")

def payForCart(_conn, payment):
    connect = _conn
    payType = payment

    print("Your total is: ")
    try:
        sql = """SELECT SUM(cart_price) as Total
                from cart"""
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:>10}'.format("Total")
        print (l)
        rows = cur.fetchall()
        price = rows[0][0]

        for row in rows:  
            l = '{:>1}'.format(row[0])
            print "      $", l
        _conn.commit


    except Error as e:
        _conn.rollback()
        print(e)

    print("\n")
    print("your order ID number is: ")

    try:
        sql = """Select MAX(o_id)
                from orders"""
         
        curr = _conn.cursor()
        curr.execute(sql) #execute defined command with input
        rows = curr.fetchall()

        ordernum = rows[0][0]
        ordernum = ordernum + 1
        print(ordernum)
        _conn.commit

    except Error as e:
        _conn.rollback()
        print(e)

    print("\n")
    print("Thank you for supporting our business :) ")

    try:
        sql = """SELECT count(*)
                FROM cart"""
        curr = _conn.cursor()
        curr.execute(sql) #execute defined command with input
        rows = curr.fetchall()

        amount = rows[0][0]
        
        _conn.commit


    except Error as e:
        _conn.rollback()
        print(e)

    
    try:
        sql = """SELECT count(distinct cart_id)
                FROM cart"""
        curr = _conn.cursor()
        curr.execute(sql) #execute defined command with input
        rows = curr.fetchall()

        i = rows[0][0]
        

        _conn.commit


    except Error as e:
        _conn.rollback()
        print(e)

    try:
        sql = """SELECT distinct cart_id
                FROM cart"""
        curr = _conn.cursor()
        curr.execute(sql) #execute defined command with input
        rows = curr.fetchall()

        listprod = [0] * i
        i = i - 1
        while i >= 0:
            listprod[i] = rows[i][0]
            i = i - 1
        

        _conn.commit


    except Error as e:
        _conn.rollback()
        print(e)

    today = date.today()
    d1 = today.strftime("%m/%d/%y")
    

    try:
        sql = """INSERT INTO orders (
                o_amount,
                o_price,  
                o_product,
                o_date,
                o_shipdate,
                o_recievedate,
                o_id
                )
                VALUES
                (?,?,?,?,?,?,?)
                """
        strprod = str(listprod)
        args = [amount, price, strprod, d1, d1, d1, ordernum]
        _conn.execute(sql,args)

        _conn.commit()

    except Error as e:
        _conn.rollback()
        print(e)
        
    try:
        sql = """Select MAX(pay_id)
                from payment"""
         
        curr = _conn.cursor()
        curr.execute(sql) #execute defined command with input
        rows = curr.fetchall()

        payid = rows[0][0]
        payid = payid + 1
        _conn.commit

       
    except Error as e:
        _conn.rollback()
        print(e)


    try:
        sql = """select o_amount
                from orders
                where o_id = ?"""
        args = [ordernum]
        curr = _conn.cursor()
        curr.execute(sql, args) #execute defined command with input
        rows = curr.fetchall()

        cartTotal = rows[0][0]
        

    except Error as e:
        _conn.rollback()
        print(e)


    if cartTotal == 0:
        try:
            sql = """INSERT INTO payment (
                    pay_id,
                    pay_type,  
                    pay_allowed,
                    pay_orderid
                    )
                    VALUES
                    (?,?,?,?)
                    """
            args = [payid, payType, 'no',ordernum]
            _conn.execute(sql,args)

            _conn.commit()

        except Error as e:
            _conn.rollback()
            print(e)
    else :

        try:
            sql = """INSERT INTO payment (
                    pay_id,
                    pay_type,  
                    pay_allowed,
                    pay_orderid
                    )
                    VALUES
                    (?,?,?,?)
                    """
            args = [payid, payType, 'yes',ordernum]
            _conn.execute(sql,args)

            _conn.commit()

        except Error as e:
            _conn.rollback()
            print(e)

    

    try:
        sql = """DELETE FROM cart"""
        _conn.execute(sql)
        _conn.commit

    except Error as e:
        _conn.rollback()
        print(e)

#account
def accountMenu(_conn):
    connect = _conn
    while 0 == 0:
        print("Would you like to create an account?\n")
        print("1: yes\n")
        print("2: no thank you, return to the previous menu\n")
        choice = input()
        if choice == 1:
            createAccount(connect)
        elif choice == 2:
            break
        else :
            print("Please choose a valid option\n")

def createAccount(_conn):
    connect = _conn
    first = raw_input("Please enter your first name: ")
    last = raw_input("Please enter your last name: ")
    email = raw_input("Please enter your email address: ")
    address = raw_input("Please enter your home address: ")
    print("Saving your account\n")
    print("...\n")
    print("...\n")
    print("...\n")
    print("...\n")
    print("...\n")

    try:
        sql = """select max(c_id)
                from customers;"""
        cur = _conn.cursor()
        cur.execute(sql)
        _conn.commit()
        rows = cur.fetchall()
        acctid = rows[0][0]
        acctid = acctid + 1

    except Error as e:
        _conn.rollback
        print(e)

    print "Your account number is: ", acctid
    print("\n Your full account information is listed below: \n")

    try:
        sql = """insert into customers(
                c_id,
                c_fname,
                c_lname,
                c_email,
                c_address
                ) 
                VALUES (?,?,?,?,?);
                """
        args = [acctid, first, last, email, address]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()

    except Error as e:
        _conn.rollback
        print(e)

    try:
        sql = """SELECT * 
                FROM customers
                where c_id = ?"""
        args = [acctid]
        cur = _conn.cursor()
        cur.execute(sql, args) #execute defined command

        l = '{:>10} {:>20} {:>20} {:>30} {:>30}'.format("ID", "Firstname", "Lastname", "email", "address")
        print (l)
        rows = cur.fetchall()

        for row in rows:    
            l = '{:>10} {:>20} {:>20} {:>30} {:>30}'.format(row[0],row[1],row[2],row[3],row[4])
            print(l)
        
        _conn.commit()

    except Error as e:
        _conn.rollback()
        print(e)
        
    
#owner interactions
def startAsOwner(_conn):
    connect = _conn
    while 0 == 0:
        print("Hello! Welcome back to your store. What would you like to do?\n")
        print("1: Manage products?\n")
        print("2: Manage Customers?\n")
        print("3: Manage Suppliers?\n")
        print("4: Return to main menu")
        choice = input("Enter number for choice: ")
        if choice == 1:
            whichProducts(connect)
        elif choice == 2:
            whichCustMenu(connect)
        elif choice == 3:
            whichSupMenu(connect)
        elif choice == 4:
            break
        else :
            print("Invalid Entry, please retry\n")
#products
def whichProducts(_conn):
    connect = _conn
    while 0 == 0:
        print("Which products do you want to manage?\n")
        print("1: Manage products?\n")
        print("2: Manage orders?\n")
        print("3: Manage categories?\n")
        print("4: Return to main menu")
        choice = input("Enter number for choice: ")
        if choice == 1:
            managePMenu(connect)
        elif choice == 2:
            manageOMenu(connect)
        elif choice == 3:
            manageCatMenu(connect)
        elif choice == 4:
            break
        else :
            print("Invalid Entry, please retry\n")



def managePMenu(_conn):
    connect = _conn
    while 0 == 0:
        print("Welcome to the product management menu. What would you like to do?\n")
        print("1: inspect products?\n")
        print("2: update products?\n")
        print("3: Add products?\n")
        print("4: Delete products?\n")
        print("5: Exit to previous menu \n")
        choice = input("Enter number for choice: ")
        if choice == 1:
            try:
                sql = """SELECT *
                        FROM products"""
                cur = _conn.cursor()
                cur.execute(sql) #execute defined command

                l = '{:>10} {:>30} {:>10} {:>10} {:>10} {:>10} {:>10} {:>20} {:>10}'.format("p_id", "p_name", "p_onhand", "p_made", "p_shipped", "p_size", "p_unitweight", "p_desc", "p_price")
                print (l)
                rows = cur.fetchall()
                

                for row in rows:    
                    l = '{:>10} {:>30} {:>10} {:>10} {:>10} {:>10} {:>10} {:>20} {:>10}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                    print(l)
                
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

        elif choice == 2:
            try:
                sql = """SELECT *
                        FROM products"""
                cur = _conn.cursor()
                cur.execute(sql) #execute defined command

                l = '{:>10} {:>30} {:>10} {:>10} {:>10} {:>10} {:>10} {:>20} {:>10}'.format("p_id", "p_name", "p_onhand", "p_made", "p_shipped", "p_size", "p_unitweight", "p_desc", "p_price")
                print (l)
                rows = cur.fetchall()
                

                for row in rows:    
                    l = '{:>10} {:>30} {:>10} {:>10} {:>10} {:>10} {:>10} {:>20} {:>10}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                    print(l)
                
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

            #print("Enter the item id for the product you would like to change\n")
            #productID = raw_input()
            #print("Enter the value you want to place into the table")
            #productValue = raw_input()
            print("Enter the number for which column you want to update starting with zero from left to right\n")
            column = input()
            if column == 0:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update products
                            set  p_id = ?
                            where p_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)

            if column == 1:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update products
                            set p_name = ?
                            where p_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            if column == 2:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update products
                            set p_onhand = ?
                            where p_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)

            if column == 3:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update products
                            set p_made = ?
                            where p_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            if column == 4:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update products
                            set p_shipped = ?
                            where p_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            if column == 5:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update products
                            set p_size = ?
                            where p_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            if column == 6:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update products
                            set p_unitweight = ?
                            where p_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            if column == 7:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update products
                            set p_desc = ?
                            where p_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            if column == 8:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update products
                            set p_price = ?
                            where p_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            


        elif choice == 3:
            print("Please enter the information for the item you want to add\n")
            pID = input("Please enter the id: ") 
            name = raw_input("Please enter the name: ")
            stock = input("Please enter the number in stock: ")
            made = input("Please enter the number made: ")
            shipped = input("Please enter the number shipped: ")
            size = input("Please enter the size: ")
            weight = input("Please enter the weight: ")
            desc = raw_input("Please enter the description: ")
            price = input("Please enter the price: ")

            try:
                sql = """INSERT INTO products(
                    p_id,
                    p_name,
                    p_onhand,
                    p_made,
                    p_shipped,
                    p_size,
                    p_unitweight,
                    p_desc, 
                    p_price
                    ) VALUES (?,?,?,?,?,?,?,?,?)
                    """
                
                args = [pID, name, stock, made, shipped, size, weight, desc, price]
                _conn.execute(sql, args)
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

        elif choice == 4:
            print("Please enter the id of the item you would like to delete\n")
            pID = input()

            try:
                sql = """Delete From products
                        where p_id = ?"""
                args = [pID]
                _conn.execute(sql,args)
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

        elif choice == 5:
            break
        else :
            print("Invalid Entry, please retry\n")

def manageOMenu(_conn):
    connect = _conn
    while 0 == 0:
        print("Welcome to the orders management menu. What would you like to do?\n")
        print("1: inspect orders?\n")
        print("2: update orders?\n")
        print("3: Add orders?\n")
        print("4: Delete orders?\n")
        print("5: Exit to previous menu \n")
        choice = input("Enter number for choice: ")
        if choice == 1:
            try:
                sql = """SELECT *
                        FROM orders"""
                cur = _conn.cursor()
                cur.execute(sql) #execute defined command

                l = '{:>10} {:>30} {:>10} {:>10} {:>10} {:>10} {:>10} {:>20}'.format("o_customer", "o_amount", "o_price", "o_product", "o_date", "o_shipdate", "o_recievedate", "o_id")
                print (l)
                rows = cur.fetchall()
                

                for row in rows:    
                    l = '{:>10} {:>30} {:>10} {:>10} {:>10} {:>10} {:>10} {:>20}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
                    print(l)
                
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

        elif choice == 2:
            try:
                sql = """SELECT *
                        FROM orders"""
                cur = _conn.cursor()
                cur.execute(sql) #execute defined command

                l = '{:>10} {:>30} {:>10} {:>10} {:>10} {:>10} {:>10} {:>20}'.format("o_customer", "o_amount", "o_price", "o_product", "o_date", "o_shipdate", "o_recievedate", "o_id")
                print (l)
                rows = cur.fetchall()
                

                for row in rows:    
                    l = '{:>10} {:>30} {:>10} {:>10} {:>10} {:>10} {:>10} {:>20}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
                    print(l)
                
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

            #print("Enter the item id for the product you would like to change\n")
            #productID = raw_input()
            #print("Enter the value you want to place into the table")
            #productValue = raw_input()
            print("Enter the number for which column you want to update starting with zero from left to right\n")
            column = input()
            if column == 0:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update orders
                            set  o_customer = ?
                            where o_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)

            if column == 1:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update orders
                            set o_amount = ?
                            where o_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            if column == 2:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update orders
                            set o_price = ?
                            where o_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)

            if column == 3:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update orders
                            set o_product = ?
                            where o_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            if column == 4:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update orders
                            set o_date = ?
                            where o_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            if column == 5:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update orders
                            set o_shipdate = ?
                            where o_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            if column == 6:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update orders
                            set o_recievedate = ?
                            where o_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            if column == 7:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update orders
                            set o_id = ?
                            where o_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            
            


        elif choice == 3:
            print("Please enter the information for the item you want to add\n")
            custnum = input("Please enter the customer number: ") 
            amount = input("Please enter the integer amount: ")
            price = input("Please enter the price: ")
            date = raw_input("Please enter the date: ")
            shipdate = raw_input("Please enter the ship date: ")
            recievedate = raw_input("Please enter the recieved date: ")
            oID = input("Please enter the order ID: ")
            

            try:
                sql = """INSERT INTO orders(
                    o_customer,
                    o_amount,
                    o_price,
                    o_date,
                    o_shipdate,
                    o_recievedate, 
                    o_id
                    
                    ) VALUES (?,?,?,?,?,?,?)
                    """
                
                args = [custnum, amount, price, date, shipdate, recievedate, oID]
                _conn.execute(sql, args)
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

        elif choice == 4:
            print("Please enter the id of the item you would like to delete\n")
            oID = input()

            try:
                sql = """Delete From orders
                        where o_id = ?"""
                args = [oID]
                _conn.execute(sql,args)
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

        elif choice == 5:
            break
        else :
            print("Invalid Entry, please retry\n")

def manageCatMenu(_conn):
    connect = _conn
    while 0 == 0:
        print("Welcome to the orders management menu. What would you like to do?\n")
        print("1: inspect categories?\n")
        print("2: update categories?\n")
        print("3: Add categories?\n")
        print("4: Delete categories?\n")
        print("5: Exit to previous menu \n")
        choice = input("Enter number for choice: ")
        if choice == 1:
            try:
                sql = """SELECT *
                        FROM categories"""
                cur = _conn.cursor()
                cur.execute(sql) #execute defined command

                l = '{:>10} {:>30} {:>10}'.format("cat_id", "cat_name", "cat_desc")
                print (l)
                rows = cur.fetchall()
                

                for row in rows:    
                    l = '{:>10} {:>30} {:>10}'.format(row[0],row[1],row[2])
                    print(l)
                
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

        elif choice == 2:
            try:
                sql = """SELECT *
                        FROM categories"""
                cur = _conn.cursor()
                cur.execute(sql) #execute defined command

                l = '{:>10} {:>30} {:>10}'.format("cat_id", "cat_name", "cat_desc")
                print (l)
                rows = cur.fetchall()
                

                for row in rows:    
                    l = '{:>10} {:>30} {:>10}'.format(row[0],row[1],row[2])
                    print(l)
                
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

            #print("Enter the item id for the product you would like to change\n")
            #productID = raw_input()
            #print("Enter the value you want to place into the table")
            #productValue = raw_input()
            print("Enter the number for which column you want to update starting with zero from left to right\n")
            column = input()
            if column == 0:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = raw_input()
                try:
                    sql = """update categories
                            set  cat_id = ?
                            where cat_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)

            if column == 1:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = raw_input()
                try:
                    sql = """update categories
                            set cat_name = ?
                            where cat_name = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            if column == 2:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update categories
                            set cat_desc = ?
                            where cat_desc = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)

            
            

        elif choice == 3:
            print("Please enter the information for the item you want to add\n")
            catID = input("Please enter the category ID number: ") 
            catname = raw_input("Please enter the category name: ")
            catdesc = raw_input("Please enter the category description: ")
            

            try:
                sql = """INSERT INTO categories(
                    cat_id, 
                    cat_name,
                    cat_desc
                    
                    ) VALUES (?,?,?)
                    """
                
                args = [catID, catname, catdesc]
                _conn.execute(sql, args)
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

        elif choice == 4:
            print("Please enter the id of the item you would like to delete\n")
            catID = input()

            try:
                sql = """Delete From categories
                        where cat_id = ?"""
                args = [catID]
                _conn.execute(sql,args)
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

        elif choice == 5:
            break
        else :
            print("Invalid Entry, please retry\n")

#customers

def whichCustMenu(_conn):
    connect = _conn
    while 0 == 0:
        print("Which customers do you want to manage?\n")
        print("1: Manage customers?\n")
        print("2: Manage payment?\n")
        print("3: Return to main menu")
        choice = input("Enter number for choice: ")
        if choice == 1:
            manageCustMenu(connect)
        elif choice == 2:
            managePayMenu(connect)
        elif choice == 3:
            break
        else :
            print("Invalid Entry, please retry\n")


def manageCustMenu(_conn):
    connect = _conn
    while 0 == 0:
        print("Welcome to the product management menu. What would you like to do?\n")
        print("1: inspect customers?\n")
        print("2: update customers?\n")
        print("3: Add customers?\n")
        print("4: Delete customers?\n")
        print("5: Exit to previous menu \n")
        choice = input("Enter number for choice: ")
        if choice == 1:
            try:
                sql = """SELECT *
                        FROM customers"""
                cur = _conn.cursor()
                cur.execute(sql) #execute defined command

                l = '{:>10} {:>20} {:>10} {:>30} {:>30}'.format("c_id", "c_fname", "c_lname", "c_email", "c_address")
                print (l)
                rows = cur.fetchall()
                

                for row in rows:    
                    l = '{:>10} {:>20} {:>10} {:>30} {:>30}'.format(row[0],row[1],row[2],row[3],row[4])
                    print(l)
                
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

        elif choice == 2:
            try:
                sql = """SELECT *
                        FROM customers"""
                cur = _conn.cursor()
                cur.execute(sql) #execute defined command

                l = '{:>10} {:>20} {:>10} {:>30} {:>30}'.format("c_id", "c_fname", "c_lname", "c_email", "c_address")
                print (l)
                rows = cur.fetchall()
                

                for row in rows:    
                    l = '{:>10} {:>20} {:>10} {:>30} {:>30}'.format(row[0],row[1],row[2],row[3],row[4])
                    print(l)
                
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

            #print("Enter the item id for the product you would like to change\n")
            #productID = raw_input()
            #print("Enter the value you want to place into the table")
            #productValue = raw_input()
            print("Enter the number for which column you want to update starting with zero from left to right\n")
            column = input()
            if column == 0:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = raw_input()
                try:
                    sql = """update customers
                            set  c_id = ?
                            where c_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)

            if column == 1:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update customers
                            set c_fname = ?
                            where c_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            if column == 2:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update customers
                            set c_lname = ?
                            where c_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)

            if column == 3:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update customers
                            set c_email = ?
                            where c_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            if column == 4:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update customers
                            set c_address = ?
                            where c_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            
            


        elif choice == 3:
            print("Please enter the information for the item you want to add\n")
            cID = input("Please enter the id: ") 
            fname = raw_input("Please enter the first name: ")
            lname = raw_input("Please enter the last name: ")
            email = raw_input("Please enter the email: ")
            address = raw_input("Please enter the home address: ")
            
            try:
                sql = """INSERT INTO customers(
                    c_id,
                    c_fname,
                    c_lname,
                    c_email,
                    c_address
                    ) VALUES (?,?,?,?,?)
                    """
                
                args = [cID, fname, lname, email, address]
                _conn.execute(sql, args)
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

        elif choice == 4:
            print("Please enter the id of the item you would like to delete\n")
            cID = input()

            try:
                sql = """Delete From customers
                        where c_id = ?"""
                args = [cID]
                _conn.execute(sql,args)
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

        elif choice == 5:
            break
        else :
            print("Invalid Entry, please retry\n")

def managePayMenu(_conn):
    connect = _conn
    while 0 == 0:
        print("Welcome to the payment management menu. What would you like to do?\n")
        print("1: inspect payments?\n")
        print("2: update payments?\n")
        print("3: Add payments?\n")
        print("4: Delete payments?\n")
        print("5: Exit to previous menu \n")
        choice = input("Enter number for choice: ")
        if choice == 1:
            try:
                sql = """SELECT *
                        FROM payment"""
                cur = _conn.cursor()
                cur.execute(sql) #execute defined command

                l = '{:>10} {:>30} {:>10} {:>10} {:>10}'.format("pay_customer", "pay_id", "pay_type", "pay_allowed", "pay_orderid")
                print (l)
                rows = cur.fetchall()
                

                for row in rows:    
                    l = '{:>10} {:>30} {:>10} {:>10} {:>10}'.format(row[0],row[1],row[2],row[3],row[4])
                    print(l)
                
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

        elif choice == 2:
            try:
                sql = """SELECT *
                        FROM payment"""
                cur = _conn.cursor()
                cur.execute(sql) #execute defined command

                l = '{:>10} {:>30} {:>10} {:>10} {:>10}'.format("pay_customer", "pay_id", "pay_type", "pay_allowed", "pay_orderid")
                print (l)
                rows = cur.fetchall()
                

                for row in rows:    
                    l = '{:>10} {:>30} {:>10} {:>10} {:>10}'.format(row[0],row[1],row[2],row[3],row[4])
                    print(l)
                
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

            #print("Enter the item id for the product you would like to change\n")
            #productID = raw_input()
            #print("Enter the value you want to place into the table")
            #productValue = raw_input()
            print("Enter the number for which column you want to update starting with zero from left to right\n")
            column = input()
            if column == 0:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update payment
                            set  pay_customer = ?
                            where pay_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)

            if column == 1:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update payment
                            set pay_id = ?
                            where pay_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            if column == 2:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update payment
                            set pay_type = ?
                            where pay_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)

            if column == 3:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update payment
                            set pay_allowed = ?
                            where pay_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            if column == 4:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update payment
                            set pay_orderid = ?
                            where pay_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            
            


        elif choice == 3:
            print("Please enter the information for the item you want to add\n")
            paycust = input("Please enter the customer id: ") 
            payID = input("Please enter the payment ID: ")
            paytype = raw_input("Please enter the type of payment: ")
            allowed = raw_input("Please enter yes or no for if the payment is allowed: ")
            orderID = input("Please enter the orderid associated with the payment: ")

            try:
                sql = """INSERT INTO payment(
                    pay_customer,
                    pay_id,
                    pay_type,
                    pay_allowed,
                    pay_orderid
                    ) VALUES (?,?,?,?,?)
                    """
                
                args = [paycust, payID, paytype, allowed, orderID]
                _conn.execute(sql, args)
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

        elif choice == 4:
            print("Please enter the id of the item you would like to delete\n")
            payID = input()

            try:
                sql = """Delete From payment
                        where pay_id = ?"""
                args = [payID]
                _conn.execute(sql,args)
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

        elif choice == 5:
            break
        else :
            print("Invalid Entry, please retry\n")

#suppliers

def whichSupMenu(_conn):
    connect = _conn
    while 0 == 0:
        print("Welcome to the supplier management menu. What would you like to do?\n")
        print("1: inspect suppliers?\n")
        print("2: update suppliers?\n")
        print("3: Add suppliers?\n")
        print("4: Delete suppliers?\n")
        print("5: Exit to previous menu \n")
        choice = input("Enter number for choice: ")
        if choice == 1:
            try:
                sql = """SELECT *
                        FROM suppliers"""
                cur = _conn.cursor()
                cur.execute(sql) #execute defined command

                l = '{:>10} {:>30} {:>10}'.format("s_id", "s_name", "s_product")
                print (l)
                rows = cur.fetchall()
                

                for row in rows:    
                    l = '{:>10} {:>30} {:>10}'.format(row[0],row[1],row[2])
                    print(l)
                
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

        elif choice == 2:
            try:
                sql = """SELECT *
                        FROM suppliers"""
                cur = _conn.cursor()
                cur.execute(sql) #execute defined command

                l = '{:>10} {:>30} {:>10}'.format("s_id", "s_name", "s_product")
                print (l)
                rows = cur.fetchall()
                

                for row in rows:    
                    l = '{:>10} {:>30} {:>10}'.format(row[0],row[1],row[2])
                    print(l)
                
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

            #print("Enter the item id for the product you would like to change\n")
            #productID = raw_input()
            #print("Enter the value you want to place into the table")
            #productValue = raw_input()
            print("Enter the number for which column you want to update starting with zero from left to right\n")
            column = input()
            if column == 0:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = input()
                try:
                    sql = """update suppliers
                            set  s_id = ?
                            where s_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)

            if column == 1:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = raw_input()
                try:
                    sql = """update suppliers
                            set s_name = ?
                            where s_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            if column == 2:
                print("Enter the item id for the product you would like to change\n")
                productID = input()
                print("Enter the value you want to place into the table")
                productValue = raw_input()
                try:
                    sql = """update suppliers
                            set s_product = ?
                            where s_id = ?""" 
                    args = [productValue, productID]
                    cur = _conn.cursor()
                    cur.execute(sql, args)
                    _conn.commit
            
                except Error as e:
                    _conn.rollback()
                    print(e)
            


        elif choice == 3:
            print("Please enter the information for the item you want to add\n")
            sID = input("Please enter the id: ") 
            sname = raw_input("Please enter the name: ")
            sprod = raw_input("Please enter the product name: ")
            

            try:
                sql = """INSERT INTO suppliers(
                    s_id,
                    s_name,
                    s_product
                   
                    ) VALUES (?,?,?)
                    """
                
                args = [sID, sname, sprod]
                _conn.execute(sql, args)
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

        elif choice == 4:
            print("Please enter the id of the item you would like to delete\n")
            sID = input()

            try:
                sql = """Delete From suppliers
                        where s_id = ?"""
                args = [sID]
                _conn.execute(sql,args)
                _conn.commit()

            except Error as e:
                _conn.rollback()
                print(e)

        elif choice == 5:
            break
        else :
            print("Invalid Entry, please retry\n")



#main
def main():
    database = r"Proj2data.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        
        createTables(conn)
        populateTables(conn)

        
    
    while 0 == 0:
        print("Welcome to the store. Please select your role\n")
        print("1: Customer\n")
        print("2: Owner\n")
        print("3: Quit\n")
        role = input("Enter number for role: ")
        if role == 1:
            startAsCust(conn)
        elif role == 2:
            startAsOwner(conn)
        elif role == 3:
            print("Thank you for coming, have a great day!")
            break
        else :
            print("Invalid Entry, please retry\n")
        

            

     
        
    

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
