Flask Resume
===
> A Flask Python API with JSON endpoints and dynamic UI templating. A simple full-stack boilerplate that demonstrates database setup with object relational mapping, RESTful HTTP requests configuration, and frontend data traversal with UI templating.

The [API](http://stuartkershaw.com/api/stuartdkershaw) is formatted using SQLAlchemy ORM via [`resume/models.py`](https://github.com/stuartkershaw/flask-resume/blob/master/resume/models.py), and returns JSON via [`resume/api.py`](https://github.com/stuartkershaw/flask-resume/blob/master/resume/api.py).

The frontend leverages the API for dynamic UI templating. Jinja2 ([`resume/templates`](https://github.com/stuartkershaw/flask-resume/tree/master/resume/templates)) and Handlebars ([`resume/static`](https://github.com/stuartkershaw/flask-resume/blob/master/resume/static/index.html)) examples are included.

## Configure

Configure the following environment variable with your own DB settings:

```
DATABASE_URL=postgres://db_user:db_pw@db_address:5432/db_name
```

Before first launch, to populated the database, uncomment the placeholder data in `resume/models.py`. This is intended as a starting point to demonstrate functionality and should be updated and removed as needed. Once the database is populated and the content shows on page load, re-comment the data scripts and enjoy.

## Start

```
python run.py
```

## Live

* http://stuartkershaw.com
* http://stuartkershaw.com/jinja2
* http://stuartkershaw.com/handlebars
* http://stuartkershaw.com/api/stuartdkershaw
