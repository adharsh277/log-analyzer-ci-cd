# Use official Python image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the analyzer script and logs
COPY analyzer/ analyzer/
COPY logs/ logs/
COPY reports/ reports/

# Run the analyzer when the container starts
CMD ["python", "analyzer/analyze.py"]
