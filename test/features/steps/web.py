from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

@given('website "{url}"')
def step(context, url):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get(url)
    
@then('title becomes "{title}"')
def step(context, title):
    assert context.browser.title == title