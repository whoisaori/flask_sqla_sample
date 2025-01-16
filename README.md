### Sample Flask project
##### This project is a template for easily getting started with the Flask 3.x and SQLAlchemy 2.x frameworks.
***

### Easy Start
##### Just clone the repository:
`git clone https://github.com/whoisaori/flask_sqla_sample.git`
***

##### Create and activate your virtual environment:<br>
`python -m venv venv`
<br>

##### Windows:<br>
`.venv/Scripts/activate`
<br>

##### Unix-systems:<br>
`source .venv/bin/activate`
<br>

##### Install packages:<br>
`pip install -r requirements.txt`
<br>
***
##### Create .flaskenv
``.env
FLASK_APP=app
FLASK_ENV=development
FLASK_DEBUG=True
``
<br>

##### Input in Python Console:
``python
from myapp.extensions import db
from myapp.models.models import *
from myapp import create_app
create_app()
``
<br>

***
### And start coding!
