
balance = 5000


def user_unset():
    global balance
    user_unset_sum = int(input("Введите cумму: "))

    if user_unset_sum <= 0:
        print("неверная сумма")
    elif user_unset_sum > balance:
        print("сумма привышает баланс")
    else:
        rest = balance - user_unset_sum
        balance = rest

        print('деньги успешно сняты \n' + str(balance))





def one_use():
    user_answer = input('Продолжить работу?\ntype exit/press enter\n_')
    if user_answer == 'exit':
        return False

    return True


while one_use():
    print('Действия пользователя')


user_unset()



