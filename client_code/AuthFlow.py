from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from SignUpDialog import SignUpDialog


def display_message(resp, dlg):
    if resp == -1:
      dlg.message_bx.text = "Invalid Full Name, Try again."
      dlg.focus_name()
    elif resp == -2:
      dlg.message_bx.text = "Invalid Email Address. Try again."
    elif resp == -3:
      dlg.message_bx.text = "Password must not be empty. Try again."
    elif resp == -4:
      dlg.message_bx.text = "Passwords do not match. Try again."
    elif resp == -5:
      dlg.message_bx.text = "User Role not selected. Try again."
    elif resp == -6:
      dlg.message_bx.text = "An account by this email already exists. Try again."

def signup_with_form():
  dlg = SignUpDialog()
  while True:
    if not alert(dlg, title="Sign Up", large=True, buttons=[("Sign Up", True, 'primary'), ("Cancel", False)]):
      # If user clicked the cancel btn
      return
    resp = anvil.server.call('_do_signup', dlg.email_txtbx.text, 
                                              dlg.full_name_txtbx.text, 
                                              dlg.password_txtbx.text, 
                                              dlg.repeat_password_txtbx.text,
                                              dlg.account_type_dd.selected_value)
    dlg.message_bx.text  = "dodo"
    dlg.message_bx.visible = True
    continue
    if resp < 0:
      display_message(resp, dlg)
    else:
      alert(f"We have sent a confirmation email to {d.email_box.text}.\n\nCheck your email, and click on the link.")
      return
    
    
  
  
  