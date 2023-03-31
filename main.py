import string
from password_list import PasswordList

digits = string.digits
upper = string.ascii_uppercase
lower = string.ascii_lowercase

char_set = digits + upper + lower
length = 5
write_directory = 'passwords.txt'
log_progress = False

pws = PasswordList(list(char_set), length)
print(pws.amount)
pws.write_to_file(write_directory, log_progress)
pws.display(log_progress)
