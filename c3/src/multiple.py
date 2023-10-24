from built_ins.contact import Contact

class Protocol():
    email: str

class Emailable(Protocol):
    email: str

class MailSender(Emailable):
    """Class extended of Emailable"""
    def send_mail(self, message: str) -> None:
        """Send email to address"""
        print(f"Sendind mail to {self.email=}")

class EmailableContact(Contact, MailSender):
    pass
