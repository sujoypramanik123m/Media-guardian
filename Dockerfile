# Use the base Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all bot files
COPY . .

# Expose the port (used by the dummy HTTP server)
EXPOSE 8000

# Set environment variable for unbuffered output (for logs)
ENV PYTHONUNBUFFERED=1

# Correct command to run the script
CMD ["python", "bot.py"]
