balance = 5000
log = []

def one_use():
    user_answer = input('Продолжить работу?\ntype exit/press enter\n_')
    if user_answer == 'exit':
        return False

    return True

def set_log(сhoice):
    if choice == '1':
        log.append("Choose currency")
    elif choice == '2':
        log.append("Show balance")
    elif choice == '3':
        log.append("Put money")
    elif choice == '4':
        log.append("Get money")


while one_use():
    print('Действия пользователя')
