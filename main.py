import controller
import model
import view
import solveString

if input('Ввести выражение строкой? 1-да, 0-нет ')=='1':
    solveString.SolveExpression(model.somestr)
    view.print_total()
else:
    model.init_first()
    while True:
        if model.init_ops():
            break
        model.init_second()
        controller.operation()
        view.print_total()
        model.first = model.total