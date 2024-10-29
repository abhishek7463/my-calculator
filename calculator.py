A=int(input("enter the vale of first no."))
B=int(input("enter the value of second no."))
symbol=str(input("enter the operator :"))
match symbol:
    case "+":
        print("sum of two no. is",A+B)
    case "-":
        print("difference of two no. is",A-B)
    case "*":
        print("multiplication of two no. is",A*B)
    case "/":
        print("the divion between two no. is",A/B)
    case "%":
        print("average of  two no.",(A+B)/2)
    case _:
        print("wrong symbols")