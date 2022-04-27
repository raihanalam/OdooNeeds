import xmlrpc.client
#https://www.odoo.com/documentation/15.0/developer/misc/api/odoo.html#api-keys
url = "http://0.0.0.0:8099"
db = "my_first_odoo"
username = 'admin'
password = '123456'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()

print("details", version)
uid = common.authenticate(db,username,password,{})

print(uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
#result = models.execute_kw(db, uid, password, 'res.partner', 'check_access_rights', ['read'], {'raise_exception': False})
partners_id = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])
#result = models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', True]]])
result = models.execute_kw(db, uid, password, 'res.partner', 'read', [partners_id], {'fields':['id','name']})

#newUser = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': 'Raihan', 'mobile': '01793581691', 'website':'test'}])
userUp = models.execute_kw(db, uid, password, 'res.partner', 'write',[[26], {'name': 'khan bahadur'}])

models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[46]])

