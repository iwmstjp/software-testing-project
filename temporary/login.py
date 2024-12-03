from behave import *
from hamcrest import assert_that, equal_to
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("the home page is opened")
def step_impl(context):
    context.homepage.open_page()

@given("the '{field}' field is filled with '{text}'")
def step_impl(context, field, text):
    field = '' if field == '[blank]' else field
    text = '' if text == '[blank]' else text
    context.homepage.fill_out_field(field, text)

@given("the '{button}':login button is clicked")
def step_impl(context, button):
    context.homepage.click_button(button)

@when("the '{button}':login button is clicked")
def step_impl(context, button):
    context.homepage.click_button(button)

@when("the '{option}' option is clicked")
def step_impl(context, option):
    context.homepage.click_option_button(option)

@given("the '{link}' link is clicked")
def step_impl(context, link):
    context.homepage.click_button(link)

@given("the '{item}' cart button is clicked")
def step_impl(context, item):
    item = '' if item == '[blank]' else item
    if(item != ''):
        context.homepage.click_item_cart_button(item)

@given("the '{button}' button is clicked")
def step_impl(context, button):
    context.homepage.click_button(button)

@given("the '{button}' item button is clicked")
def step_impl(context, button):
    context.homepage.click_item_button(button)

@given("the '{button}' removed button is clicked")
def step_impl(context, button):
    button = '' if button == '[blank]' else button
    if(button != ''):
        context.homepage.click_item_remove_button(button)

@when("the '{button}' button is clicked")
def step_impl(context, button):
    context.homepage.click_button(button)

@when("the '{button}' item button is clicked")
def step_impl(context, button):
    context.homepage.click_item_button(button)

@then("the '{error}' message is shown")
def step_impl(context, error):
    assert_that(context.homepage.get_error_message(), equal_to(error))


@then("the '{error}' message(Checkout) is shown")
def step_impl(context, error):
    assert_that(context.homepage.get_error_message_checkout(), equal_to(error))

@then("the '{item_name}' is top")
def step_impl(context, item_name):
    assert_that(context.homepage.get_top_item_name(),equal_to(item_name))

@then("the '{page}' page is shown")
def step_impl(context, page):
    assert_that(context.homepage.get_current_url(),equal_to(page))

@then("the '{text}' is shown")
def step_impl(context, text):
    assert_that(context.homepage.get_current_url_full(),equal_to(text))

@then("the '{media}' icon is shown")
def step_impl(context, media):
    assert_that(context.homepage.get_social(media),equal_to(media))

@then("the 'Cart_count'  is '{number}'. Remove '{item1}' and '{item2}'")
def step_impl(context, number, item1, item2):
    assert_that(context.homepage.get_cart_count(),equal_to(number))
    item1 = '' if item1 == '[blank]' else item1
    item2= '' if item2 == '[blank]' else item2
    if(item1 != ''):
        context.homepage.click_item_remove_button(item1)
    if(item2 != ''):
        context.homepage.click_item_remove_button(item2)

@then("the 'Cart_count'  is '{number}'. Reset state")
def step_impl(context, number):
    assert_that(context.homepage.get_cart_count(),equal_to(number))
    context.homepage.click_button("Menu")
    context.homepage.click_button("Reset")

@then("the About page is shown")
def step_impl(context):
    assert_that(context.homepage.get_current_p(),equal_to("The world relies on your code. \
                Test on thousands of different device, browser, and OS configurations–anywhere, any time."))