from ._anvil_designer import WelcomePageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import AuthFlow
from ..ForgottenPasswordDialog import ForgottenPasswordDialog


class WelcomePage(WelcomePageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def sign_up_btn_click(self, **event_args):
    AuthFlow.signup_with_form()

  def reset_password_link_click(self, **event_args):
    fp = ForgottenPasswordDialog(self.email_textbox.text)
    
    if alert(fp, title='Forgot Password', buttons=[("Reset password", True, "primary"), ("Cancel", False)]):
        if anvil.server.call('_send_password_reset', fp.email_box.text):
          alert(f"A password reset email has been sent to {fp.email_box.text}.")
        else:
          alert("That username does not exist in our records.")

  def sign_in_btn_click(self, **event_args):
    resp = AuthFlow.login_with_form(self.email_textbox.text, self.password_textbox.text)
    if resp:
      self.message_lbl.text = resp
      self.message_lbl.visible = True
    else:
      self.message_lbl.visible = False
    
    print(anvil.users.get_user()['email'])





