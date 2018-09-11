from mongoengine import *

connect('happy_hour_db', host='0.0.0.0')


class Restaurant(Document):
    restraurant_name = StringField(max_length=200, required=True)
    city = StringField(max_length=50)
    address = StringField(max_length=50)


class DayOfWeek(Document):
    day = StringField(max_length=20, required=True)
    deals = StringField(max_length=200, required=True)
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)

