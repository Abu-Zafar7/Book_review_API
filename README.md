## Clone this repository

``$ git clone <repository-url>``

## Navigate into the project directory
  
``$ cd Book_review_API``

## Create a virtual environment
  
``$ python -m venv venv``

## Activate the virtual environment
- On Windows
  
``$ venv\Scripts\activate``

## On macOS/Linux
  
``$ source venv/bin/activate``

## Install required Python packages
  
``$ pip install -r requirements.txt``

## Use the default sqlite database for development

## Apply database migrations
  
``$ python manage.py migrate``

## Create a superuser to interact with the database

``$ python manage.py runserver``

## Run the local development server
  
``$ python manage.py runserver``

Access the API at: http://127.0.0.1:8000/

## Below are the endpoints to access the API

> POST `api/register`
```json
{
  "username": "your_username",
  "password": "your_password"
}






