
luna = input("introduceti_luna: \n")

while not luna.isnumeric():
    luna = input("luna incorecta")
    
luna =int(luna)

if luna <= 0:
    print("luna gresita")
elif luna > 12:
    print("luna gresita")
elif luna in (12, 1, 2,):
    print('este iarna')
elif luna in (3,4,5):
    print("este primavara")
elif luna in (6,7,8):
    print("este vara")
elif luna in (9,10,11):
    print("este toamna")