from ._anvil_designer import sign_upTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re

class sign_up(sign_upTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  
  
  def clear_errors(self):
    self.error_label.text = ""
    self.full_name_textbox.border = ""
    self.email_textbox.border = ""
    self.password_textbox.border = ""
    self.repeat_password_textbox.border = ""
    self.user_role_drop_down.border = ""
  
  def display_error(self, resp):
    if resp == -1:
      self.error_label.text = "Invalid Full Name, Try again."
      self.full_name_textbox.border = "solid #FF0000"
    elif resp == -2:
      self.error_label.text = "Invalid Email Address. Try again."
      self.email_textbox.border = "solid #FF0000"
    elif resp == -3:
      self.error_label.text = "Password must not be empty. Try again."
      self.password_textbox.border = "solid #FF0000"
    elif resp == -4:
      self.error_label.text = "Passwords do not match. Try again."
      self.password_textbox.border = "solid #FF0000"
      self.repeat_password_textbox.border = "solid #FF0000"
    elif resp == -5:
      self.error_label.text = "User Role not selected. Try again."
      self.user_role_drop_down.border = "solid #FF0000"


  def create_account_btn_click(self, **event_args):
    resp = anvil.server.call('_do_signup', self.email_textbox.text, 
                                              self.full_name_textbox.text, 
                                              self.password_textbox.text, 
                                              self.repeat_password_textbox.text,
                                              self.user_role_drop_down.selected_value)
    self.clear_errors()
    if resp < 0:
      self.display_error(resp)
            




