import logger
import model

def mult (a,b):
    c=a*b
    return c

def div (a,b):
    c=a/b
    return c


def IsParentheses (somestr):
    for i in somestr:
        if i == '(':
            return True


def SolveParentheses (somestr:str):

    # Находим выражение в скобках
    inParentheses = ''
    for i in range(0, len(somestr)):
        if somestr[i] =='(':
            i += 1
            while somestr[i] != ')':
                inParentheses += somestr[i]
                i += 1
    
    # Потготовка выражения для вычисления
    firstList = []
    firstList = inParentheses.replace(' + ', ' +').replace('+', ' +').replace(' - ', ' -').replace('-', ' -').split()

    # Вычисляем значение в скобках, с условием что вырожение простое по примеру x+y или x-y
    total = 0
    for i in range(len(firstList)):
        firstList[i] = firstList[i].replace('+', '')
        total += int(firstList[i])

    # Заменяем вычесленный результат в основной текст
    if total < 0:
        somestr = somestr.replace(inParentheses, str(total))
    else:
        somestr = somestr.replace('('+inParentheses+')', str(total))
    return somestr


def SolveExpression (somestr:str):
    model.somestr = input('Введите выражение строкой, пример (1-3)*(2+4)/(-4-4): ')

    firstList = []
    firstList = model.somestr.replace(' * ', ' *').replace('*', ' *').replace(' / ', ' /').replace('/', ' /').split()

    for i in range(len(firstList)):
        firstList[i]=SolveParentheses(firstList[i])

    # first = 0
    # second = 0
    # total = 0
    operation = mult
    if len(firstList)>1:
        for i in range(0, len(firstList)):
            if i == 0:
                model.first = int(firstList[0].replace('(', '').replace(')', ''))
            else:
                if firstList[i][:1] == '*':
                    operation = mult
                elif firstList[i][:1] == '/':
                    operation = div
                model.second = int(firstList[i][1:].replace('(', '').replace(')', ''))
                model.total = operation(model.first, model.second)
                model.first = model.total
    else:
        logger.logger(f'{model.somestr} = {firstList[0]}')
        return firstList[0]
    logger.logger(f'{model.somestr} = {model.total}')
    return model.total