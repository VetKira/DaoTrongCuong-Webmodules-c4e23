from mongoengine import Document, StringField

class Register(Document):
  username = StringField()
  password = StringField()
  email = StringField()
  