import pytest
from playwright.sync_api import sync_playwright

#Login tests
def test_valid_login_credentials(page):
    page.locator('input[type="email"]').fill("john.doe@example.com")
    page.locator('input[type="password"]').fill("P@ssw0rd123")
    page.locator('button').click()

#ERROR HANDLING: Invalid email format
# Tests that login fails with invalid email format
def test_invalid_email_login(page):
    page.locator('input[type="email"]').fill("invalid_email_format")
    page.locator('input[type="password"]').fill("short")
    page.locator('button').click()

#ERROR HANDLING: Empty email
# Tests that login fails with empty email
def test_empty_email(page):
    page.locator('input[type="email"]').fill("")
    page.locator('input[type="password"]').fill("noemail@123")
    page.locator('button').click()

#ERROR HANDLING: Empty password
# Tests that login fails with empty password
def test_empty_password(page):
    page.locator('input[type="email"]').fill("harry.potter@hogwarts.edu")
    page.locator('input[type="password"]').fill("")
    page.locator('button').click()

#Successful login with valid credentials
def test_valid_login_credentials_alice(page):
    page.locator('input[type="email"]').fill("alice.smith@example.com")
    page.locator('input[type="password"]').fill("alice@321")
    page.locator('button').click()


def run_tests():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("file:///path/to/your/login.html") # Replace with your HTML file path
        test_valid_login_credentials(page)
        test_invalid_email_login(page)
        test_empty_email(page)
        test_empty_password(page)
        test_valid_login_credentials_alice(page)
        browser.close()

if __name__ == "__main__":
    run_tests()