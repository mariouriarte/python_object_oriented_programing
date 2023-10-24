from built_ins.contact import Contact
from address_holder import AddressHolder

# class Friend(Contact):
#     def __init__(self, name: str, email: str, phone: str) -> None:
#         super().__init__(name, email)        
#         self.phone = phone

class Friend(Contact, AddressHolder):
    def __init__(
            self,
            name: str,
            email: str,
            phone: str,
            street: str,
            city: str,
            state: str,
            code: str,
            ) -> None:
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone
