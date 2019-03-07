# django-csv-example

Example of integrating CSV data into Django. Includes importing CSV data to populate a model and exporting a CSV of selected records from the admin.


Like my work? Tip me! https://www.paypal.me/jessamynsmith


### Development

Fork the project on github and git clone your fork, e.g.:

    git clone https://github.com/<username>/django-csv-example.git

Create a virtualenv using Python 3 and install dependencies. I recommend getting python3 using a package manager (homebrew on OSX), then installing [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation) to that python. NOTE! You must change 'path/to/python3'
to be the actual path to python3 on your system.

    mkvirtualenv eggtimer --python=/path/to/python3
    pip install -r requirements.txt

Set up db:

    python manage.py migrate
    
Import data:

    python manage.py import_csv
    
Create a superuser:

    python manage.py createsuperuser

Run server:

    python manage.py runserver
    
Log in to the admin in a browser at: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)