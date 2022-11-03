## Purpose

Develop an API endpoint to get a list of users.

### Available on

https://api-users.onrender.com

### Technologies used

* Flask
* PostgreSQL
* SQLAlchemy ORM
* Redis
* Docker
* Render - Cloud Application Hosting
* Faker

### Description

* MVC Architecture
* Database has more than 1MM records
* Supports pagination
* Supports Filtration
* Cache-Control (client and server-side)

### Improvements

- DB migration
- Complete CRUD operation: Update, retrieve and delete users
- Searching and ordering support
- Authentication and authorization
- Testing

### API Usage

### Local environment set up

There are two set up, using pipenv or docker-compose. Next steps are common between them.

- Copy _.env to .env:

        $ cp _.env .env

- Update .env file with the right values

#### Using pipenv

- Install dependencies using pipenv. 
In case you don't have pipenv, execute: `pip install pipenv` first.

        $ pipenv install

    To allow DB use, install psycopg2-binary with:

        $ pipenv install --dev

- Run the development server executing:

        $ pipenv run server

#### Using docker-compose

- Execute:

        $ docker-compose up -d build

- To stop it execute:

        $ docker-compose stop
- 
**To test successfully set up visit: http://localhost:8000**

### Production environment

Set up with Gunicorn, psycopg2 and Docker deploy. Use the [Dockerfile](Dockerfile) file.

To use [render](https://render.com/) connect your GitHub repository and allow automatic deploy by push.

In server needs to configure the follow environment variables (minimal ones):

- SQLALCHEMY_DATABASE_URI
- ENV

Complete environment variables list are as example on [_.env](_.env) file, they are used on [settings](api/configurations/settings.py) app.

**Keep an eye on PORT value** It is required to deploy the app, Heroku and Render assign it automatically.

---
⌨️ with ❤️ by [Gabriella Martínez](https://github.com/martinezga) 😊
