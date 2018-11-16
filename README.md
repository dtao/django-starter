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
[x] Redis
[x] AUTH_USER_MODEL
[x] Preliminary login view
[x] Preliminary registration view
[x] Templates, with scss support (+ maybe Jinja down the road)
[x] Front-end assets w/ webpack
[ ] API pattern for serialization
[ ] API pattern for pagination
[x] Tests w/ pytest

## Usage

```
django-admin startproject --template=django_starter/template -n .env,README.md
```

[1]: https://docs.djangoproject.com/en/2.1/ref/django-admin/#cmdoption-startproject-template
