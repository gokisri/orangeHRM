import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import os


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    def test_homePageTitle(self, setup):
        self.logger.info("*********** Test_001_Login **********")
        self.logger.info("*********** Verifying Home Page Title **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "OrangeHRM":
            assert True
            self.driver.close()
            self.logger.info("*********** Home Page Title Test is passed*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*********** Home Page Title Test is failed*********")
            assert False

    def test_login(self, setup):

         self.logger.info("*********** Verifying Login test  **********")
         self.driver = setup
         self.driver.get(self.baseURL)
         self.lp = LoginPage(self.driver)
         self.lp.setUserName(self.username)
         self.lp.setPassword(self.password)
         self.lp.clickLogin()
         act_title = self.driver.title
         if act_title == "OrangeHRM":
            assert True
            self.logger.info("*****************Login test is passed***************")
            self.driver.close()
         else:
           self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
           self.driver.close()
           self.logger.error("*********** login Test is failed*********")
           assert False



