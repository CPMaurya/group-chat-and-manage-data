# Django Chat
## Installation API
On Ubuntu:
```
$ pip install virtualenv
```

On the project directory,
## Create virtual environment
```
$ virtualenv vir_env
```

## Activate
```
$ source vir_env/bin/activate
```

## Install requirements
```
$ pip install -r requirements.txt
```

## Do Database migrations
```
$ ./manage.py makemigrations
$ ./manage.py makemigrations chat 
$ ./manage.py migrate
```

## Try creating a superuser for user management
```
$ ./manage.py createsuperuser 
Give necessary inputs
```

## Run development server
```
$ ./manage.py runserver
```

## Installation UI

Install angular CLI
On the project/UI directory,

```
$ npm install primeng --save
$ npm install primeicons --save
$ ng serve
```
