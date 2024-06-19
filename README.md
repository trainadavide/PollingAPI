# PollingAPI
PollingAPI is an API for creating and participating in polls.
The API is built using Django and DRF, and Railway was used for deployment. You can try it here: https://pollingapi.up.railway.app/
## What you can do with PollingAPI
* Create polls: You can create new polls with a title and options.
* View polls: You can see the details of the polls you have created.
* Delete polls: You can delete polls that you no longer need.
* View responses.
* View user profiles: to see all the polls they have created.

# How to Setup and Run PollingAPI Locally

## Prerequisites
- Python 3.10
- pip

## Steps
1. Clone the repository to your local machine using git:
    ```
    git clone https://github.com/yourusername/PollingAPI.git
    ```
    Replace `yourusername` with your actual GitHub username.

2. Navigate to the project directory:
    ```
    cd PollingAPI
    ```

3. Create a virtual environment:
    ```
    python -m venv env
    ```

4. Activate the virtual environment:
    - On Windows:
        ```
        .\env\Scripts\activate
        ```
    - On Unix or MacOS:
        ```
        source env/bin/activate
        ```

5. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

6. Apply the migrations:
    ```
    python manage.py migrate
    ```

7. Run the server:
    ```
    python manage.py runserver
    ```

Now, you can access the API locally at `http://127.0.0.1:8000/`.