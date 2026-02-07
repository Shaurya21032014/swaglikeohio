def checkifsame(number1, number2):

    if ((number1^ number2)!= 0):
        print("number are not equal")
    else:
        print("both number are equal")

number1 = int(input("enter 1 number to compare"))
number2 = int(input("enter 2 number to compare"))


checkifsame(number1, number2)