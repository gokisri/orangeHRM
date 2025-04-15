from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    MENU_PIM = (By.XPATH, "//span[text()='PIM']")
    EMPLOYEE_LIST_TAB = (By.XPATH, "//a[text()='Employee List']")
    FIRST_EMPLOYEE_DELETE_BUTTON = (By.XPATH, "(//i[@class='oxd-icon bi-trash'])[1]")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[text()=' Yes, Delete ']")

    def navigate_to_pim(self):
        """Navigate to the PIM page."""
        self.wait.until(EC.element_to_be_clickable(self.MENU_PIM)).click()
        print("✅ Navigated to PIM Page")

    def click_employee_list(self):
        """Click on the Employee List tab to ensure it's loaded."""
        self.wait.until(EC.element_to_be_clickable(self.EMPLOYEE_LIST_TAB)).click()
        print("✅ Clicked Employee List tab.")

        # ✅ Ensure the table is fully loaded before proceeding
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='oxd-table-body']")))
            print("✅ Employee List Loaded.")
        except:
            print("❌ Employee List did not load!")
            self.driver.save_screenshot("error_employee_list_not_loaded.png")
            raise Exception("Employee List did not load properly!")

    def delete_first_employee(self):
        """Click the delete button for the first employee directly."""
        try:
            # ✅ Click the Delete Button (No checkbox selection)
            delete_button = self.wait.until(EC.element_to_be_clickable(self.FIRST_EMPLOYEE_DELETE_BUTTON))
            delete_button.click()
            print("✅ Clicked Delete button.")

            # ✅ Click Confirm Delete Button
            confirm_button = self.wait.until(EC.element_to_be_clickable(self.CONFIRM_DELETE_BUTTON))
            confirm_button.click()
            print("✅ Confirmed deletion.")

        except Exception as e:
            print(f"❌ Error in deleting employee: {e}")
            self.driver.save_screenshot("error_delete_button_not_found.png")
            raise
