"""
Write the code that will produce the output below. The script should iterate to 
produce the expressions on the left, perform the specified operation to get the 
results shown on the right and print exactly in the format shown.

1 x 8 + 1 = 9
12 x 8 + 2 = 98
123 x 8 + 3 = 987
1234 x 8 + 4 = 9876
12345 x 8 + 5 = 98765
123456 x 8 + 6 = 987654
1234567 x 8 + 7 = 9876543
12345678 x 8 + 8 = 98765432
123456789 x 8 + 9 = 987654321

YOUR NAME: Josiah Schlabach

"""

string = ""

for i in range(1, 10):
    string += str(i)
    tot = int(string) * 8 + i
    print(string + " x 8 + " + str(i) + " = " + str(tot))
