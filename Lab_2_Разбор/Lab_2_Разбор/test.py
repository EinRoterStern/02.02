import unittest
from  mail import check_email as mail

class CheckEmail(unittest.TestCase):
    def test_incorect_mail(self):
        mails = ["","1","g3g@","@gmail", "g@gmail.", ".d@gmail..c", "@@gmail", "gm@@gmail.com", 
                 "user@example", "user@.example.com", "user.@example.com", "user..example.com",
                 "user@-example.com", "user@example-.com", "user@111.222.333.444", "user@.255.255.255.255",
                 "user@example..com", "user@example.com.", "user@ex_ample.com" ]

        for email in mails:
            print(f"Testing invalid email: {email}")
            self.assertFalse(mail(email))
    def test_corect_mail(self):
        mails_cor = [
    "john.doe@example.com",
    "jane_doe@example.com",
    "james1234@example.net",
    "bob-smith@example.org",
    "alice+test@example.com",
    "test@example.com",
    "user123@example.edu",
    "example123@example.com",
    "user.name@example.com",
    "support@example.com"
]
        for email in mails_cor:
            print(f"Testing invalid email: {email}")
            self.assertTrue(mail(email))
