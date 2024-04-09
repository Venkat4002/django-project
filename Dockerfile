# Use an official Python runtime as the base image
FROM python:3.10

# Install MySQL client
#RUN apt-get update && apt-get install -y default-mysql-client

#Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Set the working directory in the container
WORKDIR /app

#Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

#Copy the rest of the application code
COPY . .

#Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
