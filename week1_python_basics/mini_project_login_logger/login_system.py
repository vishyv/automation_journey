from datetime import datetime

def login_logger():
    correct_user = 'admin'
    correct_pwd = 'pass123'

    for attempt in range(3):
        user_usrnm = input('Enter the user name: ')
        user_usrpwd = input('Enter the password: ')

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if user_usrnm == correct_user and user_usrpwd == correct_pwd:
            print('Login Successful!!')
            log_line = f'{timestamp} User {user_usrnm} -> Login Successful\n'
            with open('log.txt', 'a') as f:
                f.write(log_line)
            return 'Login Completed'
        else:
            print ('Invalid creds, try again :(')
            log_line = f"{timestamp} User {user_usrnm} -> Login unsuccessful\n"
            with open('log.txt', 'a') as f:
                f.write(log_line)

    print('Exhausted attempts, try again later')
    with open('log.txt', 'r') as f:
        print('Previous login attempts: ')
        print(f.read())
    return 'Login failed'

print(login_logger())