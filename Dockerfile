# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . .

# Install the required packages if requirements.txt exists
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Expose the port the app runs on
EXPOSE 8000

# Set environment variables (if needed)
# ENV VARIABLE_NAME=value

# Run the application
CMD ["python", "app.py"]
