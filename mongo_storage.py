# mongo_storage.py
import pymongo
from web_scraping import job_listings

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["job_database"]
collection = db["job_listings"]

for job in job_listings:
    collection.insert_one(job)
