# Workout-Planner
Workout-Planner is a Django RESTful API designed to manage personalized workout plans for users. It provides a comprehensive system for creating, updating, and retrieving workout plans, exercises, and user profiles.

## Features
**User Management:** Allows users to register, log in, and manage their profiles.   
**Workout Plans:** Create personalized workout plans with specific exercises, sets, repetitions, and goals.  
**Exercise Catalog:** A catalog of predefined exercises to choose from when creating workout plans.  
**Security:** Implements JWT authentication for secure user authentication.  
**API Documentation:** Integrated Swagger documentation for easy API exploration.  

## Installation
#### Clone the repository:
```bash
git clone https://github.com/guraspy/Workout-Planner.git
cd Workout-Planner
```
#### Create a virtual environment:
```bash
python -m venv venv
```
#### Activate the virtual environment:
- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```
#### Install the dependencies:
```bash
pip install -r requirements.txt
```
#### Create migrations:
```bash
python manage.py makemigrations users
python manage.py makemigrations exercises
python manage.py makemigrations workouts
```
#### Apply migrations:
```bash
python manage.py migrate
```
#### Populate initial exercises:
```bash
python manage.py populate_exercises
```
#### Start the development server:
```bash
python manage.py runserver
```


## API Endpoints
### The API will be accessible at localhost:8000
#### User Endpoints:

- POST /api/register:  Register a new user.
- POST /api/login: Log in and obtain JWT token.
- POST /api/logout: Log out and invalidate JWT token.
- GET /api/user/<id>: Retrieve user profile by ID.
#### Exercise Endpoints:
- GET /api/exercises: List all exercises.
- GET /api/exercises/<id>: Retrieve a specific exercise by ID.
#### Workout Plan Endpoints:
- GET /api/workout-plans: List all workout plans for the authenticated user.
- POST  /api/workout-plans: Create a new workout plan.
- GET /api/workout-plans/<id>: Retrieve a specific workout plan by ID.
- PUT  /api/workout-plans/<id>: Update a workout plan by ID.
- DELETE  /api/workout-plans/<id>: Delete a workout plan by ID.

## Authentication
The API uses JWT (JSON Web Tokens) for user authentication. To obtain a JWT token, you can make a POST request to the /api/login endpoint with your credentials. The token will then be included in cookies for subsequent requests to access protected endpoints. To invalidate JWT token, you can make POST request to the /api/logout.


## API Documentation using Swagger:
You can view the API documentation for the endpoints using drf-spectacular. These will provide an interactive API documentation where you can explore the endpoints, test them, and view schemas.

To view the Swagger documentation, navigate to:
http://localhost:8000/api/schema/docs/
