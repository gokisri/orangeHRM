import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils
import os

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = "C:\\Users\\Admin\\Desktop\\LoginData.xlsx"

    logger = LogGen.loggen()

    def test_login(self, setup):
        self.logger.info("*********** Test_002_DDT_login **********")
        self.logger.info("*********** Verifying Login DDT test  **********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)  # Initialize login page object

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        self.logger.info("Number of Rows in Excel: %d", self.rows)

        lst_status = []  # Empty List variable

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            act_title = self.driver.title
            exp_title = "OrangeHRM"

            if act_title == exp_title:
                self._handle_login_success()
                lst_status.append("pass")
            else:
                self._handle_invalid_credentials_error()

                if self.exp == 'pass':
                    self.logger.info("***** Test Failed *****")
                    lst_status.append("fail")
                else:
                    self.logger.info("***** Test Passed *****")
                    lst_status.append("pass")

        self._final_assertion(lst_status)
        self.driver.close()
        self.logger.info("********** COMPLETED TC_LOGIN DDT-001 ********")

    def _handle_login_success(self):
        if self.exp == 'pass':
            self.logger.info("***** Test Passed *****")
            self.lp.clickLogout()
        else:
            self.logger.info("***** Test Failed *****")
            self.lp.clickLogout()

    def _handle_invalid_credentials_error(self):
        try:
            # Checking if "Invalid credentials" message appears
            error_msg = self.driver.find_element(By.XPATH, "//p[contains(text(),'Invalid credentials')]").text
            if "Invalid credentials" in error_msg:
                self.logger.info("Invalid credentials for username: %s", self.user)
        except:
            pass  # If the error message element is not found, continue

    def _final_assertion(self, lst_status):
        if "fail" in lst_status:
            self.logger.info("******** Login DDT TEST FAILED ********")
            assert False
        else:
            self.logger.info("******** Login DDT TEST PASSED ********")
            assert True
