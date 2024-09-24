# Use an official Python runtime as a parent image
FROM python:3.10.12

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE myproject.settings

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Django project code
COPY . /my_django_project
WORKDIR /my_django_project

# Run the Django application
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]