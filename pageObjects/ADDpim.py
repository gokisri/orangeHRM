from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Increased wait time to 20s

    # Locators
    menu_pim = (By.XPATH, "//span[text()='PIM']")
    btn_add_employee = (By.XPATH, "//button[normalize-space()='Add']")
    txt_firstname = (By.XPATH, "//input[@placeholder='First Name']")
    txt_lastname = (By.XPATH, "//input[@placeholder='Last Name']")
    image_upload = (By.XPATH, "//input[@type='file']")
    btn_save = (By.XPATH, "//button[normalize-space()='Save']")
    Toast_message = (By.XPATH, "//*[@id='oxd-toaster_1']/div")

    # Methods
    def navigate_to_pim(self):
        self.wait.until(EC.element_to_be_clickable(self.menu_pim)).click()
        print("✅ Navigated to PIM page.")

    def click_add_employee(self):
        self.wait.until(EC.element_to_be_clickable(self.btn_add_employee)).click()
        print("✅ Clicked 'Add Employee' button.")

    def enter_employee_details(self, first_name, last_name):
        self.wait.until(EC.visibility_of_element_located(self.txt_firstname)).send_keys(first_name)
        self.wait.until(EC.visibility_of_element_located(self.txt_lastname)).send_keys(last_name)
        print(f"✅ Entered Employee Name: {first_name} {last_name}")



    def upload_employee_image(self, file_path):
        """Uploads an employee image."""
        try:
            self.wait.until(EC.presence_of_element_located(self.image_upload)).send_keys("C:\\Users\\Admin\\Desktop\\download.jpeg")
            print(f"✅ Uploaded image: {file_path}")
        except Exception as e:
            print(f"❌ Error uploading image: {e}")

    def save_employee(self):
        self.wait.until(EC.element_to_be_clickable(self.btn_save)).click()
        print("💾 Clicked 'Save' button. Waiting for Toast message...")

    def is_employee_added(self):
        """Check if the Toast message appears after adding an employee."""
        try:
            success_element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='oxd-toaster_1']/div"))
            )
            print(f"✅ Toast Message Found: {success_element.text}")
            return success_element.text

        except TimeoutException:
            print("❌ Toast message not found! Debugging page source...")

            # Save page source for debugging
            with open("debug_page_source.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)

            print("🛠 Page source saved to 'debug_page_source.html'. Please check it.")
            return None




