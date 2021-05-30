from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from SignUpDialog import SignUpDialog


def signup_with_form():
  dlg = SignUpDialog()
  
  while True:
    if not alert(dlg, title="Sign Up", large=True, buttons=[("Sign Up", True, 'primary'), ("Cancel", False)]):
      # If user clicked the cancel btn
      return
    
    
  
  
  