# Count to p and print each number
p= int(input("Enter the value of p: "))
def count_to_p(x = p):
    for i in range(1, x + 1):
        print(i, end=' ')
    print()

print("Going to count to {} . . .".format(p))
count_to_p(p)