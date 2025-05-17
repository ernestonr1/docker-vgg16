FROM python:3.11-slim

# Install system deps
RUN apt-get update && apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev

# Set workdir
WORKDIR /app

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Start API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
