# Cement Strength Display App

This is a simple Flask application that displays cement strength data. The data is stored in a PostgreSQL database.

## Getting Started

Follow these steps to run the application locally.

### Prerequisites

- Python (version specified in `runtime.txt` or `requirements.txt`)
- PostgreSQL

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/kevykibbz/concrete-strength.git
    cd concrete-strength
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database:

    - Create a PostgreSQL database.
    - Update the database connection URI in the `.env` file.

4. Apply database migrations:

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

### Running the Application

Run the Flask application:

```bash
python run.py
```

The app will be accessible at `http://localhost:5000`.

## Deploying to Heroku

Follow the steps mentioned in the [Heroku Deployment Section](#heroku-deployment).

## Project Structure

- `app`: Contains the main Flask application.
- `migrations`: Stores database migration files.
- `templates`: HTML templates for the views.
- `config.py`: Configuration settings for the app.
- `run.py`: Script to run the application.

## Contributing

Feel free to contribute to this project. Create a fork, make your changes, and submit a pull request.
