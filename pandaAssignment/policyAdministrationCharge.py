#  **Total Policy Administration Charges**
import pandas as pd


def policy_administration(modal_premium, pt, premium_frequency):

    # policy_administration charge is nil for the first 5 years as per the policy terms
    # so for first five year charge 0
    # for calculation reducing first five years from pt

    if pt <= 5:
        return 0
    else:
        pt = pt - 5

        # policy_administration charge is = 2.1 % of annual premium
        if premium_frequency == 12:
            charge_p_month = (modal_premium * 2.1/100) / 12

            if charge_p_month <= 500:              # As policy_administration charge is capped at ₹500 per month.
                return 500 * (pt * 12)             # if charge_p_month is less than the cap of ₹500, ₹500 is considered

            else:                                       # if charge_p_month is more than the cap of ₹500,
                return charge_p_month * (pt * 12)       # charge_p_month is considered

        if premium_frequency == 6:                            # when half-yearly premium_frequency, Policy
            charge_p_month = (modal_premium * 2.1 / 100) / 6  # Administration Charge is 2.1% pa so dividing by 6

            if charge_p_month <= 500:
                return 500 * (pt * 12)
            else:
                return charge_p_month * (pt * 12)

        if premium_frequency == 4:                            # when quarterly premium_frequency,Policy
            charge_p_month = (modal_premium * 2.1 / 100) / 4  # Administration Charge is 2.1% pa so dividing by 4

            if charge_p_month <= 500:
                return 500 * (pt * 12)
            else:
                return charge_p_month * (pt * 12)

        if premium_frequency == 1:                              # when monthly premium_frequency,
            charge_p_month = (modal_premium * 2.1 / 100)        # Policy Administration Charge is 2.1% p.a.

            if charge_p_month <= 500:
                return 500 * (pt * 12)
            else:
                return charge_p_month * (pt * 12)


if __name__ == "__main__":
    excel_file = "inputSheet.xlsx"
    show = pd.read_excel(excel_file)

    policy_term = (show.iloc[0, 9])
    modal_premium = show.iloc[0, 4]
    premium_frequency = show.iloc[0, 5]

administration_charge = policy_administration(modal_premium, policy_term, premium_frequency)
print("Total Policy Administration Charges is rupees: ", administration_charge)