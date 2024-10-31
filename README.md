# AOScribe

## System - Map / Page Images / Outline

<img src="./images/mapofsite.png" alt="Home Page" width="400">

- First journey into Django framework using python.  

- Below is the current state in final Alpha stage with some code and database configuration remains.

- Below are the current screen shots of the application this is alpha not finish product
  
- So be nice reviewing it or comments or use - IT'S NOT COMPLETE DON'T CLONE -

### Home Page

<img src="./images/home.PNG" alt="Home Page" width="200">

### Contact

<img src="./images/contact.PNG" alt="Contact Page" width="200">

### Login

<img src="./images/login.PNG" alt="Login Page" width="200">

### Register

<img src="./images/register.PNG" alt="Register Page" width="200">

### Dashboard

<img src="./images/dashboard.PNG" alt="Dashboard Page" width="200">

### Approved Registered users Area

### Profile

<img src="./images/profile.PNG" alt="Profile Page" width="200">

### Message

<img src="./images/message.PNG" alt="Message Page" width="200">

### Data

<img src="./images/data.PNG" alt="Data Page" width="200">

### Logout
  
- Logout button returns to the home screen on the unauthorized side of the site

### Dashboard

<img src="./images/dashboard1.png" alt="Dashboard Member Access Page" width="200">
<img src="./images/dashboard2.png" alt="Dashboard Member Access Page" width="200">

### Process

<img src="./images/process1.png" alt="Processing Page" width="200">
<img src="./images/process2.png" alt="Processing Page" width="200">

## Django Admin

<img src="./images/admin.png" alt="Django Admin Access Page" width="200">

- pages in development

# Read Me <Draft Copy>

### database readme <draft separate file>

### Fast Track

-----------------------------------------

```bash
sudo apt update && sudo apt upgrade
sudo apt install python3 python3-pip
sudo apt install python3-venv

mkdir my_django_project
cd my_django_project
python3 -m venv myenv
source myenv/bin/activate

pip install django
django-admin startproject myproject .
python manage.py migrate

python manage.py runserver
python manage.py createsuperuser
```

- Reference Url: <http://127.0.0.1:8000/admin>

``` bash
hostname -I
ifconfig
ALLOWED_HOSTS = ['192.168.x.x', 'localhost', '127.0.0.1']
python manage.py runserver 0.0.0.0:8000
```

- Reference Url: <http://192.168.x.x:8000>

``` bash
sudo ufw allow 8000
sudo ufw restart

sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL <https://download.docker.com/linux/ubuntu/gpg> | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] <https://download.docker.com/linux/ubuntu> $(lsb_release -cs) stable"
sudo apt update
sudo apt install docker-ce

sudo snap install ffmpeg

ngrok http 8000
```

- goto to ### Step 2: Dockerize the Django Project

  - Setting up Django on Ubuntu involves several key steps, from installing Python and setting up a virtual environment to installing Django itself and setting up your project. Here’s a detailed outline to help you through the process:

### 1. Prepare Your System

- Update and Upgrade Packages:
  Before you begin, make sure your system’s package list and packages are up-to-date.

  ```bash
  
  sudo apt update && sudo apt upgrade
  
  ```

- Install Python and Pip:
  Django is a Python web framework, so you need Python installed along with pip, which is Python’s package installer.

  ```bash

  sudo apt install python3 python3-pip

  ```

### 2. Set Up a Virtual Environment

- Install Virtual Environment:
  It’s best practice to use a virtual environment for Python projects. This isolates your project’s dependencies from the system’s Python.

  ```bash

  sudo apt install python3-venv

  ```

- Create and Activate a Virtual Environment:
  Navigate to the directory where you want your Django project to reside, or create a new directory.

  ```bash

  mkdir my_django_project
  cd my_django_project
  python3 -m venv myenv
  source myenv/bin/activate

  ```

### 3. Install Django

- Install Django Using Pip:
  With your virtual environment activated, install Django.

  ```bash

  pip install django

  ```

### 4. Start a Django Project

- Create a New Django Project:
  Once Django is installed, you can create a new project with the `django-admin` command.

  ```bash

  django-admin startproject myproject .

  ```

- Structure of Your Project:
  This command creates a new directory in your project folder with the necessary Django files, including `manage.py`, which is used for managing the project.

### 5. Configure the Database

- Default Database Setup:
  Django uses SQLite by default. You can start with SQLite and later migrate to another database system like PostgreSQL or MySQL if needed.

- Migrate the Database:
  Apply the initial database migrations with the following command:

  ```bash

  python manage.py migrate

  ```

### 6. Start the Development Server

- Run the Server:
  Test your setup by running Django’s development server.

  ```bash

  python manage.py runserver

  ```

  This command starts a web server on <http://127.0.0.1:8000> where you can see your new project.

### 7. Access the Admin Panel

- Create a Superuser:
  Django includes a built-in admin panel that you can use to manage data. Create a superuser to access it.

  ```bash

  python manage.py createsuperuser

  ```

- Access the Admin Panel:
  Once the superuser is created, you can access the admin panel by navigating to <http://127.0.0.1:8000/admin>.

### 8. Additional Configuration (Optional)

- Static Files Configuration:
  As you prepare for production, ensure you configure static files correctly. This involves setting `STATIC_ROOT` and running `python manage.py collectstatic`.

