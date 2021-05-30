from ._anvil_designer import WelcomePageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..import AuthFlow

class WelcomePage(WelcomePageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def sign_up_btn_click(self, **event_args):
    AuthFlow.signup_with_form()
    pass



