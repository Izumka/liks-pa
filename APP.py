from flask import Flask

class APP:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "http://Izumka.mysql.pythonanywhere-services.com/Izumka$liks_db"

