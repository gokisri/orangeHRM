import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.delete_employee import PIMPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from selenium.common.exceptions import TimeoutException

class Test_DeletePIMEmployee:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_delete_first_employee(self, setup):
        """Test Case: Click Employee List and Directly Click Delete Button"""
        self.logger.info("********** Test Delete Employee in PIM **********")
        self.driver = setup
        self.driver.get(self.baseURL)

        # ✅ Login
        self.logger.info("Logging into OrangeHRM")
        self.login = LoginPage(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()

        try:
            # ✅ Navigate to PIM and Click Employee List
            self.logger.info("Navigating to PIM Page")
            self.pim = PIMPage(self.driver)
            self.pim.navigate_to_pim()
            self.pim.click_employee_list()

            # ✅ Delete the first employee (without selecting checkbox)
            self.pim.delete_first_employee()

            # ✅ Confirm Deletion
            self.logger.info("✅ Employee deleted successfully!")

        except TimeoutException:
            self.logger.error("❌ Employee deletion failed due to timeout.")
            assert False, "Deletion confirmation not found!"

        except Exception as e:
            self.logger.error(f"❌ Test case failed due to error: {str(e)}")
            assert False, f"Test case failed: {str(e)}"
