FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libssl-dev \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy files
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Expose Streamlit default port
EXPOSE 8501

# Run Streamlit
ENV STREAMLIT_SERVER_ENABLECORS=false
CMD ["streamlit", "run", "gemini-code-1780037330332.py", "--server.port=8501", "--server.address=0.0.0.0"]
