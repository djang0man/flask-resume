Flask Resume
===
> A Flask Python API with JSON endpoints and dynamic UI templating. A simple full-stack boilerplate that demonstrates database setup with object relational mapping, RESTful HTTP requests configuration, and frontend data traversal with UI templating.

The [API](http://stuartkershaw.com/api/stuartdkershaw) is modeled with SQLAlchemy via [`resume/models.py`](https://github.com/stuartkershaw/flask-resume/blob/master/resume/models.py), and returns JSON via [`resume/api.py`](https://github.com/stuartkershaw/flask-resume/blob/master/resume/api.py).

The frontend leverages API JSON for templating. Jinja2 ([`resume/templates`](https://github.com/stuartkershaw/flask-resume/tree/master/resume/templates)) and Handlebars ([`resume/static`](https://github.com/stuartkershaw/flask-resume/blob/master/resume/static/index.html)) examples are included.

## Configure

Configure the following environment variable with your own DB settings:

```
DATABASE_URL=postgres://db_user:db_pw@db_address:5432/db_name
```

To populate the database on first launch, uncomment the example data in `resume/models.py` before starting the server. The example data is intended to demonstrate functionality and should be altered as needed. Once the database is populated and content appears on page load, re-comment the data script and enjoy.

## Start

```
python run.py
```
