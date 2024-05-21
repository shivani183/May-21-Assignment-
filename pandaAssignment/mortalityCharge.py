# **Total Mortality Charges**

import pandas as pd
from datetime import datetime


def estimate_mortality_charges(rcd_age, premium, mortality_rates, curDate, rcd):

    year = curDate.year - rcd.year

    if curDate.month < rcd.month or (curDate.month == rcd.month and curDate.day < rcd.day):
        year -= 1

    if rcd_age <= 20:
        avg_yearly_charge = premium * mortality_rates[20] / 1000
    elif 21 <= rcd_age >= 30:
        avg_yearly_charge = premium * mortality_rates[30] / 1000
    elif 31 <= rcd_age >= 40:
        avg_yearly_charge = premium * mortality_rates[40] / 1000
    elif 41 <= rcd_age >= 50:
        avg_yearly_charge = premium * mortality_rates[50] / 1000
    elif 51 <= rcd_age >= 50:
        avg_yearly_charge = premium * mortality_rates[60] / 1000
    else:
        avg_yearly_charge = premium * mortality_rates[60] / 1000

    total_charge = avg_yearly_charge * year

    print("Estimated total mortality charges after", year, "years is rupees: ", total_charge)


if __name__ == "__main__":

    mortality_rates = {20: 0.71, 30: 0.75, 40: 1.29, 50: 3.40, 60: 8.56}

    excel_file = "inputSheet.xlsx"
    show = pd.read_excel(excel_file)

    rcd = (show.iloc[0, 6])
    dob = show.iloc[0, 1]
    premium = show.iloc[0, 4]
    my_curDate = datetime.now()

    rcd_age = rcd.year - dob.year

    if rcd.month < dob.month or (rcd.month == dob.month and rcd.day < dob.day):
        rcd_age -= 1

    estimate_mortality_charges(rcd_age, premium, mortality_rates, my_curDate, rcd)

