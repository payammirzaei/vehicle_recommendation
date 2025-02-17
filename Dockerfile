# Use an official Python runtime as base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . .

# Create a virtual environment inside Docker (optional)
RUN python3 -m venv venv && source venv/bin/activate

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Command to run the application (Modify if needed)
CMD ["python3", "main.py"]
