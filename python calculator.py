
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
print(add(int(input('enter num1:')),int(input('enter num2:'))))


#====================== or ============================

def calculator(num1,num2):
    op=input('enter operator :')
    if op=='+':
        return num1+num2
    elif op=='-':
        return num1-num2
    elif op=='*':
        return num1*num2
    elif op=='/':
        return num1/num2
    elif op=='**':
        return num1**num2
    elif op not in ('+,-,*,/,**'):
        return 'please enter a valid opoerator'
print(calculator(int(input('enter num1:')),int(input('enter num2:'))))
        
