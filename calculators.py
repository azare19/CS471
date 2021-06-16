import pandas
import numpy as np
import numpy_financial as npf
from datetime import date

def mortgageCalculator( interest, years, payments_year, loan):
    start_date = date.today()
    d1 = start_date.strftime("%d/%m/%Y")

    rng = pandas.date_range(d1, periods=years * payments_year, freq='MS')
    rng.name = "Payment Date"
    df = pandas.DataFrame(index=rng, columns=['Payment', 'Principal Paid', 'Interest Paid', 'Ending Balance'], dtype='float')
    df.reset_index(inplace=True)
    df.index += 1
    df.index.name = "Period"
    
    #Monthly Payment
    pmt = -1 * npf.pmt(interest/12, years*payments_year, loan)

    #Interest Payment
    ipmt = -1 * npf.ipmt(interest/payments_year, df.index, years*payments_year, loan)

    #Principal Payment
    ppmt = -1 * npf.ppmt(interest/payments_year, df.index, years*payments_year, loan)


    df["Payment"] = pmt
    df["Principal Paid"] = ppmt
    df["Interest Paid"] = ipmt

    df = df.round(2)

    df["Ending Balance"] = 0
    df.loc[1, "Ending Balance"] = loan - df.loc[1, "Principal Paid"]

    for i in range(2, len(df) + 1):
        previous_balance = df.loc[i-1, 'Ending Balance']
        principal_paid = df.loc[i, "Principal Paid"]

        if previous_balance == 0:
            df.loc[i, ['Payment', 'Principal Paid', 'Interest Paid', 'Ending Balance']] == 0
            continue
        elif principal_paid <= previous_balance:
            df.loc[i, 'Ending Balance'] = previous_balance - principal_paid

    print(df)

def riskCalculator( age, annual_income, housing, savings, credit_score):
    if age < 18 or age > 70:
        age_risk = 5
    elif age >= 18 & age < 25:
        age_risk = 4
    elif age >= 25 & age < 35:
        age_risk = 2
    else:
        age_risk = 1

    if annual_income < 30000:
        income_risk = 5
    elif annual_income >= 30000 & annual_income < 50000:
        income_risk = 4
    elif annual_income >= 50000 & annual_income < 70000:
        income_risk = 3
    elif annual_income >= 70000 & annual_income < 100000:
        income_risk = 2
    else:
        income_risk = 1

    if housing == "own":
        housing_risk = 1
    elif housing == "rent":
        housing_risk = 3
    elif housing == "mortgage":
        housing_risk = 4

    if savings < 10000:
        savings_risk = 5
    elif savings >= 10000 & savings < 20000:
        savings_risk = 4



    
    

test = mortgageCalculator(.012,7,12,165000)
    