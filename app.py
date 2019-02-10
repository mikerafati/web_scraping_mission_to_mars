from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars
import os
app = Flask(__name__)
# client = MongoClient(os.environ['MONGODB_URI'])
# db = client['mars']
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    try:
        mars = mongo.db.mars.find_one()
        return render_template("index.html", mars=mars)
    except:
        redirect("/scrape", code=302)    
# client = pymongo.MongoClient()

# db = client.mars_db

# collection = db.mars_facts

@app.route('/scrape')
def scraper():
    mars = mongo.db.mars
    scrape = mars(
      url1='https://mars.nasa.gov/news/',

        url2='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars',

        url3='https://twitter.com/marswxreport?lang=en',

        url4='http://space-facts.com/mars/',

        url5='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'   
    )

    data = scrape.scrape()
    mars.update({}, data, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run()    

 