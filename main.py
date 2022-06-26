from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

PROMISED_DOWN = 90
PROMISED_UP = 90
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
TWITTER_EMAIL = "YOUR EMAIL"
TWITTER_PASSWORD = "YOUR PASSWORD"


class InternetSpeedTwitter:
    def __init__(self, driver_path):
        self.ser = Service(driver_path)
        self.op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.ser, options=self.op)
        self.up = PROMISED_UP
        self.down = PROMISED_DOWN

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(5)
        self.driver.maximize_window()
        sleep(3)
        go_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
                                                       '/span[4]')
        go_button.click()

        sleep(60)
        self.down = float(self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/"
                                                           "div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div"
                                                           "/div[2]/span").text)
        self.up = float(self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/"
                                                         "div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/"
                                                         "div[2]/span").text)

        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            return True
        self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        sleep(3)
        self.driver.maximize_window()
        sleep(2)
        sign_in = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/'
                                                     'div[3]/div[5]/a/div')
        sign_in.click()
        sleep(2)
        email = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/'
                                                   'div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/'
                                                   'div/input')
        email.click()
        email.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/'
                                                         'div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/'
                                                         'span/span')
        next_button.click()
        sleep(1)

        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/'
                                                      'div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]'
                                                      '/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)

        login_button = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/'
                                                          'div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/'
                                                          'div/div/div/span/span')
        login_button.click()
        sleep(2)

        what_is_happening = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/'
                                                               'div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]'
                                                               '/div[1]/div/div/div/div/div/div/div/div/div/label/div'
                                                               '[1]/div/div/div/div/div[2]/div/div/div/div')

        what_is_happening.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when"
                                    f" I pay for 300down/300up?")


bot = InternetSpeedTwitter(CHROME_DRIVER_PATH)
if bot.get_internet_speed():
    bot.tweet_at_provider()
