START_TEXT = "👋 <i>Hey {} \nWelcome to our subscription bot.</i>\n\n<b>Please send me the id given " \
             "from the website to process subscription.</b>"

INVALID_TEXT = "😕You have entered invalid ID.\nPlease send valid ID given from website."

STATUS_TEXT = """.                    🗞User Status                    .

🌀 Username  ➖ {}
🔱 Subscription ➖ {}
♻️ Registered Date ➖ {}

🔰Upgrade Your Subscription Below 🔰"""

PREMIUM_TEXT = """⚜<u>️ Premium </u>⚜️

✅ <b>50 Requests per day


✅ JSON Output


❌ Multiple Digit Recognition

💵 Payment ➖ 10Birr</b>"""

PLATINUM_TEXT = """🔱 <u>Platinum</u> 🔱️

✅ <b>50 Requests per day


✅ JSON Output


✅ Multiple Digit Recognition

💵 Payment ➖ 20Birr</b>"""

PAYMENT_TEXT = "<b>Select your payment method 👇</b>"

TELEBIRR_PAY_TEXT = """Please follow the instructions to pay for your subscription using Tele Birr.

1️⃣ Dial *127#
2️⃣ Enter 1 -> Send Money
3️⃣ Select 1 -> Send Money again.
4️⃣ Select 1 -> By Receiver mobile number 
5️⃣ Enter <code>963143774</code> as receiver phone number
6️⃣ Enter <b>{}</b> as an Amount.
7️⃣ Enter 1 and then Enter your Telebirr PIN to complete  Payment
8️⃣ Come Back to the Bot and Click On verify Payment."""

CBEBIRR_PAY_TEXT = """Please follow the instructions to recharge your account using CBE Birr.

1️⃣ Dial *847# 
2️⃣ Choose 1 (Send Money)
3️⃣ Enter <code>936657024</code> as a  phone number.
4️⃣ Enter <b>{}</b>  -> Amount to recharge.
5️⃣ Enter your PIN.
6️⃣ Enter 1 to confirm payment.
7️⃣ Come Back to the Bot and Click On verify Payment."""

TELEBIRR_REF_TEXT = """Please Enter the Transaction ID you received from TELEBIRR by SMS.
Your transaction ID will look like 9ECDC8F2AS.
 👇🏾👇🏾 /cancel to cancel"""

CBEBIRR_REF_TEXT = """Please Enter the Transaction ID you received from CBE Birr by SMS.
Your transaction ID will look like 9ECDC8F2AS.
 👇🏾👇🏾 /cancel to cancel"""

INVALID_ID_TEXT = """Invalid Transaction ID.

Please Enter correct transaction Id or click /cancel to cancel."""

LESS_PAY_TEXT = "We have received your payment but you payed " \
                "less from said amount so contact our admins for further." \
                "\n\n@BiniTech\n@MikiGode\n@Itachiinthesky"
