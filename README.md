# Content Upload and Review System

This project is a **Content Upload and Review System** that allows users to upload CSV files containing movie data, view movies with pagination, filter movies by release year and language, and sort movies by various fields, such as release date and vote average.

## Features
- **Upload CSV**: Upload a CSV file to populate the database with movie data.
- **View Movies**: View uploaded movies with pagination, filtering, and sorting options.
- **Filtering**: Filter movies by release year and language.
- **Sorting**: Sort movies by release date and vote average.
- **Pagination**: View a paginated list of movies.

---

## Prerequisites

1. **Python** should be installed on your machine.
2. **Flask** and **other dependencies** as mentioned in the `requirements.txt` file.
3. **Postman** (optional - testing API endpoints).

---

## Setup and Installation

### Step 1: Clone the Repository
Clone this repository to your local machine.

### Step 2: Create a Virtual Environment
create a virtual environment to better manage dependencies.
`python -m venv venv`


Activate the virtual environment:
- On **Windows**: Activate it using `venv\Scripts\activate`.
- On **macOS/Linux**: Activate it using `source venv/bin/activate`.

### Step 3: Install Dependencies
Install all required dependencies using `pip install -r requirements.txt`.



### Step 4: Running the Flask Application
run the application using the command: `flask run`:

By default, the app will run on `http://127.0.0.1:5000`.(The IMDB HomePage appears).


---

## API Endpoints

1. **Upload CSV**: `POST /upload`
   Upload a CSV file to populate the movie database.

2. **View Movies**: `GET /movies`
   Retrieve a paginated list of movies, with filtering by release year and language, and sorting by release_date and vote_average.

---

## Postman Collection
You can find a ready-to-use Postman collection to test the API in the `postman/Content_Upload_Review_System_API.postman_collection.json` file.

---

## Testing the Application

1. Upload a CSV: Use the `POST /upload` endpoint to upload a CSV file containing movie data.
2. View Movies: Use the `GET /movies` endpoint to view and filter movies by various criteria.

---

## Conclusion

We have successfully created the **Content Upload and Review System**, allowing for seamless movie data management, including CSV uploads, filtering, sorting, and pagination through the provided API endpoints.

---
## Problem Statement

https://shorturl.at/W8UyW


