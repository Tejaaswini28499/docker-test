# Use official Python image from Docker Hub
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy local files into container
COPY app.py .

# Run the Python script when container starts
CMD ["python", "app.py"]
