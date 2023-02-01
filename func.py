import re


def to_fixed(num_obj: float, digits=0):
    """
        :param num_obj: transfer number.
        :param digits: a number of simbols after comma.


        :return: str number
    """
    return f"{num_obj:.{digits}f}"


def put_money(balance):
    """
    :param balance: transfer the balance

    :return: will return the updated balance
    """
    inp_user = input("Enter the amount : ").replace(',', '.')
    inp_user = (re.findall(r'-[0-9.,]+|[0-9.,]+', inp_user))
    try:
        true_inp_user = float(inp_user[0])
        true_inp_user = to_fixed(true_inp_user, 2)

        return float(true_inp_user) + balance
    except TypeError:
        print('Ведите число!')
