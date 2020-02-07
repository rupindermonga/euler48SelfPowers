'''
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''

def SelfPowers(n,x):
    # n power n with last x digits
    total = sum(pow(i, i) for i in range(1, n + 1))
    return str(total)[-x:]

final = SelfPowers(1000,10)
print(final)