# **Total Loyalty Additions**
import pandas as pd


def loyalty_add(policy_term, modal_premium_year):

    loyalty_additions = {
        10: 0.15,  # 15% of one Annualized Premium for 10 years
        15: 0.20,  # 20% of one Annualized Premium for 15 years
        20: 0.25,  # 25% of one Annualized Premium for 20 years
        25: 0.30   # 30% of one Annualized Premium for 25 years
    }

    loyalty = loyalty_additions.get(policy_term)

    if loyalty is not None:
        return "Total Loyalty rate for", policy_term, "years is rupees:", loyalty * modal_premium_year
    else:
        return "Total Loyalty rate for", policy_term, " years not found in data."


if __name__ == "__main__":
    excel_file = "inputSheet.xlsx"
    show = pd.read_excel(excel_file)

    pt = int(show.iloc[0, 9])
    modal_premium = show.iloc[0, 4]

str1 = loyalty_add(pt, modal_premium)
print(str1)
