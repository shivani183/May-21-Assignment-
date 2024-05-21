# **Revival Amount**

from datetime import datetime
import pandas as pd


def revival_amount(surDate, last_premiumDate):

    year = surDate.year - last_premiumDate.year
    modal_premium = 50000
    if surDate.month < last_premiumDate.month or (surDate.month == last_premiumDate.month and surDate.day < last_premiumDate.day):
        year -= 1
    return year * modal_premium


if __name__ == "__main__":
    excel_file = "inputSheet.xlsx"
    show = pd.read_excel(excel_file)

    my_surDate = show.iloc[0, 13]
    my_last_premiumDate = show.iloc[0, 14]

    revival_charge = revival_amount(my_surDate, my_last_premiumDate)

    print("Your revival charge is rupees:", revival_charge)