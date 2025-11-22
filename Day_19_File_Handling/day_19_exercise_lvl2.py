#Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re
with open('./DATA/email_exchange_big.txt') as f1:
    data=f1.read()
    print(data)
