# Base Python image
FROM python:3.10-slim

# Working directory set karo
WORKDIR /app

# Requirements copy karo
COPY requirements.txt .

# Dependencies install karo
RUN pip install --no-cache-dir -r requirements.txt

# Bot ke saare files copy karo
COPY . .

# Port expose karo (jo dummy HTTP server use karta hai)
EXPOSE 8000

# Environment variable for unbuffered output (logs ke liye)
ENV PYTHONUNBUFFERED=1

# Sahi command jo script ko run kare
CMD ["python", "bot.py"]
