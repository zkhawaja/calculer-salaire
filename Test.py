import unittest
import calculersalaire as c

class Test(unittest.TestCase):
    def test_architecte(self):
        self.assertEqual(c.CalculerSalaire("Architecte",4),"4000 euro")
    def test_médecin(self):
        self.assertEqual(c.CalculerSalaire("médecin",8), "7000 euro")
    def test_consultant(self):
        self.assertEqual(c.CalculerSalaire("consultant",5), "5000 euro")


if __name__ == '__main__':
   unittest.main()
