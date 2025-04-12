# Import smtplib for the actual sending function
import smtplib

import requests
# Import the email modules we'll need
from email.mime.text import MIMEText

with open("free_output.txt") as file:
    for line in file:
        usage_value = float(line)

token_id = []
with open("token_and_id.txt") as file:
    for line in file:
        token_id.append(line)

cap_value = .7

print(token_id)

chat_id = token_id[0].strip("\n")
TOKEN = token_id[1].strip("\n")
message = 'Atenção! O uso da RAM do pcrites1 está acima de {}%! Atualmente, seu uso é de aproximadamente: {}%'.format(cap_value * 100, 100 * usage_value)

if usage_value > cap_value:
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()
