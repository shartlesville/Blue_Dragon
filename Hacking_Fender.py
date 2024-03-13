import csv

compromised_users = []

with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    compromised_users.append(password_row['Username'])

with open('compromised_users.txt', 'w') as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user)

import json

with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {"recipient": 'The Boss', "message": 'Mission Success'}
  json.dump(boss_message_dict, boss_message)

with open("new_passwords.csv", 'w') as new_passwords_obj:
  slash_null_sig = """  _  _     ___   __  ____   \n          
/ )( \   / __) /  \(_  _)            \n
) \/ (  ( (_ \(  O ) )(              \n
\____/   \___/ \__/ (__)             \n
 _  _   __    ___  __ _  ____  ____  \n
/ )( \ / _\  / __)(  / )(  __)(    \ \n
) __ (/    \( (__  )  (  ) _)  ) D ( \n
\_)(_/\_/\_/ \___)(__\_)(____)(____/ \n
        ____  __     __   ____  _  _ \n
 ___   / ___)(  )   / _\ / ___)/ )( \\n
(___)  \___ \/ (_/\/    \\___ \) __ (\n
       (____/\____/\_/\_/(____/\_)(_/\n
 __ _  _  _  __    __                \n
(  ( \/ )( \(  )  (  )               \n
/    /) \/ (/ (_/\/ (_/\             \n
\_)__)\____/\____/\____/"""
  new_passwords_obj.write(slash_null_sig)
