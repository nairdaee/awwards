# AWWARDS


Created on _June 8, 2020_

---

## AUTHOR

Adrian Etenyi

### Description
This is an app that allows a user to post a project he/she has created and get it reviewed by his/her peers
It can also be rated based on its level of functionality
___

### User stories

A user is able to:

* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View their profile page


### Application setup

* Since the app uses a remote database provided by Heroku, you will need to configure your own local database  to be able to use it. Follow these steps:
    * Create a virtual environment i.e `virtualenv --python=/usr/bin/python3 <env name> ` and activate it
    * Install all the requirements....__see requirements__
    * Configure your own database...__see db configurations__ and make migrations
    * Run application


### Requirements

`python 3.7.5` _(Python 3.7 - 3.8)_

```
    Django==1.11.29/ Django==3.0.5
    djangorestframework==3.11.0
    django-bootstrap3==12.1.0
    gunicorn==20.0.4
    Pillow==7.1.2
    psycopg2==2.8.5
    pytz==2020.1
    whitenoise==5.1.0
```

> To install them just use `pip3 install -r requirements.txt`

### DB Configurations (You can also use sqlite as your database)

> Go to postgresql i.e `psql`
 * Create your database `CREATE DATABASE <database name>;`

* Change the contents of database to the following:
    ```
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': '< Your database name >',
                'USER': '< Your Database Username >',
                'PASSWORD':'< Your Database Password >',
             }
        }
    ```

* Make migrations i.e `python3.7 manage.py makemigrations` then run them to update your db `python3.7 manage.py migrate`

> Note: _if you want you can use the .env file to store your db credentials for safety purposes_

### Known bugs

When posting a rate score...you have to press the post button twice for it to display the user's rating on rating table

### Live site

> https://awardsss.herokuapp.com/

If you want to access the apps API....add the following to your url:
* `.../api/projects/` - to see the projects
* `.../api/profiles/` - to see users profiles


### Support and contact details

Feel free to send me comments,queries and/or feedback via email @etadriano2@gmail.com

### License

Copyright (c) 2020 Adrian Etenyi.
Licensed under the [MIT license](LICENSE)
