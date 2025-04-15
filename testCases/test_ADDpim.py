import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.ADDpim import PIMPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from selenium.common.exceptions import TimeoutException

class Test_AddPIMEmployee:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_add_pim_employee(self, setup):
        """Test Case: Add an Employee in PIM"""
        self.logger.info("********** Test Add Employee in PIM **********")
        self.driver = setup
        self.driver.get(self.baseURL)

        # Login
        self.logger.info("Logging into OrangeHRM")
        self.login = LoginPage(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()

        try:
            # Navigate to PIM and Add Employee
            self.logger.info("Navigating to PIM Page")
            self.pim = PIMPage(self.driver)
            self.pim.navigate_to_pim()
            self.pim.click_add_employee()
            self.logger.info("Entering Employee Details")
            self.pim.enter_employee_details("John", "Doe")
            self.pim.upload_employee_image("C:\\Users\\Admin\\Desktop\\download.jpeg")
            self.pim.save_employee()

            # Validation Step
            toast_message = "Employee addition failed"  # Default in case of Timeout

            try:
                toast_message = self.pim.is_employee_added()
            except TimeoutException:
                self.logger.error("Failed to validate employee addition. Timeout occurred.")

            assert "Successfully Saved" in toast_message, f"Unexpected success message: {toast_message}"

        except Exception as e:
            self.logger.error(f"Test case failed due to error: {str(e)}")
            assert False, f"Test case failed: {str(e)}"
