Flask Resume
===
> A Flask Python API with JSON endpoints and dynamic UI templating. A simple full-stack boilerplate that demonstrates database setup through object relational mapping, RESTful HTTP request configuration, and frontend data traversal for UI templating.

The [API](http://stuartkershaw.com/api/stuartdkershaw) is structured with SQLAlchemy ORM through [`resume/models.py`](https://github.com/stuartkershaw/flask-resume/blob/master/resume/models.py), and returns JSON with [`resume/api.py`](https://github.com/stuartkershaw/flask-resume/blob/master/resume/api.py).

The frontend leverages API data for a dynamic UI. Jinja2 ([`resume/templates`](https://github.com/stuartkershaw/flask-resume/tree/master/resume/templates)) and Handlebars ([`resume/static`](https://github.com/stuartkershaw/flask-resume/blob/master/resume/static/index.html)) templating approaches are included.

## Configure

Configure the following environment variable with your DB settings:

```
DATABASE_URL=postgres://db_user:db_pw@db_address:5432/db_name
```

On first launch, uncomment the placeholder data in `resume/models.py` to populate the database. This data is intended as a starting point and should be removed / updated as needed. Once populated, re-comment and enjoy.

## Start

```
python run.py
```

## Live

* http://stuartkershaw.com
* http://stuartkershaw.com/jinja2
* http://stuartkershaw.com/handlebars
* http://stuartkershaw.com/api/stuartdkershaw
