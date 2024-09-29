# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install poetry
RUN pip install --no-cache-dir poetry

# Copy only the pyproject.toml and poetry.lock files (if it exists)
COPY pyproject.toml poetry.lock* ./

# Install dependencies using poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Set environment variables (if needed)
# ENV VARIABLE_NAME=value

# Run the application using poetry
CMD ["poetry", "run", "python", "main.py"]
