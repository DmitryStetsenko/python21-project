balance = 5000


def one_use():
    user_answer = input('Продолжить работу?\ntype exit/press enter\n_')
    if user_answer == 'exit':
        return False

    return True


while one_use():
    print('Действия пользователя')
    def Show_Balace():
        print(balance)
