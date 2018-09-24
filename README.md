# django-starter

Like sourdough starter, but for Django.

## Purpose

I guess what I want is to be able to start a Django project quickly with
patterns already established and some preliminary models and views set up. How
it should work, exactly, I haven't decided.

Maybe a [project template][1] is what I'm looking for.

## Goals

[x] WSGI server
[x] Postgres
[ ] Redis
[x] AUTH_USER_MODEL
[x] Preliminary login view
[x] Preliminary registration view
[x] Templates, with scss support (+ maybe Jinja down the road)
[x] Front-end assets w/ webpack
[ ] API pattern for serialization
[ ] API pattern for pagination
[ ] Tests w/ pytest

## Setup

Install library dependencies:

```
pip install -r requirements-dev.txt
```

Set up a Postgres database:

```
createuser -d -E -R -S {{project_name}}
createdb -O {{project_name}} {{project_name}}
```

[1]: https://docs.djangoproject.com/en/2.1/ref/django-admin/#cmdoption-startproject-template
