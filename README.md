# Vendor Management System with Performance Metrics

## Hi there !

Here I have designed and developedVendor Management System with Performance Metrics. This web application developed using the Django and Django REST Framework, MySQL database, and REST API for efficient vendor management and performance tracking and  token-based authentication for secure API .This design is purely coded myself no copied content.

Thanks !

## Features

 * Common Features 
  **Vendor Management**: Create, update, and delete vendor information.
  **Performance Metrics**: Track and analyze vendor performance through key metrics.
  **RESTful API**: Expose RESTful APIs for seamless integration with other systems.
  **Token-based authentication** : It is a common and secure method for authenticating          	users in web applications, especially when building RESTful APIs.
- **MySQL Database**: Utilize MySQL for robust and scalable data storage.

 ##Advance Features 🔥

 **On-Time Delivery Rate**

 **Quality Rating Average**

 **Average Response Time**

 **Fulfilment Rate**

 **Vendor Performance**

## Requirements

- Python 3.11
- Django 5.0
- MySQL
- Django REST framework
- rest_framework.authtoken
- Additional Python packages
- Postman
     


## Installation

* Import this project into your IDE
* Create new Database in Mysql and set name as 'vendor_details' 

## Database Connection

* I have used following 👇 data for database connection
    * DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME':'vendor_details',
            'USER':'root',
            'PASSWORD':'root',
            'HOST':'localhost',
            'PORT':'3306',
    }
}

* Then go terminal
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser

## How to Run 
py manage.py runserver
Go to http://127.0.0.1:8000/admin/
Fill the all models data and Access the application at http://127.0.0.1:8000/
After open the url u can Access The All Data By Given unique vendor id In Input 
   
##API Endpoints
The API endpoints are available at http://127.0.0.1:8000/api/:

api/vendors/<str:vendor_id>/performance/', 
api/vendors/',
api/vendors/<int:vendor_id>/', 
api/purchase_orders/',
api/purchase_orders/<int:po_id>/'
api/purchase_orders/<int:po_id>/acknowledge/'

Due to global authetication to CBV's u can Test These All API's in 'Postman' with Token based authentication

## About

Hello! 👋 I'm Satyam Das, a passionate Python developer with a strong foundation in web development. I recently completed comprehensive Python and Django courses from Naresh IT, honing my skills in both the Python programming language and the Django web framework and Databases.

Connect with me on [LinkedIn](www.linkedin.com/in/satyam-das-43b0b3224) to discuss potential collaborations, share insights, or explore exciting opportunities in the world of Python development!

Email : gsatyam.das@gmail.com

Your feedback is highly valuable!.I welcome your thoughts, suggestions, and bug reports. Your input helps me improve the Vendor Management System and make it more robust and user-friendly.
