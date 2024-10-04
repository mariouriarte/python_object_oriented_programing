import json
from pprint import pprint

from c9.src.contact import Contact, ContactEncoder, decode_contact

c = Contact("Noriko", "Hannah")
#print(c.__dict__)

c_decode = json.dumps(c.__dict__)
print(c_decode)

#
c = Contact("Noriko", 'Varam')
text = json.dumps(c, cls=ContactEncoder)
print(text)

some_text = ('{"__class__": "Contact", "first": "Milli", "last": "Dale", "full_name": "Milli Dale"}')
print(some_text)
c2 = json.loads(some_text, object_hook=decode_contact)
print(c2.full_name)
