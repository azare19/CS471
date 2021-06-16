from ._anvil_designer import PaymentCalculatorTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class PaymentCalculator(PaymentCalculatorTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def calculate_payment_btn_click(self, **event_args):
    monthlyPayment = self.getMonthlyPayment(float(self.loan_amount_txtbx.text), 
                                            float(self.interest_rate_txtbx.text)/1200,
                                           int(self.number_of_years_txtbx.text))
    self.monthly_payment_output_lbl.text = f"{monthlyPayment:.2f}"
    total_payment = float(monthlyPayment) * 12 * int(self.number_of_years_txtbx.text)
    self.total_payment_output_lbl.text = f"{total_payment:.2f}"
    

  def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
    # compute the monthly payment.
    monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
    return monthlyPayment

  def home_btn_click(self, **event_args):
    open_form('StudentHomePage')

