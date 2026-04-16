# 1. Base image (Stable and Slim)
FROM python:3.11-slim

# 2. Environment variables set karna
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Work directory create karna
WORKDIR /code

# 4. Requirements copy aur install karna
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /code/requirements.txt

# 5. App aur Models folder copy karna
COPY ./app /code/app
COPY ./models /code/models

# 6. API ko expose karna
EXPOSE 8000

# 7. Start command (Uvicorn)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]