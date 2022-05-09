import json
import random
import urllib.request

HOST = 'localhost'
PORT = 8099
DB = 'my_first_odoo'
USER = 'admin'
PASS = '123456'

def json_rpc(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000),
    }
    req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers={
        "Content-Type":"application/json",
    })
    reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]

def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})

# log in the given database
url = "http://%s:%s/jsonrpc" % (HOST, PORT)
uid = call(url, "common", "login", DB, USER, PASS)

# create a new note
args = {
    #'color': 8,
    'memo': 'Test note from JSON RPC',
    #'create_uid': uid,
}
# note_id = call(url, "object", "execute", DB, uid, PASS, 'note.note', 'create', args)
# print('created note.......', note_id)
# args = {
#     'patient_name': 'JSON RPC',
# }
# patient_id = call(url, "object", "execute", DB, uid, PASS, 'hospital.patient', 'create', args)
# print('created patient.........', patient_id)

#perform read operations

# read_patient = call(url, "object", "execute", DB, uid, PASS, 'hospital.patient', 'read', [32])
# print('patient.........', read_patient)

#Write/update operations
# vals = {
#     'patient_name': 'JSON RPC Updated',
# }
# update_patient = call(url, "object", "execute", DB, uid, PASS, 'hospital.patient', 'write', [32],vals)
# print('patient.........', update_patient)

#Delete Operations
delete_patient = call(url, "object", "execute", DB, uid, PASS, 'hospital.patient', 'unlink', [32])
print('deleted patient.........', delete_patient)