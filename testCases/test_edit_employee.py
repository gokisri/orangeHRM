import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.Edit_employee import EmployeeListPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from selenium.common.exceptions import TimeoutException

class TestEditEmployee:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def login_to_application(self, driver):
        """Reusable login method to authenticate into OrangeHRM"""
        self.logger.info("Logging into OrangeHRM")
        driver.get(self.baseURL)

        login_page = LoginPage(driver)
        login_page.setUserName(self.username)
        login_page.setPassword(self.password)
        login_page.clickLogin()
        self.logger.info("✅ Successfully logged into OrangeHRM")

    @pytest.mark.regression
    def test_edit_employee_details(self, setup):
        """Test Case: Edit First Employee in Employee List"""
        self.logger.info("********** Test Edit Employee Details **********")
        self.driver = setup

        try:
            # ✅ Use reusable login method
            self.login_to_application(self.driver)

            # ✅ Navigate to PIM and then to Employee List
            emp_list = EmployeeListPage(self.driver)
            emp_list.navigate_to_pim()  # Navigate to PIM first
            emp_list.open_employee_list()  # Then click Employee List

            # ✅ New employee details
            new_first_name = "John"
            new_last_name = "Doe"

            # ✅ Edit and save employee details
            emp_list.edit_first_employee(new_first_name, new_last_name)

            # ✅ Assert success message
            success_message = emp_list.verify_success_message()
            assert success_message == "Successfully Saved", f"❌ Expected success message not found: {success_message}"

            self.logger.info("✅ Employee details updated successfully!")

        except TimeoutException:
            self.logger.error("❌ Employee edit failed due to timeout.")
            assert False, "Timeout error!"

        except Exception as e:
            self.logger.error(f"❌ Test case failed due to error: {str(e)}")
            assert False, f"Test case failed: {str(e)}"
