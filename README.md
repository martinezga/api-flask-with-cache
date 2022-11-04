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
- Non-case sensitive filter

### API Usage

Added a [Postman collection](api-users.postman_collection.json) to easily use API endpoints and query parameters combinations.
Also contains examples of expected responses.

### Endpoint: /auth/users/
#### HTTP Method: GET

By default, response it is paginated with 10 objects.

**Pagination query parameters:**

- page: Optional. Number for pagination across multiple pages of results
- per_page: Optional. Number of objects to be returned, between 1 and 100.

**Filtration query parameters:**

- name: Optional. User's name. Filter exact coincidence. Case sensitive.
- lastname: Optional. User's last name. Filter exact coincidence. Case sensitive.
- email: Optional. User's email address. Filter exact coincidence. Case sensitive.

**Pagination and filtration could be used in same request.**

**To make a request with last_page field (obtained in response) must have per_page (if used)**

Examples:
- /auth/users/?page=5&per_page=3/
- /auth/users/?name=Sue/
- /auth/users/?name=Sue&email=sueortega3058@email.com/
- /auth/users/?name=Eduardo&lastname=Todd/
- /auth/users/?lastname=Cantrell&email=nataliecantrell499@email.com/
- /auth/users/?name=Sue&page=5/

### Endpoint: /auth/users/
#### HTTP Method: POST

Create and user.

Required json body:
  ```json
  {
      "name": "John",
      "lastname": "Doe",
      "email": "johndoe4444@email.com"
  }
  ```

### Endpoint: /dummy/users/
#### HTTP Method: GET

Create dummy users with random data provided by Faker.

- With NO query parameters create ONE user.

- With query parameters create as many users as you request.

Example:
- /dummy/users/?qty=20/
- /dummy/users/?qty=1000/

**Note: up to 1000 server could respond with time out error**

Response with real created items and total_registered in Database.

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
