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

> POST `api/user/register/`  to register a new user

> POST `api/user/login/` to obtain a JWT token

> POST `api/user/token/refresh/` to refresh the JWT token

> GET `api/books/` to get the list of books with their details

> GET `api/books/<id>/` to retrieve details of a specific book

> POST `api/books/` to post about a new book, only admin and authenticated users can post a book. Users aren't allowed to post a book

> GET `api/reviews/` lists all the reviews

> GET `api/reviews/<id>/` retrieves a specific review

> POST `api/reviews/` a user can post a review about a book with book, rating and comment as the json fields.

> PUT `api/reviews/<id>/` updates a review of a given user, only a user can update their reviews

> DELETE `api/reviews/<id>/` deletes a review of a user, only a user can delete their reviews

> GET `api/recommendations/?genre=fiction&user_rating=4` recommends a book based on author, rating, genre - you have to put the search query in the recommendations

> GET `/api/books/?ordering=average_rating` returns books in order of average rating

> GET `api/books/?search=bookname` returns details of the book search in the query

# USE POSTMAN TO CHECK THE ENDPOINTS






