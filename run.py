from app import create_app
from app.ext.db import db
from app.models import *
from app.controllers import *

app = create_app("develop")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = 'mysecretkey'

if __name__ == "__main__":
    app.run(debug=True)