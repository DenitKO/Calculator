import controller
import model
import view
import solveString

if input('Ввести выражение строкой? 1-да, 0-нет ')=='1':
    somestr = input('Введите выражение строкой, пример (1-3)*(2+4)/(-4-4): ')
    solveString.SolveExpression(somestr)
else:
    model.init_first()
    while True:
        if model.init_ops():
            break
        model.init_second()
        controller.operation()
        view.print_total()
        model.first = model.total