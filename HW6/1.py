from decimal import Decimal

def create_list(expr):
    num = ''
    op = ''

    for ch in expr:
        if ch.isdigit() or ch == '.':
            num += ch
        elif ch == '-':
            num += ' ' + ch
            op += '+'
        elif ch == ' ':
            continue
        else:
            op += ch
            num += ' '

    num, op = list(map(Decimal, num.split())), list(op)

    def make_operation(sign: str) -> None:
        while sign in op:
            sign_index = op.index(sign)
            first_num = num[sign_index]
            second_num = num[sign_index + 1]
            if sign == '/':
                if second_num == 0:
                    print('Делите на 0')
                    exit()
                num[sign_index] = first_num / second_num
            elif sign == '*':
                num[sign_index] = first_num * second_num

            else:
                num[sign_index] = first_num + second_num


            del num[sign_index + 1]
            del op[sign_index]

    for i in '/*+':
        make_operation(i)

            return num[sign_index]
expression = '1+2*3'
print(create_list(expression))
