import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds123171.mlab.com:23171/kira

host = "ds123171.mlab.com"
port = 23171
db_name = "kira"
user_name = "kira"
password = "VetKira.96"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())