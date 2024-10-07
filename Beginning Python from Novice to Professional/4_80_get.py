people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    }
}


labels = {
    'phone': 'phone number',
    'addr': 'address' 
}

a = input('Name: ')
request = input('Phone number (p) or address (a)?')

key = request
if (request == 'p'):
    key = 'phone'
if (request == 'a'):
    key = 'address'

person = people.get(a, {})
label = labels.get(key, key)
result = person.get(key, 'not available')

print(a,label,result)




