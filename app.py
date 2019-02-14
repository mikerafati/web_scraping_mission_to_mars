from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import pymongo
import scrape_mars
import os
app = Flask(__name__)
# client = MongoClient(os.environ['MONGODB_URI'])
# db = client['mars']
client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_data_entries


@app.route("/")
def index():
    mars_collection = list(db.collection.find())[0]
    return  render_template('index.html', mars_collection=mars_collection)
    

@app.route('/scrape')
def scrape():
    db.collection.remove({})
    mars_collection = scrape.scrape()
    db.collection.insert_one(mars_collection)
    return render_template('scrape.html')
    

    

if __name__ == "__main__":
    app.run()    

 