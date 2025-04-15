# OrangeHRM Automation Framework

This project is an automated testing framework for the [OrangeHRM](https://www.orangehrm.com/) web application. It is built using **Python**, **Pytest**, and follows a **hybrid framework** approach including **data-driven testing**, **Page Object Model (POM)**, and HTML reporting.

---

## 🧰 Tech Stack

- **Language:** Python
- **Test Framework:** Pytest
- **IDE:** PyCharm
- **Reporting:** HTML Reports
- **Design Pattern:** Page Object Model (POM)
- **Logging:** Custom Logger
- **Other Features:** Config reader, screenshots on failure, multi-browser support

---

## 📁 Project Structure

nopcommerce-project/ │ ├── Configurations/ # config.ini - stores browser & URL configs ├── Logs/ # Execution logs ├── pageObjects/ # Page Object Model classes ├── Reports/ # HTML reports with assets ├── Screenshots/ # Screenshots captured on failures ├── Test Data/ # Test data files ├── testCases/ # Pytest test cases │ ├── test_login.py │ ├── test_login_ddt.py │ ├── test_ADDpim.py │ ├── test_delete_pim_employee.py │ ├── test_edit_employee.py │ └── conftest.py # Fixtures and hooks ├── Utilities/ # Custom utilities (logger, config reader) │ ├── customLogger.py │ └── readProperties.py └── pytest.ini # Pytest configuration file

---

## ✅ Implemented Test Cases

1. **Login Test with Data Driven Method**  
   - Verifies login using multiple positive and negative credentials from test data.
   - Uses DDT (Data Driven Testing) to loop through user/pass combinations.

2. **Login Process and Title Verification**  
   - Validates successful login and checks the page title.

3. **Add New Employee**  
   - Adds a new employee in the PIM module and verifies successful entry.

4. **Delete Existing Employee**  
   - Deletes an employee entry and confirms successful deletion.

5. **Edit Employee Information**  
   - Edits personal details of an existing employee and saves changes.

---

## 🧪 How to Run Tests

Make sure to activate the virtual environment and install dependencies:

```bash
pip install -r requirements.txt


Then execute the tests using:
pytest -v --html=Reports/report.html

To run a specific test:
pytest testCases/test_login.py

Screenshots & Reports
HTML report is automatically generated in the Reports/ folder.
Screenshots are captured for failed test cases and stored in the Screenshots/ folder.

Configuration
Update the following in Configurations/config.ini:
[common info]
baseURL = https://opensource-demo.orangehrmlive.com/
username = Admin
password = admin123
browser = chrome



Future Improvements

Integrate with CI/CD pipelines (e.g., GitHub Actions, Jenkins) for automated testing.
Enhance cross-browser testing capabilities.
Expand test cases to include employee search and advanced filtering.
Implement additional validations for UI components like dropdowns, date pickers, etc.




