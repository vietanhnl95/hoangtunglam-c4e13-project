import mongoengine


# mongodb://<dbuser>:<dbpassword>@ds163656.mlab.com:63656/userlist
host = "ds163656.mlab.com"
port = 63656
db_name = "userlist"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
