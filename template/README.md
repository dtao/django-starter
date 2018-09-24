# {{project_name}}

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
