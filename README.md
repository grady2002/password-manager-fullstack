# Password Manager

Password Manager CRUD web application made in React frontend and Python backend.

# Usage Instructions

## Database Setup

- Import the `query.sql` into your database client dashboard

## Frontend

    cd client
    npm install
    npm start

## Backend (Linux / Mac)

    cd server
    pip3 install -r requirements.txt
    python3 main.py

## Backend (Windows)

    cd server
    pip install -r requirements.txt
    python main.py

## Database (ONLY FOR NON XAMPP USERS)

Non XAMPP users either need to create a database manually or use the `query.sql` file to create the database. If creating a database manually use the following code in your SQL console.

```sql
create database passwordManager;
use passwordManager;
create table auth (
    id int auto_increment primary key,
    username varchar(255) unique,
    pass varchar(255),
    site varchar(255)
);
insert into auth (username, pass, site) values ("admin", "admin", "example.com")
```
