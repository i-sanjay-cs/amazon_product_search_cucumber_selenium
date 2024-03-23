import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from behave import given, then

# Define step definitions
@given(u'I am on the Login page URL "https://www.amazon.in/"')
def open_browser_and_search(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.amazon.in/")
    context.driver.maximize_window()


@then(u'I click on sign in button and wait for sign in page')
def open_sign_in_page(context):
    # Code to click on sign in button
    sign_in_dropdown = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav-link-accountList-nav-line-1")))
    sign_in_dropdown.click()

    # Wait for 5 seconds
    time.sleep(5)

    # Verify if Sign In Page is displayed
    assert "Sign In" in context.driver.title

@then(u'I should see Sign In Page')
def sign_in_page_opened(context):
    print("Signed in page Successfully")
    time.sleep(5)

@when(u'I enter username as "username"')
def entering_username(context):
    # Locate the username field and enter the username
    username_field = WebDriverWait(context.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#ap_email")))
    username_field.send_keys("username")
    time.sleep(3)

@when(u'I Click on Continue button')
def clicked_continue(context):
    # Locate the Continue button and click on it
    continue_button = WebDriverWait(context.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#continue")))
    continue_button.click()
    time.sleep(3)

@when(u'I enter password as "password"')
def entering_password(context):
    # Locate the password field and enter the password
    password_field = WebDriverWait(context.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#ap_password")))
    password_field.send_keys("password")

@when(u'click on login button')
def click_login(context):
    # Click on the Sign In button
    sign_in_button = WebDriverWait(context.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#signInSubmit")))
    sign_in_button.click()
    time.sleep(3)

@then(u'I am logged in')
def logged_in(context):
    print("Successfully Logged In")


@then(u'I search different "laptops" from the search bar')
def search_laptops(context):
    search_product(context, "laptops")

@then(u'I search different "pendrive" from the search bar')
def search_pendrive(context):
    search_product(context, "pendrive")

@then(u'I search different "led tv" from the search bar')
def search_led_tv(context):
    search_product(context, "led tv")

def search_product(context, product):
    # Click on the search bar
    search_bar = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#twotabsearchtextbox")))
    search_bar.click()

    # Input the product into the search bar
    search_bar.send_keys(product)

    # Press Enter key to submit the search
    search_bar.send_keys(Keys.ENTER)

    # Wait for search results to load
    time.sleep(5)

@then(u'I search different "<products>" from the search bar')
def search_for_product(context, products):
    # Click on the search bar
    search_bar = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#twotabsearchtextbox")))
    search_bar.click()
    

    # Input the product into the search bar
    search_bar.send_keys(products)

    # Press Enter key to submit the search
    search_bar.send_keys(Keys.ENTER)
    time.sleep(5)

@then(u'I exit the browser')
def exit_browser(context):
    # Quit the browser
    context.driver.quit()
    print("Browser exited")
