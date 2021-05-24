from ._anvil_designer import sign_upTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class sign_up(sign_upTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def create_account_btn_click(self, **event_args):
    if self.password_textbox.text != self.repeat_password_textbox.text:
      self.error_label.text = "Please make sure that the passwords are same!"
      self.password_textbox.border = "#FF0000"
    else:
      resp = anvil.server.call('_do_signup', self.email_textbox.text, 
                                              self.full_name_textbox.text, 
                                              self.password_textbox.text, 
                                              self.user_role_drop_down.selected_value)





