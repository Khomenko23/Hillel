import re
password_score = 0
pattern = r'[@_!#$%^&*()<>?/\|}{~:]'
number = r'[1234567890]'
uppers = r'[QWERTYUIOPASDFGHJKLZXCVBNM]'
lowers = r'[qwertyuiopasdfghjklzxcvbnm]'
recommendations = ''

password = input('Please enter your password:')

if len(password) >= 8:
    password_score += 1
else:
    error1 = 'The minimum password length is 8'
    recommendations += error1 + '\n'

if re.findall(number, password):
    password_score += 1
else:
    error2 = 'Use digits'
    recommendations += error2 + '\n'

if re.findall(uppers, password):
    password_score += 1
else:
    error3 = 'Use capitals'
    recommendations += error3 + '\n'

if re.findall(lowers,password):
    password_score += 1
else:
    error4 = 'Use lowers'
    recommendations += error4 + '\n'

if re.findall(pattern, password):
    password_score += 1
else:
    error5 = 'Use special characters'
    recommendations += error5 + '\n'

print(f'Password score:{password_score}')
if password_score <5:
    print(f'Recommendations:' + '\n' + recommendations)