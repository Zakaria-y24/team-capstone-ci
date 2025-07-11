# Team Name: SU25_Team1

This is the team repository for <SU25_Team1>

## Project

To design and develop a fully functional, visually appealing, and secure online e-store that allows customers to browse and purchase pre-made decorative resin blocks. The goal is to create an intuitive user experience that showcases seasonal, color-themed, and botanical designs, while providing a seamless checkout process and administrative product management capabilities. The Resin Bloom project includes the planning, design, development, testing, and deployment of a web-based retail application. The application will be built using Django (Python) for the backend, PostgreSQL for the database, and HTML/CSS/JavaScript with Bootstrap for the frontend. It will not support custom orders, but instead feature a curated inventory of ready-made resin items categorized by color, season, or motif.

### Project Name
Resin Bloom

### Project Description  
Resin Bloom is an e-store specializing in decorative resin blocks. These are pre-made items—sealed botanical designs, seasonal motifs, and color-based themes—that users can browse and purchase via a simulated checkout process. 

In Scope:

Customer-facing website with product catalog and search/filter features.

Product pages with item descriptions, prices, and images.

Simulated shopping cart and checkout process (no real payment integration).

User account registration and login functionality.

Admin dashboard for managing products (CRUD operations).

Backend database for storing product, order, and user data.

Responsive design for mobile and desktop devices.

Integration of seasonal themes and automated catalog updates.

## Team

Team details follow

### 495 Students 

Zakaria Yabarow - Team Manager

Krishna Patel - Team Lead

### 394 Students

Tyler Steiner - Senior Software Developer

Chasten Watkins - Senior Software Developer

### 294 Students

Erno Kuhinko - Junior Software Developer

Luis Espinal - Junior Software Developer

## Prerequisites

•	Backend: Python (Django, possibly Flask for specific microservices)

•	Database: PostgreSQL

•	Frontend: HTML, CSS, Bootstrap, JavaScript

•	Tools: Visual Studio Code, GitHub for version control and collaboration

## Set Up and Installation

Details on how to set up the project follow.

1.	Required Software for the Project:
   
•	Development Tool – Visual Studio Code 

•	Backend – Python, Django

•	Version control – Git 

•	Database system – PostgreSQL 

During installation:

• Setup all applications to their default values.

• Uncheck Stack Builder

• Save the password you create for all applications (Priority - pgAdmin4)

________________________________________
2.	Setting Up PostgreSQL Database
   
•	Open pgAdmin4 (PostgreSQL’s database management tool).

•	In the left panel, click the Servers dropdown.

•	Right-click on Databases, then select Create → Database.

•	Set the database name to: resinbloom_db.

•	Click Save.

________________________________________
3.	 Cloning the Project Ensure you have VS Code, Python, and Git installed before proceeding.
   
•	Open VS Code.

•	Open the terminal (Ctrl + ` in VS Code). 

•	Use Git Bash Terminal

•	Run the following command to clone the repository: git clone https://github.com/FranklinUniversityCompSciPracticum/SU25_Team1.git

•	Navigate into the project directory: cd SU25_Team1

DO NOT CREATE A NEW FLODER USING ONEDRIVE!
________________________________________
 4.   Setting Up the Virtual Environment
    
•	To create a virtual environment using VS Code terminal: 

     For Powershell: python -m venv venv
   
     For Git Bash (Windows): py -m venv venv
   
•	Activate the virtual environment: source venv/Scripts/activate

•	Install required dependencies: pip install -r requirements.txt

________________________________________
5.   Creating the .env File
   
•	Create a .env file in the project root directory (inside SU25_Team1, next to manage.py).

•	Open .env and add the following content:

   •	DB_NAME=resinbloom_db
   
   •	DATABASE_USER=postgres

   •	DB_PASSWORD=your-postgres-password

   (Replace your-postgres-password with actual values)
   
   •	DB_HOST=localhost

   •	DB_PORT=5432
________________________________________
6.   Running Database Migrations
   
•	Apply the database migrations: python manage.py migrate

•	Create a superuser (save the credentials)

________________________________________
7.   Running the Development Server
   
•	Start the Django development server: python manage.py runserver

•	Use Ctrl + Click to navigate to http://127.0.0.1:8000/

•	Message displayed for successful setup: The install worked successfully! Congratulations! 


8. Loading Sample Products
To populate the database with sample resin products:

•	Make sure the media/product_images/ folder exists and contains the product images.

•	Run the following script from the project root: python scripts/load_products.py

•	This will add several products to the database with matching image files. If any image file is missing, that product will be skipped


test




