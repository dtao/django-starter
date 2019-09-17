# {{project_name}}

## Setup

Install library dependencies:

```
pip install -r requirements-dev.txt
npm install
```

Set up a Postgres database:

```
createuser -d -E -R -S {{project_name}}
createdb -O {{project_name}} {{project_name}}
```

Run migrations:

```
honcho run python manage.py migrate
```

Start the app:

```
honcho start
```

## Testing

To run the tests:

```
pytest
```

By convention, tests are organized per-module in every app's tests/ directory.
For example, tests for models.py should be located in tests/test_models.py.

## Deployment

The following environment variables are *required*:

- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_SECRET_KEY`

Also, make sure webpack builds are run in the target environment for each
deployment. On Heroku, for example, this is as simple as ensuring the necessary
[buildpack][1] is enabled:

```
heroku buildpacks:add heroku/nodejs
```

[1]: https://devcenter.heroku.com/articles/using-multiple-buildpacks-for-an-app
