# Use an official PyTorch image as a parent image
FROM pytorch/pytorch:latest

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory to the location of manage.py
WORKDIR /app/image_classification

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]