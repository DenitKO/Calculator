import logger

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

somestr = '2*2/4'

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

    firstList = []
    firstList = somestr.replace(' * ', ' *').replace('*', ' *').replace(' / ', ' /').replace('/', ' /').split()
    print(firstList)

    for i in range(len(firstList)):
        firstList[i]=SolveParentheses(firstList[i])
    print(firstList)

    first = 0
    second = 0
    total = 0
    operation = mult
    if len(firstList)>1:
        for i in range(0, len(firstList)):
            if i == 0:
                first = int(firstList[0].replace('(', '').replace(')', ''))
            else:
                if firstList[i][:1] == '*':
                    operation = mult
                elif firstList[i][:1] == '/':
                    operation = div
                second = int(firstList[i][1:].replace('(', '').replace(')', ''))
                total = operation(first, second)
                first = total
    else:
        logger.logger(f'{somestr} = {firstList[0]}')
        return firstList[0]
    logger.logger(f'{somestr} = {total}')
    return total