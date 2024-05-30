# Expense Tracker Web Application

This web application is designed to track expenses and generate downloadable reports in Excel and PDF formats. It also allows users to upload an Excel sheet and provides charts of the expenses.
  
  Table of Contents
  
      •	Overview
      •	Features
      •	Tech Stack
      •	Setup Instructions
      •	Usage
      •	License
      
  Overview

    The Expense Tracker web application helps users manage their expenses by tracking them, generating reports, and visualizing data through charts. It supports currency conversion and allows for seamless integration and deployment using Docker.
  Features

    •	Expense Tracking: Track your daily expenses and categorize them.
    •	Report Generation: Generate downloadable reports in Excel and PDF formats.
    •	Excel Upload: Upload an Excel sheet to visualize expenses through charts.
    •	Currency Conversion: Convert expenses to different currencies using JavaScript.
    
  Tech Stack

    •	Python
    •	Django: Web framework for building the application.
    •	JavaScript: Used for currency conversion and dynamic changes in the frontend.
    •	Docker: Used to containerize the application for easy deployment.
    
  Setup Instructions

    To set up the project locally, follow these steps:
    1.	Clone the repository:
        git clone https://github.com/yourusername/expense-tracker.git
        cd expense-tracker
        
    2.	Install the required dependencies:
        pip install -r requirements.txt
        
    3.	Run the Django migrations:
        python manage.py migrate
        
    4.	Start the Django development server:
        python manage.py runserver
        
    5.	Dockerize the application (optional):
          o	Build the Docker image:
              docker build -t expense-tracker .
          o	Run the Docker container:
              docker run -p 8000:8000 expense-tracker
              
  Usage
  
      To use the web application, follow these steps:
      1.	Access the application: Open your browser and go to http://127.0.0.1:8000/.
      2.	Track Expenses:
            o	Add your daily expenses through the web interface.
            o	Categorize each expense for better tracking.
      3.	Generate Reports:
            o	Download reports in Excel or PDF format.
      4.	Upload Excel Sheet:
            o	Upload an Excel sheet to visualize your expenses through charts.
  License
  
    This project is licensed under the MIT License.

