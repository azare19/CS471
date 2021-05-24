from ._anvil_designer import sign_upTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import custom_signup.login_flow

class sign_up(sign_upTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def create_account_btn_click(self, **event_args):
    custom_signup.login_flow.signup_with_form()
    self.update_login_status()



