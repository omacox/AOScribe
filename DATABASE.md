# Database Setup

## Setup of MySQL

    - See below (this database readme is in draft)

- log into mysql

```bash
sudo mysql -u mainuser -p
```

root

- <password>

mainuser

- <password>

```sql

CREATE DATABASE aoscribe;

USE aoscribe;

CREATE TABLE userslog (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(45) UNIQUE NOT NULL,
    password VARCHAR(20) NOT NULL,
    pin VARCHAR(10) NOT NULL,
    email VARCHAR(60) UNIQUE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    date_joined DATETIME DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE mainapp_customuser
ADD COLUMN elevenlabs_api_key VARCHAR(255) NULL,
ADD COLUMN assemblyai_api_key VARCHAR(255) NULL,
ADD COLUMN openai_api_key VARCHAR(255) NULL;

CREATE TABLE `auth_user` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `password` varchar(128) NOT NULL,
    `last_login` datetime(6) DEFAULT NULL,
    `is_superuser` tinyint(1) NOT NULL,
    `username` varchar(150) NOT NULL UNIQUE,
    `first_name` varchar(150) NOT NULL,
    `last_name` varchar(150) NOT NULL,
    `email` varchar(254) NOT NULL UNIQUE,
    `is_staff` tinyint(1) NOT NULL,
    `is_active` tinyint(1) NOT NULL,
    `date_joined` datetime(6) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `django_admin_log` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `action_time` datetime(6) NOT NULL,
    `object_id` longtext,
    `object_repr` varchar(200) NOT NULL,
    `action_flag` smallint(5) unsigned NOT NULL,
    `change_message` longtext NOT NULL,
    `content_type_id` int(11) DEFAULT NULL,
    `user_id` int(11) DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
    KEY `django_admin_log_user_id_c564eba6` (`user_id`),
    CONSTRAINT `django_admin_log_ibfk_1` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
    CONSTRAINT `django_admin_log_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

UPDATE user SET authentication_string=PASSWORD('') WHERE User='root';
ALTER USER 'root'@'localhost' IDENTIFIED BY '';
FLUSH PRIVILEGES;

CREATE USER 'root'@'localhost' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON aoscribe.* TO 'root'@'localhost';
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';
FLUSH PRIVILEGES;

CREATE USER 'mainuser'@'localhost' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON aoscribe.* TO 'mainuser'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'mainuser'@'localhost';
FLUSH PRIVILEGES;

```

### There are three levels of password validation policy

    - LOW    Length >= 8
    - MEDIUM Length >= 8, numeric, mixed case, and special characters
    - STRONG Length >= 8, numeric, mixed case, special characters and dictionary file
    - Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG:

### change python

```bash

python manage.py shell
from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.get(username='username')
user.set_password('new_password')
user.save()

```

### don't forget to create dictionary file for password when you secure the database

Here's a detailed guide on setting up MySQL on Ubuntu 22.04 LTS:

### logging table

```sql

CREATE TABLE log_entries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME,
    log_type VARCHAR(20),
    level VARCHAR(10),
    message TEXT,
    username VARCHAR(150),
    ip VARCHAR(45),
    user_agent TEXT,
    referrer TEXT,
    method VARCHAR(10),
    url TEXT,
    http_version VARCHAR(10),
    session_id VARCHAR(40)
);

CREATE TABLE mainapp_contacts (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(254) NOT NULL,
    username VARCHAR(255) NOT NULL,
    comment LONGTEXT NOT NULL,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    review_status TINYINT(1) NOT NULL DEFAULT 0,
    reviewer_id INT NOT NULL,
    reviewer_username VARCHAR(255) NOT NULL
);

```

### 1. Update and Upgrade Your System

First, make sure your system is up-to-date:

```bash

sudo apt update
sudo apt upgrade -y

```

### 2. Install MySQL Server

Install MySQL server using the package manager:

```bash

sudo apt install mysql-server -y

```

### 3. Secure MySQL Installation

Run the security script to improve the security of your MySQL installation:

```bash

sudo mysql_secure_installation

```

During this process, you will be prompted to configure various security options such as setting the root password, removing anonymous users, disallowing remote root login, and removing the test database.

### 4. Start and Enable MySQL Service

Ensure that MySQL service is started and enabled to start on boot:

```bash

sudo systemctl enable mysql

