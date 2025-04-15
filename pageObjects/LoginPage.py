from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, \
    ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage:
    textbox_username_xpath = "//input[@placeholder='Username']"
    textbox_password_name = "password"
    button_login_xpath = "(//button[normalize-space()='Login'])[1]"
    button_dropdown_xpath = "//span[@class='oxd-userdropdown-tab']"
    button_logout_xpath = "//a[contains(text(), 'Logout')]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10 seconds explicit wait

    def setUserName(self, username):
        username_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.textbox_username_xpath)))
        username_field.send_keys(username)

    def setPassword(self, password):
        password_field = self.wait.until(EC.presence_of_element_located((By.NAME, self.textbox_password_name)))
        password_field.send_keys(password)

    def clickLogin(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_login_xpath)))
        login_button.click()

    def clickDropdown(self):
        try:
            dropdown_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_dropdown_xpath)))
            dropdown_button.click()
            print("Dropdown clicked successfully")
        except TimeoutException:
            print("Dropdown button not found!")

    def clickLogout(self):
        try:
            self.clickDropdown()  # Ensure dropdown is opened before logout

            for attempt in range(3):  # Retry up to 3 times in case of a stale element
                try:
                    button_logout = self.wait.until(
                        EC.element_to_be_clickable((By.XPATH, self.button_logout_xpath))
                    )
                    button_logout.click()
                    print("Logout successful")
                    return  # Exit function if logout succeeds

                except StaleElementReferenceException:
                    print(f"Attempt {attempt + 1}: Stale element detected. Retrying logout...")

                except ElementClickInterceptedException:
                    print(f"Attempt {attempt + 1}: Logout button not clickable. Retrying...")

            print("Logout failed after multiple attempts.")

        except TimeoutException:
            print("Logout button not found. Skipping logout.")

        except Exception as e:
            filename = f"logout_error_{int(time.time())}.png"
            self.driver.save_screenshot(filename)  # Save unique screenshot
            print(f"Exception while logging out: {e}")
