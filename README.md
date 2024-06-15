# Django SSE Alert System

This project is a Django-based web application that demonstrates how to implement a real-time alert system using Server-Sent Events (SSE). The alerts are broadcasted to connected clients in real-time, providing an interactive and responsive user experience.

## Features

- Real-time alerts using Server-Sent Events (SSE)
- RESTful API for creating alerts
- Responsive and user-friendly frontend
- Dockerized for easy setup and deployment

## Technologies Used

- Django
- Django REST Framework
- django-eventstream
- Docker & Docker Compose
- HTML, CSS, JavaScript

## Installation

### Using Docker

1. **Clone the repository**:

   ```sh
   git clone https://github.com/JuanSebastianGB/sse-single-event.git
   cd sse-single-event
   ```

2. **Create a `.env` file**:
   Create a `.env` file in the project root directory with the necessary environment variables.

3. **Build and run the containers**:

   ```sh
   docker-compose up --build
   ```

4. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:8000/`.

### Without Docker

1. **Clone the repository**:

   ```sh
   git clone https://github.com/JuanSebastianGB/sse-single-event.git
   cd sse-single-event
   ```

2. **Create a virtual environment**:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations**:

   ```sh
   python manage.py migrate
   ```

5. **Create a superuser**:

   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```sh
   python manage.py runserver
   ```

## Docker Configuration

### Dockerfile

```dockerfile
FROM python:3.12-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
ENTRYPOINT [ "/app/entrypoint.sh" ]
```

### run with docker compose

```sh
docker-compose up --build -d
```
