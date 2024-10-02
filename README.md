# Django Project Setup and Running Instructions

## Requirements

- Python 3.11+
- Docker (optional but recommended)
- Docker Compose (optional but recommended)

## 1. Setting Up the Development Environment

### Using `venv` (Virtual Environment)

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On **Windows**:

      ```bash
      venv\Scripts\activate
      ```

    - On **macOS/Linux**:

      ```bash
      source venv/bin/activate
      ```

4. Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply the database migrations:

    ```bash
    python manage.py migrate
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the application at `http://127.0.0.1:8000/`.

---

## 2. Setting Up and Running with Docker

### Docker

1. **Build the Docker image**:

    ```bash
    docker build -t <your-image-name> .
    ```

2. **Run the Docker container**:

    ```bash
    docker run -d -p 8000:8000 <your-image-name>
    ```

    This will start the Django application on port 8000.

3. Access the application at `http://127.0.0.1:8000/` in your web browser.

### Docker Compose (Alternative)

1. If you're using Docker Compose, you can simplify the setup:

    - First, make sure your `docker-compose.yml` file is set up correctly.
  
2. **Build and start the services**:

    ```bash
    docker-compose up --build
    ```

3. **Run the migrations**:

    ```bash
    docker-compose exec web python manage.py migrate
    ```

4. Access the application at `http://127.0.0.1:8000/` in your browser.

---

## 3. Testing

To run the tests in your Django project, use the following command:

```bash
python manage.py test

