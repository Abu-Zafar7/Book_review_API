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

```bash
curl -X POST <base_url>/api/token/ \
-H "Content-Type: application/json" \
-d '{
  "username": "your_username",
  "password": "your_password"
}'

curl -X GET <base_url>/api/reviews/ \
-H "Authorization: Bearer your_access_token"

[
  {
    "id": 1,
    "title": "Book Title",
    "review": "This book was amazing!",
    "rating": 5,
    "author": "Reviewer Name"
  },
  {
    "id": 2,
    "title": "Another Book",
    "review": "Not as good as the first.",
    "rating": 3,
    "author": "Another Reviewer"
  }
]


