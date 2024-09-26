# POTATO-Take-Home-Task

How to Use the System:
Clone the Repository:

bash

git clone https://github.com/Abhirajp595/twitter-analytics.git
cd twitter-analytics
Install Dependencies:

bash

pip install -r requirements.txt
Run Flask API:

bash

python app.py
Query the API: Access the API at http://localhost:5000/search?term=music to analyze tweets containing the term "music."

Optional Docker Setup: Build and run with Docker:

bash

docker build -t twitter-analytics .
docker run -p 5000:5000 twitter-analytics
Key Design Choices:
Flask API for simple HTTP query handling.
Pandas for efficient data manipulation.
Docker for easy deployment and environment consistency.
