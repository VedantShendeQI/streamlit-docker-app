FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

# 🔥 IMPORTANT
ENV PORT=8080

EXPOSE 8080

# 🔥 USE PORT VARIABLE (this is key fix)
CMD ["streamlit", "run", "app1.py", "--server.port=8080", "--server.address=0.0.0.0"]