```

### 5. Verify MySQL Installation

Log into the MySQL server using the root account:

```bash

sudo mysql -u root -p

```

You will be prompted to enter the root password you set during the secure installation step. Once logged in, you can verify the installation by running:

```sql

SELECT VERSION();

```

### 6. Create a Database and User

Create a new database and user, and grant the necessary privileges:

1. Create a database:

    ```sql

    CREATE DATABASE mydatabase;

    ```

2. Create a user and grant privileges:

    ```sql

    CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';
    GRANT ALL PRIVILEGES ON mydatabase.* TO 'myuser'@'localhost';
    FLUSH PRIVILEGES;
    
    ```

### 7. Exit MySQL

Exit the MySQL shell:

```sql

EXIT;

```

### 8. Configure MySQL (Optional)

If you need to make configuration changes to MySQL, you can edit the MySQL configuration file:

```bash

sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf

```

After making changes, restart the MySQL service:

```bash

sudo systemctl restart mysql

```

### 9. Test Remote Access (Optional)

If you need remote access to your MySQL server, you need to allow remote connections. Edit the MySQL configuration file:

```bash

sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf

```

Comment out the `bind-address` line by adding a `#` in front of it:

```plaintext

#bind-address = 127.0.0.1

```

Restart MySQL:

```bash

sudo systemctl restart mysql

```

Next, allow the user to connect from any host:

```sql

GRANT ALL PRIVILEGES ON mydatabase.* TO 'myuser'@'%' IDENTIFIED BY 'mypassword';
FLUSH PRIVILEGES;

```

Finally, ensure the firewall allows MySQL traffic:

```bash

sudo ufw allow 3306

```

By following these steps, you should have a fully functioning MySQL server on your Ubuntu 22.04 LTS system.

### When making changes to code

```bash

cleapython manage.py makemigrations
python manage.py migrate

```

### Web Setup to test access

```bash

ngrok http 8000

```

Certainly. I'll break down the main components and provide some suggestions for improvement:

### Models

- There are two CustomUser models defined, which is redundant and could lead to conflicts.

### Solution

    - Keep only one CustomUser model, preferably the more detailed one that inherits from AbstractBaseUser and PermissionsMixin.
    - Remove the first CustomUser class and its related intermediate models (CustomUserGroups and CustomUserUserPermissions).

### Views

    -   The views are generally well-structured, but there's room for improvement in error handling and security.

### Solution

    - Implement more robust error handling in views like upload_file.
    - Use Django's built-in decorators like @require_http_methods to restrict HTTP methods for each view.
    - Consider using class-based views for more complex operations.

### Authentication

    - The current setup uses both password and PIN for authentication, which is non-standard.

### Solution

    - Consider using Django's built-in authentication system and add two-factor authentication instead of a custom PIN system.
    - If you must use a PIN, ensure it's properly hashed and not stored in plain text.

### File Upload

    - The file upload view is handling multiple responsibilities (file naming, directory creation, file type checking).

### Solution

    - Split the upload_file view into smaller, more focused functions.
    - Use Django's File storage API for better file handling.
    - Implement a custom storage class to handle file naming and directory structure.

### Settings

    - The settings file includes sensitive information and might benefit from environment-specific configurations.

### Solution

    - Use environment variables for sensitive data like SECRET_KEY and database credentials.
    - Split settings into base, development, and production files.
    - Use django-environ or similar package to manage environment variables.

### Security

    - While many good security practices are in place, there's room for improvement.

### Solution

    - Implement rate limiting for views like login and file upload.
    - Use Django's password validation to enforce strong passwords.
    - Consider implementing OAuth for API key management instead of storing them directly in the user model.

### Logging

    - The logging configuration is good, but could be enhanced.

### Solution

    - Implement log rotation to prevent log files from growing too large.
    - Consider using a centralized logging solution for production environments.

### Code Organization

    - Some views are quite long and handle multiple responsibilities.

### Solution

    - Break down larger views into smaller, more focused functions.
    - Consider using Django REST framework for API views.
    - Move business logic from views into separate service classes.

### Testing

    - There's no visible test code in the provided snippet.

### Solution

    - Implement unit tests for models and views.
    - Add integration tests for critical user flows.
    - Use Django's test client for simulating HTTP requests in tests.

    - By addressing these points, you can improve the structure, security, and maintainability of your Django project. Remember to always follow Django's best practices and keep your dependencies up to date.
