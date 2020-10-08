import unittest
from contact import *

class testContact(unittest.TestCase):

    contact1=Contact("Adam", "Bak")
    contact2=Contact("Zbigniew", "IGLA")

    def test_email(self):
        self.assertEqual(self.contact1.email(), "Adam_Bak@firma.pl")
        self.assertEqual(self.contact2.email(), "Zbigniew_IGLA@firma.pl")

    def test_przedstawSie(self):
        self.assertEqual(self.contact1.przedstawSie(), "Adam Bak")
        self.assertEqual(self.contact2.przedstawSie(), "Zbigniew IGLA")
