# install project

## install and activate enviroment

for installing project, you need to download this from git

```
https://github.com/Qetu987/test_task.git
```

After you need to install venv and activate

for unix
```
python3 -m venv venv 
source venv/bin/activate
```

for win 
```
python -m venv venv 
venv\Scripts\activate
```

## init db and migrate

for create and migrate db fields 
```
python3 manage.py migrate
```

## start project 

for switch on daily task 

```
python3 manage.py crontab add .
```

and finally run server 

```
python3 manage.py runserver
```