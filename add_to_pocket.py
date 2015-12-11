from selenium import webdriver
from datetime import datetime

FINRA_PW = "Winter2015"


def nykr():
    br = webdriver.Firefox()
    br.get("http://www.newyorker.com/magazine")
    
    issueNo = br.find_element_by_css_selector("#page-header h3").text
    issueNoElems = issueNo.split(" ")
    if len(issueNoElems) > 4:    # double issue
        secondWeek = int(issueNoElems[-2].strip(","))
        dateNo = datetime.now().day
        if dateNo + 8 > secondWeek:
            return None
    
    storiesLinks = br.find_elements_by_css_selector(".stories article h2 a")

    return storiesLinks


def add_to_pocket():
    
    stories = nykr()
    
    if stories == None:
        print("double issue, already added last week")
    
    else:

        pocket = webdriver.Firefox()
        pocket.get("https://getpocket.com/a/")
    
        if "login" in pocket.current_url:
            pocket.find_element_by_id("feed_id").send_keys("itsalisaz")
            pocket.find_element_by_id("login_password").send_keys("qwerty")
            pocket.find_element_by_id("login_password").submit()
    
        add = pocket.find_element_by_css_selector("#pagenav_addarticle a")
    
        for story in stories:
            add.click()
            pocket.find_element_by_css_selector("#addMenu div input").send_keys(story.get_attribute("href"))
            pocket.find_element_by_css_selector("#addMenu div .button").click()
    
    pocket.quit()



if __name__ == "__main__":
    
    add_to_pocket()