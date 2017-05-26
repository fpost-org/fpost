from behave import *

@when (u'I go to the fPost home page')
def step_impl(context):
    context.browser.get('http://localhost:5000')

@then(u'I should see that the title is "fPost"')
def step_impl(context):
    assert context.browser.title == "fPost"