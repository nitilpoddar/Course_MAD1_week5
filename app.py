from flask import request, render_template, Flask
from flask_sqlalchemy import SQLAlchemy
import os

#creating a current directory
current_dir= os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(current_dir, "testdb.sqlite3")
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

class Item(db.Model):
    __tablename__ = 'item'
    ID = db.Column(db.Integer, autoincrement = True, primary_key=True)
    Item_Name = db.Column(db.String, unique=True)
    Stock = db.Column(db.Integer)
    Wholesale_Price = db.Column(db.Integer)


@app.route("/")
def index():
    items = Item.query.all()
    return render_template("index.html", items=items, title = "Rabbit")


if __name__ == "__main__":
    app.run(debug=True)