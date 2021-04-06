import time
from selenium import webdriver

class InstaBot():
    def __init__(self, username, pw):
        self.username = username
        self.pw = pw
        self.driver = webdriver.Chrome(executable_path=r'C:\\Users\\97254\\OneDrive\\Desktop\\chromedriver_win32\\chromedriver.exe')
        self.driver.get('https://www.instagram.com')
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(username)#enter username 
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(pw)#enter password
        time.sleep(0.5)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()#click login
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()#click not now
        time.sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()#click not now
        time.sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a").click()#Goto profile
        time.sleep(8)
    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]

    def _get_names(self):
        time.sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")\
            .click()
        return names
    def unfollow(self):
        not_following_back = []#enter to the list here
        for i in range(len(not_following_back)):
            time.sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(not_following_back[i])#enter the name of the person from the list
            time.sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a").click()#click the first person
            time.sleep(3)
            try:
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button").click()#click unfollow
                time.sleep(4)
                self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]").click()#click are you sure you want to unfollow
            except:
                pass
my_bot = InstaBot('roi.carmona', 'R1604200101c')
my_bot.get_unfollowers()
my_bot.unfollow()
