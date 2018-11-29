import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds011462.mlab.com:11462/movie

host = "ds011462.mlab.com"
port = 11462
db_name = "movie"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())