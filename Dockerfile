# # Use the official Python image from the Docker Hub
# FROM python:3.13-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy all files from the current directory to the working directory in the container
# COPY . .

# # Install any needed dependencies specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Make port 5000 available to the world outside this container
# EXPOSE 5001

# # Run the Flask application
# CMD ["python", "./apps/main.py"]


# Gunakan Python 3.13 sebagai base image
FROM python:3.13-slim

# Install dependensi sistem yang diperlukan untuk psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy all files from the current directory to the working directory in the container
COPY . .

# Install dependencies dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Hapus cache pip setelah instalasi untuk mengurangi ukuran image
RUN rm -rf /root/.cache/pip

# Membuat port 5001 tersedia untuk aplikasi
EXPOSE 5001

# Jalankan aplikasi Flask
CMD ["python", "./apps/main.py"]

