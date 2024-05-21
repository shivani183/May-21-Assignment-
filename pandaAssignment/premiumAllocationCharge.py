# **Total Premium Allocation Charges**

import pandas as pd

def premium_allocation(modal_premium, policy_term):

    if 99999 >= modal_premium >= 50000:         # according to modal premium charges are different
        pac_years = [12, 8, 4, 4, 4]            # PAC percentages for the first 5 years
    elif 199999 >= modal_premium >= 100000:
        pac_years = [6, 3, 3, 3, 3]
    elif 239999 >= modal_premium >= 200000:
        pac_years = [3, 1, 1, 1, 1]
    else:
        pac_years = [0, 0, 0, 0, 0]


    total_pac = 0
    for year, pac_percent in enumerate(pac_years):
        if year < 5:
            pac_amount = modal_premium * pac_percent / 100
            total_pac += pac_amount
            if policy_term-1 == year:
                break

    return total_pac


if __name__ == "__main__":
    excel_file = "inputSheet.xlsx"
    show = pd.read_excel(excel_file)

    policy_term = int(show.iloc[0, 9])
    modal_premium = show.iloc[0, 4]

total_pac=premium_allocation(modal_premium, policy_term)
print("Total Premium Allocation Charge (PAC) is rupees: ", total_pac)
