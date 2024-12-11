**Clone this repository**

``$ git clone <repository-url>``

- Navigate into the project directory
``$ cd Book_review_API``

# Create a virtual environment
``$ python -m venv venv``

# Activate the virtual environment
# On Windows
``$ venv\Scripts\activate``

# On macOS/Linux
``$ source venv/bin/activate``

# Install required Python packages
``$ pip install -r requirements.txt``

# Apply database migrations
``$ python manage.py migrate``

# Run the local development server
``$ python manage.py runserver``

Access the API at: http://127.0.0.1:8000/
