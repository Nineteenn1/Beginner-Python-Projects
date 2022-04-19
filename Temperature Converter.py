def getinput():
    print("Enter the temperature")
    a = float(input())
    return a
def Converter():
    print("Press 1 for Fahrenheit to Celsius\nPress 2 for Celsius to Fahrenheit")
    x = int(input())
    if x == 1:
       a = getinput()
       return (a - 32) * 5/9
    if x == 2:
        a = getinput()
        return (a + 32) * 9/5

print(Converter())
