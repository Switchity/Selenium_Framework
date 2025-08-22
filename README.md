or create a new repository on the command line
echo "# Selenium_Framework" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/Switchity/Selenium_Framework.git
git push -u origin master



…or push an existing repository from the command line
git remote add origin https://github.com/Switchity/Selenium_Framework.git
git branch -M master
git push -u origin master

# 📘 Selenium Framework (Python + Pytest + POM)

A **scalable and maintainable Selenium test automation framework** built using:

* **Python** (Selenium WebDriver)
* **Pytest** (test runner, fixtures, reporting)
* **Page Object Model (POM)** (clean separation of test logic & locators)
* **Config-driven setup** (environment variables & `.env`)
* **HTML & Allure Reports** (for test reporting)

---

## 📂 Project Structure

```
selenium_framework/
│── tests/
│   ├── test_login.py         # Login test cases
│   ├── test_search.py        # Search test cases (example)
│   └── test_checkout.py      # Checkout flow test cases
│
│── pages/
│   ├── base_page.py          # Common Selenium methods (wrapper)
│   ├── login_page.py         # Login page object
│   ├── search_page.py        # Search page object
│   └── checkout_page.py      # Checkout page object
│
│── utils/
│   ├── config.py             # Config (URLs, credentials, browser)
│   ├── helpers.py            # Waits, screenshots, utilities
│   └── logger.py             # Logging setup
│
│── conftest.py               # Pytest fixtures (browser setup/teardown)
│── requirements.txt          # Dependencies
│── pytest.ini                # Pytest settings
│── README.md                 # Documentation
```

---

## 🚀 Features

* ✅ **Cross-browser support** (Chrome, Firefox, Edge)
* ✅ **Page Object Model (POM)** for scalability
* ✅ **Environment-driven config** via `.env` file
* ✅ **Logging & screenshots** on failures
* ✅ **HTML & Allure reports** for execution results
* ✅ **Pytest-xdist** for **parallel execution**
* ✅ **CI/CD ready** (Jenkins, GitHub Actions, GitLab CI)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/selenium_framework.git
cd selenium_framework
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create `.env` File

Create a `.env` file in project root:

```ini
BASE_URL=https://the-internet.herokuapp.com
USERNAME=tomsmith
PASSWORD=SuperSecretPassword!
BROWSER=chrome
```

You can switch browsers by changing `BROWSER` to `firefox` or `edge`.

---

## 🧪 Running Tests

### Run All Tests

```bash
pytest
```

### Run Specific Test File

```bash
pytest tests/test_login.py
```

### Run Tests by Marker

```bash
pytest -m login
```

### Run Tests with HTML Report

```bash
pytest --html=report.html --self-contained-html
```

### Run Tests in Parallel (4 threads)

```bash
pytest -n 4
```

---

## 📊 Reports

### Pytest-HTML Report

Generates an interactive HTML report (`report.html`).

### Allure Report (Optional)

1. Install allure:

   ```bash
   pip install allure-pytest
   ```
2. Run tests with allure output:

   ```bash
   pytest --alluredir=allure-results
   ```
3. Serve allure report:

   ```bash
   allure serve allure-results
   ```

---

## 📸 Screenshots on Failure

* Screenshots are captured automatically when a test fails.
* Saved in `screenshots/` directory with timestamp.

---

## 🏗️ Extending the Framework

* Add a new **page object** under `pages/` (e.g., `product_page.py`).
* Write tests for it under `tests/`.
* Reuse `BasePage` methods (`click`, `type`, `get_text`, `wait_for_element`).
* Store sensitive data in `.env`, never hardcode credentials.

---

## 🔗 CI/CD Integration

You can integrate this framework with:

* **GitHub Actions** → run tests on push/PR
* **Jenkins** → nightly regression runs
* **Docker + Selenium Grid** → distributed execution
* **BrowserStack/Sauce Labs** → cross-browser/cloud execution

---

## 📚 Example Test (Login)

```python
import pytest
from pages.login_page import LoginPage
from utils.config import Config

@pytest.mark.login
def test_valid_login(driver):
    page = LoginPage(driver)
    page.open_login_page()
    page.login(Config.USERNAME, Config.PASSWORD)
    assert "You logged into a secure area!" in page.get_flash_message()
```

---

## 👨‍💻 Author

* **Your Name** – Automation Engineer
* 💼 Expertise: Python, Django, Selenium, Pytest, CI/CD
* 🌐 [LinkedIn/GitHub Profile](https://github.com/your-username)

---

## 🏆 Why This Framework?

✔ Clean separation of test logic & locators
✔ Easy to scale for larger applications
✔ Supports parallel & cross-browser execution
✔ Ready for enterprise CI/CD pipelines

---

👉 Would you like me to also **add GitHub Actions CI/CD YAML** so this project can run Selenium tests automatically on every push/PR?
