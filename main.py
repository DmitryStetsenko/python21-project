balance = 5000
current_currency = "uah"


def one_use():
    user_answer = input('Продолжить работу?\ntype exit/press enter\n_')
    if user_answer == 'exit':
        return False

    return True


def show_balance():
    print("Ваш банас составляет:",balance)


def choose_currency():
    global balance
    choose = input("Enter currency: (1 - usd / 2- uah)")
    if choose == "1":
        if current_currency == "usd":
            print("your balance = ", balance, "usd")
        elif current_currency == "uah":
            balance = balance / 36.93
            print("your balance = ", balance, "usd")
    if choose == "2":
        if current_currency == "uah":
            print("your balance = ", balance, "uah")
        elif current_currency == "usd":
            balance = balance * 36.93
            print("your balance = ", balance, "uah")


while one_use():
    print('Действия пользователя')

    choose_action = input("1 - Choose currency \n2 - Show balance")
    if choose_action == "1":
        choose_currency()
    if choose_action == "2":
        show_balance()


