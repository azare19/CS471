from ._anvil_designer import SignUpDialogTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class SignUpDialog(SignUpDialogTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  
  def focus_name(self):
    """Focus on the name box."""
    self.full_name_txtbx.focus()
  
  def focus_email(self):
    """Focus on the email box."""
    self.email_txtbx.focus()
    
  def focus_password(self, **kws):
    """Focus on the password box."""
    self.password_txtbx.focus()

  def focus_password_repeat(self, **kws):
    """Focus on the password repeat box."""
    self.repeat_password_txtbx.focus()
  
  def account_type_focus(self):
    """Focus on the Account type drop down."""
    self.account_type_dd.focus()
    
  def set_message_box_text(self, text):
    """Set the message box text"""
    self.message_bx.text = text
  
  def close_alert(self, **kws):
     """Close any alert we might be in with 'login' value."""
     self.raise_event('x-close-alert', value=True)
