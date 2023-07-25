# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and any other dependencies
RUN pip install --no-cache-dir flask

# Expose the port on which Flask will run
EXPOSE 9090

# Set the default message environment variable
ENV PRINT_MESSAGE="Printing Service 1"

# Command to run the Flask application
CMD ["python", "app.py"]
