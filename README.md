# django-starter

Like sourdough starter, but for Django.

## Purpose

I guess what I want is to be able to start a Django project quickly with
patterns already established and some preliminary models and views set up. How
it should work, exactly, I haven't decided.

Maybe a [project template][1] is what I'm looking for.

## Goals

[x] WSGI server
[ ] Postgres
[ ] Redis
[ ] AUTH_USER_MODEL
[ ] Preliminary register & login views
[ ] Templates, with scss support (+ maybe Jinja down the road)
[ ] Front-end assets w/ webpack
[ ] API pattern for serialization
[ ] API pattern for pagination
[ ] Tests w/ pytest

## Setup

```
pip install -r requirements-dev.txt
```

[1]: https://docs.djangoproject.com/en/2.1/ref/django-admin/#cmdoption-startproject-template
