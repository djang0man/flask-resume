Flask Resume
===
> A Flask API with JSON endpoints and dynamic templating.

The [API](http://stuartkershaw.com/api/stuartdkershaw) is database-fed and structured using [`resume/models.py`](https://github.com/stuartkershaw/flask-resume/blob/master/resume/models.py). HTTP GET requests to `/api/username` return JSON as defined in [`resume/api.py`](https://github.com/stuartkershaw/flask-resume/blob/master/resume/api.py).

The frontend leverages JSON to build a dynamic UI. Examples of Jinja2 ([`resume/templates`](https://github.com/stuartkershaw/flask-resume/tree/master/resume/templates)) and Handlebars ([`resume/static`](https://github.com/stuartkershaw/flask-resume/blob/master/resume/static/index.html)) templating approaches are included.

## Configure

Configure the following environment variables with your settings:

```
DATABASE_URL=postgres:// db_user : db_pw @ db_address : 5432 / db_name"
```

On first launch, uncomment the example data in `resume/models.py`. Comment it back out after the database is populated. This is intended to provide a starting point and should then be removed or updated!

## Start

```
python run.py
```

## Live

* http://stuartkershaw.com
* http://stuartkershaw.com/jinja2
* http://stuartkershaw.com/handlebars
* http://stuartkershaw.com/api/stuartdkershaw
