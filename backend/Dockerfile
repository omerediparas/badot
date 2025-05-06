FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies needed for mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set Flask environment variables
ENV FLASK_APP=app:create_app
ENV FLASK_ENV=development  

# Copy the rest of the app (adjust if necessary)
COPY ./app /app

# Expose the port
EXPOSE 5000

# Run Flask app
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
