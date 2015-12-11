import unittest, emailtxt


class EmailTxtTest(unittest.TestCase):

    def test_get_subject(self):
        fileName = "test_alisa-says-yay.txt"
        subject = emailtxt.get_subject(fileName)
        self.assertEqual(subject, "test: alisa says yay")
    
    def test_get_content(self):
        fileName = "the talk of the town_amo-amas.txt"
        content = emailtxt.get_content(fileName)
        self.assertIn("Joshua Katz, professor", content)
        self.assertIn("grownups all day", content)
    

if __name__ == "__main__":
    unittest.main()