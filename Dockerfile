# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .

# Install poppler-utils for pdfplumber (via pdf2image internally)
RUN apt-get update && \
    apt-get install -y poppler-utils && \
    pip install --no-cache-dir -r requirements.txt

# Copy all source code into the container
COPY . .

# Set default command
CMD ["python", "titles.py"]
