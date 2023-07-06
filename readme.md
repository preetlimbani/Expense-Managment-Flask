# Expense Tracker API

Expense Tracker API is a Flask-based RESTful API that allows users to register, login, and manage their expenses.

## Features

- User registration and login
- Create, update, and delete expenses
- Retrieve a list of expenses for the authenticated user

## Technologies Used

- Flask
- Flask-RESTful
- Flask-PyMongo
- Flask-JWT-Extended
- Flask-Marshmallow
- MongoDB

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/preetlimbani/Expense-Managment-Flask.git
    ```
2. Installing requirments:
   ```shell
   pip install -r requirements.txt
   ```

3. Set up the configuration:

   Create a .env file in the root directory.
   
   Add the following environment variables to the .env file:
   ```shell
   SECRET_KEY=<your-secret-key>
   MONGO_URI=<your-mongodb-uri>
   ```
   Replace <your-secret-key> with a secret key of your choice. Replace <your-mongodb-uri> with the URI of your MongoDB database.


4. Run the application:

   ```shell
   python run.py
   ```