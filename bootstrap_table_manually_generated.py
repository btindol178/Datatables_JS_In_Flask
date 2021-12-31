from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer, index=True)
    address = db.Column(db.String(256))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120), index=True)

db.create_all()

user1 = User(name = "Demo User", age = 34, address = "demouserpassword",phone ='12343234',email = "demouser@gmail.com")
db.session.add(user1)
db.session.commit()
user2 = User(name = "Demo User2", age = 32, address = "demouserpassword1",phone ='12332234',email = "demouser1@gmail.com")
db.session.add(user2)
db.session.commit()
user3 = User(name = "Demo User3", age = 31, address = "demouserpassword3",phone ='12379234',email = "demouser2@gmail.com")
db.session.add(user3)
db.session.commit()
user4 = User(name = "Demo User4", age = 34, address = "5edfs",phone ='12343234',email = "demouser@gmail.com")
db.session.add(user4)
db.session.commit()
user5 = User(name = "Demo User25", age = 37, address = "sdafsdfe",phone ='3768343',email = "demouser1@gmail.com")
db.session.add(user5)
db.session.commit()
user6 = User(name = "Demo User36", age = 51, address = "3sdfasf4",phone ='3436756',email = "demousdfsaer2@gmail.com")
db.session.add(user6)
db.session.commit()
user7 = User(name = "Demo User", age = 34, address = "demouserpassword",phone ='1234sdfg3234',email = "demodfsuser@gmail.com")
db.session.add(user7)
db.session.commit()
user8 = User(name = "Demo User432", age = 32, address = "demouserpassword1",phone ='1233dsg2234',email = "demosfdgsuser1@gmail.com")
db.session.add(user8)
db.session.commit()
user9 = User(name = "Demo User443", age = 313, address = "demouserpassword3",phone ='123sdfg79234',email = "demosdgsuser2@gmail.com")
db.session.add(user9)
db.session.commit()
user10 = User(name = "Demo User432", age = 343, address = "5eijnmrdfs",phone ='12343234',email = "demosfsuser@gmail.com")
db.session.add(user10)
db.session.commit()
user11 = User(name = "Demo User245", age = 376, address = "sdafollile",phone ='376866343',email = "demodsguser1@gmail.com")
db.session.add(user11)
db.session.commit()
user12 = User(name = "Demo User34", age = 5144, address = "3sdfadsasf4",phone ='343656756',email = "demousfssdfsaer2@gmail.com")
db.session.add(user12)
db.session.commit()


@app.route('/')
def index():
    users = User.query
    return render_template('bootstrap_table.html', title='Bootstrap Table',
                           users=users)


if __name__ == '__main__':
    app.run()