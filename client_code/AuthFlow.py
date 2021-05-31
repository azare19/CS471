from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from SignUpDialog import SignUpDialog


def clear_errors(dlg):
    # Clear Error Msg and Borders
    dlg.message_lbl.text = ""
    dlg.full_name_txtbx.border = ""
    dlg.email_txtbx.border = ""
    dlg.password_txtbx.border = ""
    dlg.repeat_password_txtbx.border = ""
    dlg.account_type_dd.border = ""
    dlg.message_lbl.visible = False

def display_error_message(resp, dlg):
    if resp == -1:
      dlg.message_lbl.text = "Invalid Full Name, Try again."
      dlg.full_name_txtbx.border = "solid #FF0000"
    elif resp == -2:
      dlg.message_lbl.text = "Invalid Email Address. Try again."
      dlg.email_txtbx.border = "solid #FF0000"
    elif resp == -3:
      dlg.message_lbl.text = "Password must alphanmeric and longer than 7 characters"
      dlg.password_txtbx.border = "solid #FF0000"
    elif resp == -4:
      dlg.message_lbl.text = "Passwords do not match. Try again."
      dlg.password_txtbx.border = "solid #FF0000"
      dlg.repeat_password_txtbx.border = "solid #FF0000"
    elif resp == -5:
      dlg.message_lbl.text = "User Role not selected. Try again."
      dlg.account_type_dd.border = "solid #FF0000"
    elif resp == -6:
      dlg.message_lbl.text = "An account by this email already exists. Try again."
    dlg.message_lbl.visible = True

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
    clear_errors(dlg)
    if resp < 0:
      display_error_message(resp, dlg)
    else:
      alert(f"We have sent a confirmation email to {dlg.email_txtbx.text}.\n\nCheck your email, and click on the link.")
      return
    
    
def login_with_form(email, password):
  try:
    anvil.users.login_with_email(email, password, remember=True)
  except anvil.users.EmailNotConfirmed as e:
    return str(e)
  except anvil.users.AuthenticationFailed as e:
    return str(e)
  
  