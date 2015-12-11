import unittest, scrub
from bs4 import BeautifulSoup


class GetUrlsTest(unittest.TestCase):

    def setUp(self):
        nyTxt = open('nyer.txt')
        nyHtml = nyTxt.read()
        nyTxt.close()
        self.nySoup = BeautifulSoup(nyHtml, 'html.parser')
        
    
    def test_find_main_sections(self):
        mainDict = scrub.find_links(self.nySoup, "main")
        self.assertEqual(len(mainDict), 3)
        self.assertIn('reporting', mainDict.keys())
        self.assertIn('fiction', mainDict.keys())
    
    def test_find_report_and_fiction_links(self):
        mainDict = scrub.find_links(self.nySoup, "main")
        reporting = mainDict['reporting']
        self.assertEqual(len(reporting), 4)
        fiction = mainDict['fiction']
        self.assertEqual(len(fiction), 1)
    
    def test_find_second_sections(self):
        secDict = scrub.find_links(self.nySoup, "secondary")
        self.assertEqual(len(secDict), 4)
        self.assertIn('the critics', secDict.keys())
        self.assertIn('the talk of the town', secDict.keys())
    
    def test_find_critics_and_talk_links(self):
        secDict = scrub.find_links(self.nySoup, "secondary")
        critics = secDict['the critics']
        self.assertEqual(len(critics), 4)
        talk = secDict['the talk of the town']
        self.assertEqual(len(talk), 5)
    
    def test_find_reporting_article_urls(self):
        mainDict = scrub.find_links(self.nySoup, "main")
        reporting = mainDict['reporting']
        urlString = ''.join(reporting)
        self.assertIn("underworld", urlString.lower())
        self.assertIn("stranger", urlString.lower())
        self.assertIn("greek", urlString.lower())
    


class GetArticleTest(unittest.TestCase):

    def setUp(self):
        nyTxt = open('nyer.txt')
        nyHtml = nyTxt.read()
        nyTxt.close()
        nySoup = BeautifulSoup(nyHtml, 'html.parser')
        mainDict = scrub.find_links(nySoup, "main")
        self.fictionUrl = mainDict['fiction'][0]
    
    def test_get_article_html(self):
        artParsed = scrub.get_article_from_url(self.fictionUrl)
        textFromWebpage = "Yongsu and I launched the flat-bottomed boat"
        self.assertIn(textFromWebpage, artParsed)


if __name__ == "__main__":
    unittest.main()
        