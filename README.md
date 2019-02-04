# Cardholder


Setting up development Environment on Linux
----------------------------------

### Install Project (edit mode)

#### Working copy
    
    $ cd /path/to/workspace
    $ cd card_holder
    $ pip install -e .
 
### Setup Database

#### Configuration

```yaml

db:
  url: postgresql://postgres:postgres@localhost/card_holder_dev
  test_url: postgresql://postgres:postgres@localhost/card_holder_test
  administrative_url: postgresql://postgres:postgres@localhost/postgres
```

#### Remove old abd create a new database **TAKE CARE ABOUT USING THAT**

    $ card_holder db create --drop --mockup

And or

    $ card_holder db create --drop --basedata 

#### Drop old database: **TAKE CARE ABOUT USING THAT**

    $ card_holder [-c path/to/config.yml] db --drop

#### Create database

    $ card_holder [-c path/to/config.yml] db --create

Or, you can add `--drop` to drop the previously created database: **TAKE CARE ABOUT USING THAT**

    $ card_holder [-c path/to/config.yml] db create --drop


### Running tests

```bash
pip install -r requirements-dev.txt
pytest
```

### Running server

#### Single threaded 

```bash
card_holder [-c path/to/config.yml] serve
```

#### WSGI

wsgi.py

```python
from card_holder import card_holder
card_holder.configure(files=...)
app = card_holder
```

```bash
gunicorn wsgi:app
```

### How to start

Checkout `card_holder/controllers/foo.py`, 
`card_holder/models/foo.py` and `card_holder/tests/test_foo.py` to
learn how to create an entity.

