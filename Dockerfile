#Use python base image
From python:3.12-slim

#Set working directory
WORKDIR /app

#Copy requirements
COPY requirements.txt .
 
#install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Copy application files
COPY . .

#Expose application port
EXPOSE 5000

#Start Flask application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
