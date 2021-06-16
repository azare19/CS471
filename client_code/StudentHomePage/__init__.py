from ._anvil_designer import StudentHomePageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class StudentHomePage(StudentHomePageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.username_label.text = anvil.users.get_user()['name']
    

  def loan_calculator_link_click(self, **event_args):
    open_form('PaymentCalculator')

