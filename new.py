n = int(input("Enter the number of rows of the pattern"))
x = input("Enter the character you want to print")
for i in range(1,int(n),1):
    for j in range(1,int(n),1):
        print(x, end = " ")
    print()