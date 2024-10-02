# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables to ensure Python output is not buffered
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install the dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port the app runs on (default Django port is 8000)
EXPOSE 8000

# Set the entrypoint to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
