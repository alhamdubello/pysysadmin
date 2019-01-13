#!/usr/bin/env  python3.6

###if else sample script

user = { 'admin': True, 'active': True, 'name': 'alhamdu' }
prefix = ""
if user['admin'] and user['active']:
    prefix = "ACTIVE - (ADMIN) "
elif user['admin']:
    prefix = "ACTIVE"
elif user['active']:
    prefix = "ACTIVE - "
print(prefix + user['name'])
