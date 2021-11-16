from faker import Factory
from datetime import datetime

import json

def create_names(fake):
    for x in range(100):
        genUname = fake.slug()
        genName = fake.name()
        genJob = fake.job()
        genCountry = fake.country()
        genText = fake.text()
        genProfile = fake.profile()
        go = {
                "name": genName,
                "job": genJob,
                "country": genCountry,
                "notes": genText,
                "profile_details": genProfile,
                "timestamp": datetime.now()
        }

        print(go)
if __name__ == '__main__':
    fake = Factory.create()
    create_names(fake)