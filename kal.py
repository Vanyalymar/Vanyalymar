#Ебать какой простой калькулятор

vi = 0
a = 0
b = 0


vi = str(input("что нужно сделать: "));
a = float(input("Введите первое число: "))
b  = float(input("Введите второе число: "))
t =  ('Результат: ')

if vi == '+':
    print (t)

    print (a+b)
    

elif vi == '-':
    print(a-b)
    print (t)
elif vi == '/':
  
    print(a/b)
    print (t)
elif vi == '*':

    print (t)
    print(a*b)

    
