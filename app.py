from flask import Flask , render_template, request 
import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv


load_dotenv()

# def create_app():  # to prevent creating multiple apps
app = Flask(__name__)
# client = MongoClient('mongodb://127.0.0.1:27017/')
client = MongoClient(os.environ.get("MONGODB_URI")) # os.environ look the envrionment variables
app.db = client['miniBlogPost']



# data = {}
@app.route("/", methods=['GET','POST'])
def home():
    if request.method=="GET":
        print("request: ",request.method)

    elif request.method == 'POST':
        # print("request get ",request.form.get()))
        if request.form.get("title") and request.form.get("content"):
            title = request.form.get('title')
            content = request.form.get('content')
            date = datetime.datetime.today().date()
            time = datetime.datetime.today().time().strftime("%H:%M")
            # data[title] = [content,date,time]

            app.db.data.insert({"title":title,"content":content,"date":f"{date}","time":f"{time}"})

    data={entry['title']:[entry['content'],entry['date'],entry['time']] for entry in app.db.data.find({})}
    
    # print("database: " ,app.db.data.find({}))
    # print([data for data in app.db.data.find({})])
            
    return render_template("index.html",data=dict(reversed(list(data.items()))))


    # return app


