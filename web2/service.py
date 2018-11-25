from mongoengine import Document,StringField , IntField, BooleanField

#design database
class Service(Document): #quy tac cua class viet hoa chu dau
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    occupied = BooleanField()


    
