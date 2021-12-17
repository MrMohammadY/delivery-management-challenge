# Delivery Management

This project was created for couriers which calculates their daily salary and weekly salary and show this information.

<hr style="border:2px solid gray"> </hr>

## Installation

### First step

create BMI directory:

    mkdir Delivery_Management

go to BMI directory:

    cd Delivery_Management

---

### Second step

clone the project:

    git clone https://github.com/MrMohammadY/delivery-management-challenge.git

create virtualenv in BMI directory:

    virtualenv delivery_venv

now active your virtualenv:

    source delivery_venv/bin/activate

---

### Third step

go to project by:

    cd delivery-management-challenge

install package with:

    pip install -r requirements.txt

---

### Fourth step

in bmi directory you should create .env file for some django settings(.env files is hidden files):

    touch .env

and fill this argument in env file:

- SECRET_KEY = '\<django secret key (you can generate from this [site](https://djecrety.ir/)) >'
- DEBUG = True
- ALLOWED_HOSTS = ['*']

---

### Fifth step

now make migrations with:

    python manage.py makemigrations

and after that applying migrations:

    python manage.py migrate

and after apply migrations run celery:

    celery -A delivery worker -l info

and run celery beat:

    celery -A delivery beat -l info

---

### In the last

you can now run project by:

    python manage.py runserver