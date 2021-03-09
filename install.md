# Install project

<hr>
## Install and activate enviroment

For installing project you need to download this from git

<br>

```
https://github.com/Qetu987/test_task.git
```

After that you need to install venv and activate

for **unix**
```
python3 -m venv venv 
source venv/bin/activate
```

for **win**
```
python -m venv venv 
venv\Scripts\activate
```
## Init db and migrate

To create and migrate db fields 

```
python3 manage.py migrate
```

## Start project


to switch on daily task 

```
python3 manage.py crontab add .
```

and finally run server 

```
python3 manage.py runserver
```
