# Use the official Python image as the base image
FROM python:3.11

# Set the working directory
WORKDIR /inventoryManager

# Copy the requirements file
COPY requirements.txt /inventoryManager/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files into the container
COPY . /inventoryManager/

# Expose the port your Django app runs on
EXPOSE 8000

# Command to run the Django application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]