START_TEXT = "π <i>Hey {} \nWelcome to our subscription bot.</i>\n\n<b>Please send me the id given " \
             "from the website to process subscription.</b>"

INVALID_TEXT = "πYou have entered invalid ID.\nPlease send valid ID given from website."

STATUS_TEXT = """.                    πUser Status                    .

π Username  β {}
π± Subscription β {}
β»οΈ Registered Date β {}

π°Upgrade Your Subscription Below π°"""

PREMIUM_TEXT = """β<u>οΈ Premium </u>βοΈ

β <b>50 Requests per day


β JSON Output


β Multiple Digit Recognition

π΅ Payment β 10Birr</b>"""

PLATINUM_TEXT = """π± <u>Platinum</u> π±οΈ

β <b>50 Requests per day


β JSON Output


β Multiple Digit Recognition

π΅ Payment β 20Birr</b>"""

PAYMENT_TEXT = "<b>Select your payment method π</b>"

TELEBIRR_PAY_TEXT = """Please follow the instructions to pay for your subscription using Tele Birr.

1οΈβ£ Dial *127#
2οΈβ£ Enter 1 -> Send Money
3οΈβ£ Select 1 -> Send Money again.
4οΈβ£ Select 1 -> By Receiver mobile number 
5οΈβ£ Enter <code>963143774</code> as receiver phone number
6οΈβ£ Enter <b>{}</b> as an Amount.
7οΈβ£ Enter 1 and then Enter your Telebirr PIN to complete  Payment
8οΈβ£ Come Back to the Bot and Click On verify Payment."""

CBEBIRR_PAY_TEXT = """Please follow the instructions to recharge your account using CBE Birr.

1οΈβ£ Dial *847# 
2οΈβ£ Choose 1 (Send Money)
3οΈβ£ Enter <code>936657024</code> as a  phone number.
4οΈβ£ Enter <b>{}</b>  -> Amount to recharge.
5οΈβ£ Enter your PIN.
6οΈβ£ Enter 1 to confirm payment.
7οΈβ£ Come Back to the Bot and Click On verify Payment."""

TELEBIRR_REF_TEXT = """Please Enter the Transaction ID you received from TELEBIRR by SMS.
Your transaction ID will look like 9ECDC8F2AS.
 ππΎππΎ /cancel to cancel"""

CBEBIRR_REF_TEXT = """Please Enter the Transaction ID you received from CBE Birr by SMS.
Your transaction ID will look like 9ECDC8F2AS.
 ππΎππΎ /cancel to cancel"""

INVALID_ID_TEXT = """Invalid Transaction ID.

Please Enter correct transaction Id or click /cancel to cancel."""

LESS_PAY_TEXT = "We have received your payment but you payed " \
                "less from said amount so contact our admins for further." \
                "\n\n@BiniTech\n@MikiGode\n@Itachiinthesky"
