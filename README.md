# Django Survey Application

![Django-Survey-App Logo](link-to-logo.png) *(Replace 'link-to-logo.png' with an appropriate image of your choice)*

The Django-Survey-App is a custom Django survey application that integrates with the allauth authentication app. This demo app builds upon the [official Django tutorial](https://docs.djangoproject.com/en/1.10/intro/tutorial01/) and includes additional features to enhance the survey experience.

## Key Features

- Replaces the default SQLite database with MySQL, utilizing [mysqlclient](https://pypi.python.org/pypi/mysqlclient) as the database connector.
- Presents random questions to users until all survey questions are answered.
- Provides a comprehensive survey results report accessible through the admin page.
- Utilizes [django-bootstrap3](https://django-bootstrap3.readthedocs.io/) and [bootstrap-admin](https://github.com/django-admin-bootstrap/django-admin-bootstrap) for enhanced styling and aesthetics.

## Installation

### Step 1: Install MySQL

To use the Django-Survey-App, you need to have MySQL installed. You can download MySQL from the [official website](https://dev.mysql.com/downloads/mysql/) and follow the [installation instructions](https://dev.mysql.com/doc/refman/5.7/en/installing.html) provided. Additionally, you might need to add the MySQL binary path to your bash profile:

```bash
export PATH="/usr/local/mysql/bin:$PATH"
```

### Step 2: Initialize Database and User

Once MySQL is installed, open a terminal and start a MySQL interactive session. Then, create the necessary database and user for the Django-Survey-App:

```bash
$ mysql -u root -p
mysql> CREATE USER djangouser@localhost IDENTIFIED BY 'replace-this-password';
mysql> CREATE DATABASE djangosurvey CHARACTER SET UTF8;
mysql> CREATE DATABASE test_djangosurvey CHARACTER SET UTF8;
mysql> GRANT ALL PRIVILEGES ON djangosurvey.* TO djangouser@localhost;
mysql> GRANT ALL PRIVILEGES ON test_djangosurvey.* TO djangouser@localhost;
mysql> FLUSH PRIVILEGES;
mysql> exit
```

Additionally, set an environment variable for your MySQL password:

```bash
export DJANGOUSER_MYSQL_PASSWORD=replace-this-password
```

Make sure to replace `'replace-this-password'` with your actual password in the above commands.

### Step 3: Install Python and Dependencies

The Django-Survey-App was developed using Python 3.6. If you don't have Python installed or if this project doesn't work with your current Python installation, you can use [Anaconda](https://www.continuum.io/downloads) and create a virtual environment:

```bash
$ conda create -n djangosurvey-env python=3.6
$ source activate djangosurvey-env
```

Next, install the required dependencies using pip:

```bash
$ pip install -r requirements.txt
```

### Step 4: Database Updates

Whenever there are updates to the models in this app, you must run the following commands to update the database schema:

```bash
$ python manage.py makemigrations polls
$ python manage.py migrate
```

The first command creates migrations for changes to models.py, and the second applies those migrations to the database.

## Testing and Conventions

Testing and linting have been implemented using [pytest](http://doc.pytest.org/) and [flake8](http://flake8.pycqa.org/). To install the development requirements for testing and linting, run:

```bash
$ pip install -r dev-requirements.txt
```

All committed code should pass all tests, which can be run with:

```bash
$ pytest
```

Additionally, all committed code should adhere to basic PEP8 and linting requirements, which can be verified using:

```bash
$ flake8
```

Feel free to contribute to the project by following these conventions and running the tests before making any pull requests.

Thank you for using Django-Survey-App! If you encounter any issues or have suggestions for improvements, please let us know by raising an issue on our repository.
