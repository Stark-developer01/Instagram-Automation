from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        bot.maximize_window()
        time.sleep(3)
        bot.find_element_by_name('username').send_keys(self.username)
        bot.find_element_by_name('password').send_keys(self.password + Keys.RETURN)
        time.sleep(3)

    def searchUser(self, user):
        bot = self.bot

        bot.get('https://www.instagram.com/explore/tags/' + user)

         # If you wish to search for a user instead just put this line 'https://www.instagram.com/
        # instead of 'https://www.instagram.com/explore/tags/'

    def likePhotos(self, amount):
        bot = self.bot
        bot.find_element_by_class_name('v1Nh3').click()

        i = 1
        while i<= amount:
            time.sleep(2)
            bot.find_element_by_class_name('fr66n').click()
            bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            i+=1

        bot.get('https://www.instagram.com/' + self.username)


insta = InstagramBot('your_username', 'your_password') #Give your username and password of your account here
insta.login()
insta.searchUser('hashtag_you_want_to_search') #Type in the hashtag here which you want to search 
# Type the username or user id above if you want to search for a particular user
insta.likePhotos(8)
