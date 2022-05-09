import odoorpc

# Prepare the connection to the server
odoo = odoorpc.ODOO('localhost', port=8099)

# Check available databases
print(odoo.db.list())

odoo.login('my_first_odoo','admin','123456')

user = odoo.env.user

print(user.name)

# Simple 'raw' query
# user_data = odoo.execute('res.users', 'read', [user.id])
# print(user_data)

if 'crm.lead' in odoo.env:
    crm_leads = odoo.env['crm.lead'].search([])
    for lead in crm_leads:
        print('......',lead)
        lead_rec = odoo.env['crm.lead'].browse(lead)
        print('..................',lead_rec.name)
        lead_rec.description = 'Hello odooooooooooooooo....'
        lead_rec.write({'mobile': '01793581691'})

        rec_to_delete = odoo.env['crm.lead'].search([('id', '=', 27)])
        lead_del = odoo.env['crm.lead'].browse(rec_to_delete)
        lead_del.unlink()
        print('delete this',rec_to_delete)
        