FROM python:3.9-slim

WORKDIR /app

# Add environment variables for better Flask configuration
ENV FLASK_APP=app.py \
    FLASK_ENV=production \
    PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create volume for persistent data
VOLUME ["/app/data"]

EXPOSE 5000

# Modified command to ensure proper binding
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
