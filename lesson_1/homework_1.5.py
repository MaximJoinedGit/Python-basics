"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

profit = input('Введите выручку фирмы: ')
exps = input('Введите издержки фирмы: ')

if profit.isdigit() and exps.isdigit():
    profit, exps = int(profit), int(exps)
fin_year = profit - exps

if fin_year > 0:
    print('Год был успешным, компания получила прибыль.')
    gain = profit / exps
    print(f'Прибыль компании в этом году {gain:.2%}')
staff = input('Введите количество сотрудников: ')

if staff.isdigit():
    staff = int(staff)
    profit_by_employee = profit / staff
    print(f'{profit_by_employee}! Столько компании принес каждый сотрудник.')
else:
    print('Компания за год только потеряла деньги.')
