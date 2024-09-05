import mysql.connector
from getpass import getpass
from datetime import datetime

# Database Connection


class Database:
    def __init__(self,localhost,root,password, db):
        self.conn = mysql.connector.connect(
            host=localhost,
            user=root,
            password=password,
            database=db
        )
        self.cursor = self.conn.cursor()

    def execute(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.conn.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

# Admin Class


class Admin:
    def __init__(self, db):
        self.db = db

# ADD NEW CAR

    def add_car(self):
        Rego = input("Enter Car Rego: ")
        Brand = input("Enter Car Brand: ")
        Model = input("Enter Car Model: ")
        Year = input("Enter Car Rego Year: ")
        RentPerDay = input("Enter Car Rent Per Day: ")
        Availability = input("Enter Car Availabliity - Yes/No: ")

        query = "INSERT INTO Cars (Rego,brand,model,year,rent_per_day,available) VALUES (%s,%s,%s,%s,%s,%s)"
        self.db.cursor.execute(query, (Rego,Brand,Model,Year,RentPerDay,Availability))
        self.db.conn.commit()
        print(f"Car '{Model}' added successfully.")

# DELETE EXISTING CAR
    def delete_car(self):
        Rego = input("Enter Car Rego to delete: ")
        query = "DELETE FROM Cars WHERE Rego = %s"
        self.db.cursor.execute(query, (Rego,))
        self.db.conn.commit()
        print(f"Car '{Rego}' Car deleted successfully.")

# SHOW ALL AVAILABLE CARS

    def list_cars(self):
        query = "SELECT * FROM Cars"
        self.db.cursor.execute(query)
        cars = self.db.fetchall()
        print("Available Cars:")
        for car in cars:
            print(car)



# Customer Class


class Customer:
    def __init__(self, db):
        self.db = db

# ADD A NEW CUSTOMER

    def add_customer(self):
        name = input("Enter customer name: ")
        phone = input("Enter customer phone: ")
        email = input("Enter customer email: ")
        query = "INSERT INTO Customers (name, phone, email) VALUES (%s, %s, %s)"
        self.db.execute(query, (name, phone, email))
        print("Customer added successfully.")

# SHOW LIST OF CUSTOMERS

    def list_customers(self):
        query = "SELECT * FROM Customers"
        self.db.cursor.execute(query)
        customers = self.db.fetchall()
        if customers:
            print("Customers:")
            for customer in customers:
                print(customer)
        else:
            print("No Customers Available.")

# SHOW ALL CUSTOMER BOOKINGS

    def view_customer_bookings(self):
        print("1. Existing Booking")
        print("2. View All Bookings")
        choice = input("Enter choice: ")
        if choice == '1':
            mobile = input("Enter Mobile NO: ")
            query = "SELECT Bookings.booking_id, Cars.model, Customers.phone, Bookings.start_date, Bookings.end_date FROM Bookings INNER JOIN Cars ON Bookings.car_id = Cars.car_id INNER JOIN Customers ON Customers.customer_id = Bookings.customer_id WHERE Customers.phone = %s"

            self.db.cursor.execute(query, (mobile,))
            bookings = self.db.fetchall()
            if bookings:
                print("Customer Bookings:")
                for booking in bookings:
                    print(booking)
            else:
                print("No Customer Booking.")

        elif choice == '2':
            query = "SELECT Bookings.booking_id, Cars.model, Customers.phone, Bookings.start_date, Bookings.end_date FROM Bookings INNER JOIN Cars ON Bookings.car_id = Cars.car_id INNER JOIN Customers ON Customers.customer_id = Bookings.customer_id"
            self.db.cursor.execute(query)
            bookings = self.db.fetchall()
            if bookings:
                print("Customer Bookings:")
                for booking in bookings:
                    print(booking)
            else:
                print("No Customer Booking.")

# VIEW CUSTOMER BOOKINGS

    def view_mybookings (self, custid):
        query = "SELECT Bookings.booking_id, Cars.model, Customers.phone, Bookings.start_date, Bookings.end_date FROM Bookings INNER JOIN Cars ON Bookings.car_id = Cars.car_id INNER JOIN Customers ON Customers.customer_id = Bookings.customer_id WHERE Customers.customer_id = %s"
        self.db.cursor.execute(query, (custid,))
        bookings = self.db.fetchall()
        if bookings:
            print("Customer Bookings:")
            for booking in bookings:
                print(booking)
        else:
            print("No Customer Booking.")

# VIEW PAYMENTS FOR THE RENTED CAR

    def view_payments(self):
        print("1. View Payment for an existing booking")
        print("2. View All Payments")
        choice = input("Enter Choice: ")
        if choice == '1':
            mobile = input("Enter Mobile NO: ")
            query = "SELECT Cars.model, Payments.payment_id, Customers.customer_id, Payments.booking_id, Payments.amount, Payments.payment_date FROM Payments INNER JOIN Bookings ON Payments.booking_id = Bookings.booking_id INNER JOIN Cars ON Bookings.car_id = Cars.car_id INNER JOIN Customers ON Customers.customer_id = Bookings.customer_id WHERE Customers.phone = %s"

            self.db.cursor.execute(query, (mobile,))
            payments = self.db.fetchall()
            if payments:
                print("Customer Payments:")
                for payment in payments:
                    print(payment)
            else:
                print("No Customer Payment Made.")

        elif choice == '2':
            query = "SELECT Cars.model, Payments.payment_id, Customers.customer_id, Payments.booking_id, Payments.amount, Payments.payment_date FROM Payments INNER JOIN Bookings ON Payments.booking_id = Bookings.booking_id INNER JOIN Cars ON Bookings.car_id = Cars.car_id INNER JOIN Customers ON Customers.customer_id = Bookings.customer_id"
            self.db.cursor.execute(query)
            payments = self.db.fetchall()
            if payments:
                print("Customer Payments:")
                for payment in payments:
                    print(payment)
            else:
                print("No Customer Payments.")

# VIEW AVAILABLE CARS

    def view_cars(self):
        query = "SELECT * FROM Cars WHERE available = 'Yes'"
        self.db.cursor.execute(query)
        cars = self.db.fetchall()
        if cars:
            print("Available Cars:")
            for car in cars:
                print(car)
        else:
            print("No Cars Available.")

# TO RENT A CAR

    def rent_car(self, custid):
        Rego = input("Enter Rego: ")
        query1 = "SELECT * FROM Cars WHERE Rego = %s"
        self.db.cursor.execute(query1, (Rego,))
        cars1 = self.db.fetchall()
        if cars1:
            print("Car Available with Rego")
            for car_detail in cars1:
                print(car_detail)
            query = "SELECT car_id FROM Cars WHERE Rego = %s"
            self.db.cursor.execute(query, (Rego,))
            cars = self.db.fetchone()
            amount_query = "SELECT rent_per_day FROM Cars WHERE Rego = %s"
            self.db.cursor.execute(amount_query, (Rego,))
            car_rent = self.db.fetchone()
            for rent in car_rent:
                print(rent)
            start_date = input("Enter start date to Rent(YYYY-MM-DD): ")
            end_date = input("Enter Return date (YYYY-MM-DD): ")
            book_now = input("Do you want to book this car: Yes/No: ")
            if book_now == "Yes":
                for car_id in cars:
                    pay_now = input("Do you want to make a Payment: Yes/No: ")
                    if pay_now == "Yes":
                        query2 = "INSERT INTO Bookings (customer_id, car_id, start_date, end_date) VALUES (%s, %s, %s, %s)"
                        var = (custid, car_id, start_date, end_date)
                        self.db.cursor.execute(query2, var)
                        self.db.conn.commit()
                        query3 = "SELECT booking_id FROM Bookings WHERE customer_id = %s and car_id =%s"
                        self.db.cursor.execute(query3, (custid, car_id))
                        booking = self.db.fetchone()
                        for booking_id in booking:
                            print("CAR RENTED SUCCESSFULLY.")
                            for amount in car_rent:
                                self.return_car("No", Rego)
                                self.make_payment(booking_id, amount)
                    else:
                        print("Booking Cancelled, Please Choose another Car.")
            else:
                print("Choose another Car.")

        else:
            print("No Cars Available.")
       
# RETURN A CAR FOR THE GIVEN REGO

    def return_car(self, Is_Available, Rego):
        query = "UPDATE Cars SET available = %s WHERE Rego = %s"
        self.db.cursor.reset()
        self.db.cursor.execute(query, (Is_Available, Rego))
        self.db.conn.commit()
        print("CAR RENTURNED SUCCESSFULLY.")

# MAKE PAYMENT FOR THE BOOKING

    def make_payment(self, booking_id, amount):
        payment_date = datetime.now().strftime('%Y-%m-%d')
        query2 = "INSERT INTO payments (booking_id, amount, payment_date) VALUES (%s, %s, %s)"
        var = (booking_id, amount, payment_date)
        self.db.cursor.reset()
        self.db.cursor.execute(query2, var)
        self.db.conn.commit()
        print("CAR PAYMENT SUCCESSFUL.")

# Rental System Class


class RentalSystem:

    def __init__(self):
        self.db = Database("localhost","root","Peppapig@123","systembase")
        self.admin = Admin(self.db)
        self.customer = Customer(self.db)

# DETAILS FOF ADMIN MENU

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. List of Customers")
            print("2. View Customer Bookings")
            print("3. View Payments")
            print("4. Add Car")
            print("5. Delete Car")
            print("6. List of Cars")
            print("7. Logout")
            choice = input("Enter choice: ")
            if choice == '1':
                self.customer.list_customers()
            elif choice == '2':
                self.customer.view_customer_bookings()
            elif choice == '3':
                self.customer.view_payments()
            elif choice == '4':
                self.admin.add_car()
            elif choice == '5':
                self.admin.delete_car()
            elif choice == '6':
                self.admin.list_cars()
            elif choice == '7':
                break

# DETAILS OF CUSTOMER MENU

    def customer_menu(self):
        while True:
            print("\nCustomer Menu:")
            print("1. Add New Customer")
            print("2. Existing Customers")
            choice = input("Enter choice: ")
            if choice == '1':
                self.customer.add_customer()
            elif choice == '2':
                name = input("Enter Customer username: ")
                phone = input("Enter Phone Number: ")
                query = "SELECT customer_id FROM customers WHERE name = %s AND phone = %s"
                self.db.cursor.execute(query, (name, phone))
                customers = self.db.fetchone()
                for customer in customers:
                    if customer:
                        self.ExistingCustomer_menu(customer)
                    else:
                        print("Invalid login credentials.")
                        self.customer_menu()

# EXISTING CUSTOMER DETAILS MENU

    def ExistingCustomer_menu(self, custid):
        while True:
            print("\nExisting Customer Menu:")
            print("1. View Cars Availability")
            print("2. Rent a Car & Make Payment")
            print("3. Return Car")
            print("4. My Bookings")
            print("5. Logout")
            choice = input("Enter choice: ")
            if choice == '1':
                self.customer.view_cars()
            elif choice == '2':
                self.customer.rent_car(custid)
            elif choice == '3':
                Rego = input("Enter Rego: ")
                query5 = "SELECT * FROM Cars inner join bookings a on a.car_id = Cars.car_id where Cars.Rego = %s and a.customer_id = %s"
                self.db.cursor.execute(query5, (Rego, custid))
                cars1 = self.db.fetchone()
                if cars1:
                    print("Car Booking Available with Rego")
                    for car_detail in cars1:
                        print(car_detail)
                Is_Available = input("Do you want to Return This Car: Yes/No: ")
                if Is_Available == "Yes":
                    self.customer.return_car(Is_Available, Rego)
            elif choice == '4':
                self.customer.view_mybookings(custid)
            elif choice == '5':
                break

# LOIN DETAILS

    def login(self):
        while True:
            print("\nWelcome to Car Rental System")
            print("1. Admin Login")
            print("2. Customer Login")
            print("3. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                username = input("Enter admin username: ")
                password = input("Enter admin password: ")
                query = "SELECT * FROM admin WHERE username = %s AND password = %s"
                self.db.cursor.execute(query,(username,password))
                admin = self.db.fetchall()
                if admin:
                    self.admin_menu()
                else:
                    print("Invalid login credentials.")
            elif choice == '2':
                self.customer_menu()
            elif choice == '3':
                print("Thank you for using Car Rental System!")
                break


# Run the Rental System

if __name__ == "__main__":
    rental_system = RentalSystem()
    rental_system.login()
