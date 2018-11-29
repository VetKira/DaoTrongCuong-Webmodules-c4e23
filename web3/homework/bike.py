from mongoengine import Document, StringField , IntField

class Bike(Document):
    model = StringField()
    daily = StringField()
    image = StringField()
    year = IntField()
 