# **CAR RENTAL SYSTEM**

## INTRODUCTION

In today's rapidly evolving environment, it is essential for service-oriented enterprises to emphasize both efficiency and customer satisfaction. For a car rental agency, dependence on manual documentation can result in delays and an increased likelihood of errors. Consequently, our organization is in the process of developing a comprehensive Car Rental System.
The primary objective of this system is to automate the rental process, enhance operational efficiency, and improve the customer experience. Our forthcoming Car Rental System will supplant outdated manual practices with an automated solution, thereby decreasing the time needed for rental transactions and reducing the potential for mistakes.
This system will feature a user-friendly interface for both vehicle reservations and returns, ensuring a seamless experience for our clients. Key functionalities will encompass effective data management for customer and vehicle records, an intuitive booking interface, and a robust vehicle management module.
Furthermore, the system will integrate secure pricing and billing features, along with advanced reporting and analytics tools to provide valuable insights for the business.
The Car Rental System will be architected to facilitate the company's growth, incorporating elements such as user roles, access control, integration capabilities, and scalability while ensuring adherence to relevant regulations.
Through the deployment of this Car Rental System, we aspire to elevate our service standards, foster customer loyalty, and position our company as a frontrunner in the car rental sector. Our car rental system is meticulously designed to showcase our proficiency in creating a user-friendly and efficient software platform for car rentals.
This initiative is specifically tailored to meet the demands of both individuals and businesses in search of affordable and dependable car rental services. Recognizing the increasing demand for car rentals.
we have developed a system that simplifies and streamlines the rental process for our customers. Our platform provides a diverse selection of vehicles.

## Installation and Configuration

- Operating System: Linux/Windows/MacOS
- Database: MySQL version 8.0 
- Programming Language: Python (version 3.12)

## Installation Procedure

Clone the Repository:

```bash
git clone https://github.com/username/car-rental-system.git  cd car-rental-system
```

## Install Dependencies

Utilize Python's package manager
``bash  pip install mysql_connector_python  ``

## Database Configuration

Establish a MySQL database and modify the DATABASES settings accordingly

## Current System Overview

- The organization currently manages rentals through manual paperwork
- This method results in significant time consumption and lacks a database for future verification.
- There is no mechanism for providing feedback to either the administrator or the users.

## Enhanced System Overview

- The newly implemented system functions entirely in a digital format.
- It encompasses features such as user information management, rapid access to car details, and the collection of customer feedback during the login process.
- This system caters to tourism and travel services, allowing users to easily submit requests.
- It is recognized as one of the most user-friendly software solutions for establishing an online car rental service.
- The interface is designed for ease of use and straightforward implementation.
- With minimal infrastructure requirements, it proves to be a cost-effective solution.

## Features

#### ADMIN LOGIN 

#### CUSTOMER LOGIN

#### EXIT

## *ADMIN LOGIN*

The administrative dashboard provides an extensive summary of the system's present condition, including the total number of available vehicles, active rentals, registered users, and pending bookings.

### *LIST OF CUSTOMERS*
- This feature enables the administrator to access a comprehensive list of all customers registered within the system.


- Upon selection, the system gathers and presents the information of all customers.
The information may encompass customer names, contact details, and any other pertinent data stored in the system.

- The administrator can utilize this functionality to examine customer information, confirm customer identities, or oversee the roster of active users in the system.
### VIEW CUSTOMER BOOKINGS
- This feature allows access to customer booking information.
- *EXISTING BOOKING:* The administrator can retrieve the booking details for a particular customer by inputting the customer's mobile number. If a booking is found, the system will present pertinent information, including the rented vehicle, rental dates, and current status. If no booking is found, the system will inform the administrator with a message stating "No Customer Booking."
- *VIEW ALL BOOKINGS:* The administrator has the ability to view all bookings made by customers within the system. This encompasses active, completed, and potentially cancelled bookings.
- This feature is really important for keeping track of how customers are using the rental service. It aids in managing the fleet and getting a better grasp of what customers prefer.  
### VIEW PAYMENTS
- This option lets the admin check payment records linked to customer bookings.  
- *VIEW PAYMENT FOR EXISTING BOOKING:* The admin can input a customer’s mobile number to see payments made for a particular booking. If a payment exists, details like the amount, date, and payment method will show up. If there’s no payment recorded, the system will say, "No Customer Payment Made."  
- *VIEW ALL PAYMENTS:* The admin can look at all payments made by customers, no matter the booking.  
- This option is vital for managing finances within the system, helping the admin keep track of rental income, monitor pending payments, and make sure all transactions are accurately logged.

### *ADD CAR*

- This feature is accessible through the Admin login. It allows for the entry of newly added vehicles into the database.
- The administrator is responsible for inputting all relevant details of the vehicle based on the specified parameters.

### *DELETE CAR*
- This feature allows the administrator to eliminate a vehicle from the rental inventory.
- The administrator identifies the vehicle to be removed, typically by inputting a unique identifier like the registration number. 
- After removal, the vehicle will no longer be accessible for rental within the system. 
- This capability is beneficial for excluding vehicles that are unavailable for rent due to reasons such as damage, sale, or retirement from the fleet.
### *LIST OF CARS*
- This feature presents a comprehensive list of all vehicles available in the rental inventory.
- The system gathers and showcases all vehicles along with their specifications, including make, model, year, registration number, and current availability status.
- Administrators can utilize this function to oversee the fleet, verify vehicle availability, and efficiently manage the inventory.

### *LOGOUT*
- This feature logs the administrator out of the system and directs them back to the main menu.
- Upon selection, the active admin session is concluded, and the system reverts to the primary menu, allowing the administrator to either log in again or exit the system.
- This feature is crucial for maintaining security, as it regulates admin access to sensitive functionalities and ensures that sessions are appropriately terminated.

## *CUSTOMER LOGIN*

The Customer Login Menu offers members various options to oversee their accounts and access important information. The available menu options include.
#### ADD NEW CUSTOMER
#### *EXISTING CUSTOMER*
## *ADD NEW CUSTOMER*

This functionality is designed to onboard new customers into the system. When a customer visits in person or interacts online, their personal information—including name, address, phone number, and email—is gathered and input into the system. This procedure guarantees that the customer is incorporated into the database and is prepared to rent vehicles.

## *EXISTING CUSTOMERS*
 This feature enables you to view and manage the information of customers who are already registered in the system. It is especially beneficial for reviewing customer profiles, updating contact details, examining rental history, or responding to specific customer queries. This functionality ensures that customer records remain accurate and current.

## *VIEW CARS AVAILABILITY*
The system provides an up-to-date overview of the rental cars on offer. This functionality displays the status of each vehicle, highlighting those that are currently rented and those that are available for new bookings. It enables staff to efficiently assess inventory and deliver prompt information to customers regarding availability.
## *RENT A CAR & MAKE PAYMENT*
The primary function of the system is to facilitate vehicle rentals. After a customer chooses a car, the system assists the user in defining the rental duration and handling the payment process. This guarantees that the vehicle is designated as rented within the system, and the transaction is securely documented.

## *RETURN CAR*
Upon the return of a rented vehicle, this functionality is utilized to update the system appropriately. It designates the car as available for subsequent rentals and completes any outstanding transactions related to the return. This procedure is crucial for preserving an accurate inventory and guaranteeing that vehicles are prepared for the next customer.
## *LOGOUT*
Upon finishing all tasks, this feature enables the user to safely log out of the system. Exiting the session guarantees that all actions are recorded and that the session is closed correctly, thereby safeguarding against unauthorized access.