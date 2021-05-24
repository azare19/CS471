import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import re
import bcrypt
    

def hash_password(password, salt):
  """Hash the password using bcrypt in a way that is compatible with Python 2 and 3."""
  if not isinstance(password, bytes):
    password = password.encode()
  if not isinstance(salt, bytes):
    salt = salt.encode()

  result = bcrypt.hashpw(password, salt)

  if isinstance(result, bytes):
    return result.decode('utf-8')

@anvil.server.callable
def _do_signup(email, name, password, repeat_password, account_type):
  if not re.match(r"(?=^.{0,40}$)^[a-zA-Z-]+\s[a-zA-Z-]+$", name):
    return -1
  elif not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]+$", email):
    return -2
  elif len(password) == 0:
    return -3
  elif password != repeat_password:
    return -4
  elif account_type is None:
    return -5
  
  user = app_tables.users.get(email=email.lower())
  if user is None:
    pwhash = hash_password(password, bcrypt.gensalt())
    user = app_tables.users.add_row(name=name.title(),
                                    email=email.lower(),
                                   email_confirmed=False,
                                   password_hash=pwhash,
                                   user_type=account_type)
  else:
    return -6
  return 0
