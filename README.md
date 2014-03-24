kam-u-thiann-tioh
=================

search engine on 臺灣318運動資料


Backend Initialization
-----------------

at repo root directory, do the following:

1. install virtualenv

    pip install virtualenv


2. init the env folder, enter virtual environment

    virtualenv env
    . env/bin/activate


3. install django and related packages

    pip install -Ur packages.txt


Backend Bootstrap
-----------------

at repo root directory, do the following

    . env/bin/activate
    cd server
    python ./manage.py runserver 8000

Now check http://localhost:8000/

