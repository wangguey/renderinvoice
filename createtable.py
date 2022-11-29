from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://spring:IKG8hHQOToIr801ZQgPluD0S1MGpTTxt@dpg-ce1oloarrk09esc1e1gg-a.oregon-postgres.render.com/invoice'
db = SQLAlchemy(app)

@app.route('/')
def index():
    # sql = """
    # CREATE TABLE login (
    # id serial NOT NULL,
    # uid character varying(50) NOT NULL,
    # state character varying(10) NOT NULL,
    # PRIMARY KEY (id))
    # """
    # db.engine.execute(sql)
    # time.sleep(2)
    sql = """
    CREATE TABLE users (
    id serial NOT NULL,
    uid character varying(50) NOT NULL,
    state character varying(10) NOT NULL,
    digit3 character varying(10) NOT NULL,
    PRIMARY KEY (id))
    """
    db.engine.execute(sql)
    return "資料表建立成功！"

if __name__ == '__main__':
   app.run(debug=True)