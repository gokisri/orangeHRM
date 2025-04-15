from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.customLogger import LogGen

class EmployeeListPage:
    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Locators
    MENU_PIM = (By.XPATH, "//span[text()='PIM']")
    EMPLOYEE_LIST_TAB = (By.XPATH, "//a[text()='Employee List']")
    FIRST_EMPLOYEE_EDIT_BTN = (By.XPATH, "(//i[contains(@class, 'bi-pencil')])[1]")
    SAVE_BUTTON = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='oxd-toaster_1']/div/div[1]/div[2]/p[2]")

    # Form fields
    FIRST_NAME_FIELD = (By.NAME, "firstName")
    LAST_NAME_FIELD = (By.NAME, "lastName")

    def navigate_to_pim(self):
        """Navigate to the PIM page from the main menu."""
        self.logger.info("Navigating to PIM page")
        self.wait.until(EC.element_to_be_clickable(self.MENU_PIM)).click()

    def open_employee_list(self):
        """Navigate to the Employee List page."""
        self.logger.info("Navigating to Employee List page")
        self.wait.until(EC.element_to_be_clickable(self.EMPLOYEE_LIST_TAB)).click()

    def edit_first_employee(self, new_first_name, new_last_name):
        """Edit the first employee's details."""
        self.logger.info("Editing the first employee in the list")
        self.wait.until(EC.element_to_be_clickable(self.FIRST_EMPLOYEE_EDIT_BTN)).click()

        # Edit employee details
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD)).clear()
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(new_first_name)
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_FIELD)).clear()
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(new_last_name)

        # Save changes
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
        self.logger.info("Clicked the Save button")

    def verify_success_message(self):
        """Verify if the success message is displayed after saving employee details."""
        try:
            # Wait until success message is visible (increased wait time)
            success_msg_element = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
            success_msg = success_msg_element.text
            self.logger.info(f"Success message displayed: {success_msg}")

            # Compare the success message exactly or handle the mismatch if needed
            expected_message = "Successfully Saved"  # Update this with the correct expected message
            if success_msg.strip() == expected_message:  # Use strip() to handle leading/trailing spaces
                return success_msg  # Success message matches
            else:
                self.logger.error(f"Unexpected success message: {success_msg}")
                return None  # Return None if the message doesn't match
        except Exception as e:
            self.logger.error(f"Error: Success message not found! {str(e)}")
            return None  # Return None to indicate failure
