import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random, re


class shopsky(unittest.TestCase):

    def setUp(self):
        # The chrome webdriver 
        self.driver = webdriver.Chrome(
            "/Users/vimarshkoul/Desktop/sel/chromedriver")
        self.driver.get("https://www.codechef.com/rankings/COOK125B?filterBy=Institution%3DMugneeram%20Bangur%20Memorial%20Engineering%20College%2C%20Jodhpur&order=asc&sortBy=rank")



    def ques(self):
        self.driver.implicitly_wait(10)
       
        ele = self.driver.find_elements_by_tag_name("span")
        string =""
        for i in ele:
            # print(i.text)
            string+=i.text
        # print(string)
        self.driver.implicitly_wait(10)
        lst = re.findall(r"[\w][★][\w]+", string)
        # print(lst)

        # with open("star.txt") as star:
        f= open("star.txt", "a+")
        for i in lst:
            f.write(i + "\n")
        f.close()



    def test_0(self):
        print("Testing Initiated...")
        self.driver.implicitly_wait(10)
        self.ques()




if __name__ == "__main__":
    unittest.main()