<div style="display:flex; justify-content:center; font-size: 42px; color: #ed9600"> Install project </div>

<hr>
<div style="font-size: 22px; color: #ed9600"> Install and activate enviroment </div>

<br>

For installing project you need to download this from git

<br>

```
https://github.com/Qetu987/test_task.git
```

After that you need to install venv and activate

for 
<span style="font-size: 16px; color: #ed9600; font-weight: bold;">
    unix
</span>
```
python3 -m venv venv 
source venv/bin/activate
```

for 
<span style="font-size: 16px; color: #ed9600; font-weight: bold;">
    win
</span> 
```
python -m venv venv 
venv\Scripts\activate
```
<div style="font-size: 22px; color: #ed9600"> Init db and migrate </div>

<hr>

To create and migrate db fields 

```
python3 manage.py migrate
```

<div style="font-size: 22px; color: #ed9600"> Start project </div>

<hr>
<br>

to switch on daily task 

```
python3 manage.py crontab add .
```

and finally run server 

```
python3 manage.py runserver
```