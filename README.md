Flask Resume
===
> A Flask API with JSON endpoints and dynamic templating.

The [API](http://stuartkershaw.com/api/stuartdkershaw) is structured through [`resume/models.py`](https://github.com/stuartkershaw/flask-resume/blob/master/resume/models.py) and returns JSON with [`resume/api.py`](https://github.com/stuartkershaw/flask-resume/blob/master/resume/api.py).

The frontend leverages JSON to build a dynamic UI. Jinja2 ([`resume/templates`](https://github.com/stuartkershaw/flask-resume/tree/master/resume/templates)) and Handlebars ([`resume/static`](https://github.com/stuartkershaw/flask-resume/blob/master/resume/static/index.html)) templating approaches are included.

## Configure

Configure the following environment variables with your settings:

```
DATABASE_URL=postgres:// db_user : db_pw @ db_address : 5432 / db_name"
```

On first launch, uncomment the example data within `resume/models.py`. Once the database is populated this should be commented back out. The placeholder data is intended as a starting point and should be removed or updated as needed. 

## Start

```
python run.py
```

## Live

* http://stuartkershaw.com
* http://stuartkershaw.com/jinja2
* http://stuartkershaw.com/handlebars
* http://stuartkershaw.com/api/stuartdkershaw
