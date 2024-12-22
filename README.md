# My FastAPI Application

This is a simple FastAPI application that serves as a basic example for API development.

## Requirements

- Python 3.12 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository:**

   If you haven't cloned the repository yet, run the following command:

   ```bash
   git clone https://github.com/clemmzzy

Navigate to your project directory:

   cd your-repo


2. **Create and activate a virtual environment(optional but recommended):**
    For Windows:
        python -m venv env_name
        
        **Activate Environment:**

        .\env_name\Scripts\activate


3. **Install dependencies:**
    Make sure you have all the required dependencies by running:

        pip install -r requirements.txt

    If you don't have a requirements.txt file, you can create one by running:

        pip freeze > requirements.txt

    Alternatively, you can manually install FastAPI and Uvicorn with:

        pip install fastapi uvicorn

 4. **Running the Application:**

    Once the dependencies are installed, you can run the application using uvicorn:

    uvicorn main:app --reload

    This will start the FastAPI application in development mode with live reloading. You can now visit the app in your browser at:

        http://127.0.0.1:8000   ----------- (https://localhost:8000)

    You can access the interactive API documentation by visiting:

    Swagger UI: http://127.0.0.1:8000/docs  ---------   (https://localhost:8000/docs)        