- Security Settings:
  Before deploying, adjust settings like `DEBUG`, `ALLOWED_HOSTS`, and secure your application with HTTPS.

### 9. Ready for Development

- Develop Your Application:
  Start adding apps to your project, developing your models, views, and templates according to your project requirements.

This outline should help you set up Django on Ubuntu effectively. Each step is crucial to ensuring that your environment is both functional and prepared for further development and eventual deployment.

To configure your Django project to be accessible from other devices on your local network, you need to make adjustments to your Django settings and run the server on an IP that is accessible within your local network. Here’s how to do it step-by-step:

### 1. Find Your Local IP Address

First, you need to find the IP address of the machine where your Django project is running. This IP should be accessible within your local network. You can find your local IP address by running the following command in your terminal:

```bash

hostname -I

```

Or you can use `ifconfig` (you might need to install it using `sudo apt install net-tools`):

```bash

ifconfig

```

Look for an output similar to `192.168.x.x` under the appropriate network interface (usually `eth0` for Ethernet or `wlan0` for Wi-Fi).

### 2. Configure Django Settings

Edit your Django project’s settings file (`myproject/settings.py`). You need to allow your host machine’s IP address or use a wildcard to allow all hosts during development. However, be cautious with wildcards and never use them in production:

```python

ALLOWED_HOSTS = ['192.168.x.x', 'localhost', '127.0.0.1']

```

Replace `192.168.x.x` with your actual local IP address.

### 3. Run Django Development Server on Local Network

By default, Django’s development server runs on localhost (`127.0.0.1`). To make your server accessible from other machines on your local network, you need to run it bound to your local IP address or `0.0.0.0` (which means all available IPv4 addresses on the local machine):

```bash

python manage.py runserver 0.0.0.0:8000

```

Using `0.0.0.0` allows connections from any computer in your network to your Django development server.

### 4. Access the Django Server from Another Device

On another device in the same network, open a web browser and enter:

```plaintext

http://192.168.x.x:8000

```

Replace `192.168.x.x` with the IP address you found earlier. You should see your Django project’s homepage.

### 5. Security and Firewall Considerations

Ensure that your firewall settings allow traffic on the port you're using (default is 8000). If you’re using `ufw`, you might need to allow this port:

```bash

sudo ufw allow 8000
sudo ufw restart

```

### 6. Testing

Make sure to test the access from multiple devices within your network to ensure everything is configured correctly. If there are issues, double-check your `ALLOWED_HOSTS` settings and ensure your device’s firewall is not blocking incoming connections.

### Additional Tips

- Security: This setup is suitable for development and testing purposes within a secure local network. For production environments, more comprehensive security measures should be implemented.
- Performance: Running the development server for multiple users can be slow. Consider using a more robust WSGI server like Gunicorn if you need to handle more traffic even in a development setting.

By following these steps, your Django development server will be accessible from any device within your local network, facilitating development and collaborative testing.

Running Django in a Docker container is a great way to ensure consistency across different environments. Here’s how to set up Docker to run your Django project from a server. This setup involves creating a Dockerfile, a docker-compose.yml file, and configuring your Django project appropriately.

### Step 1: Install Docker

First, ensure Docker is installed on your server. If it's not already installed, you can install Docker using the following commands:

```bash

sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install docker-ce

```

### Step 2: Dockerize the Django Project

#### Create a Dockerfile

Navigate to your Django project directory and create a `Dockerfile`. This file describes the Docker image and how your application should be run inside the container.

```Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Run the application on port 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]

```

#### Create a `requirements.txt`

List all Python packages your Django project needs in a `requirements.txt` file:

```plaintext

Django>=3.2,<4.0
gunicorn
# Any other libraries you need

```

#### Create a docker-compose.yml File

For easy management of your Docker container, including settings for production and development environments, create a `docker-compose.yml` file:

```yaml

version: '3.8'

services:
  web:
    build: .
    command: gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    environment:
      - DEBUG=0
      - SECRET_KEY=YourSecretKeyHere
      - DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

```

Adjust `DJANGO_ALLOWED_HOSTS` to include your server's IP address or domain if known.

- DJANGO_ALLOWED_HOSTS=['localhost','127.0.0.1','::1','192.168.1.220']

### Step 3: Build and Run the Container

Navigate to the directory containing your `docker-compose.yml` file and run:

```bash

sudo apt install docker-compose  
cd my_django_project
sudo docker-compose up --build

```

This command builds the image from your Dockerfile and starts running your Django application.

### Step 4: Access Your Django Application

Once your Docker container is running, you can access your Django application by navigating to `http://<server-ip>:8000` on your browser, where `<server-ip>` is the IP address or domain of your server.

### Step 5: Additional Configuration (Optional)

For production environments, consider the following additional settings:

- Databases: Configure a production-grade database like PostgreSQL.
- Static Files: Manage static files and media with services like AWS S3, or set up Nginx as a reverse proxy to serve static files.
- Security: Ensure `DEBUG` is set to `False` and use environment variables to manage sensitive information securely.
- Performance: Optimize your Docker image and manage resources with Docker-compose settings.

This guide should help you get your Django project up and running inside a Docker container on any server.
