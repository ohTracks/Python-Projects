import itertools

def main():
    
    inp = input("list: ")
    digits=[]
    for c in str(inp):
        try:
            digit=int(c)
            digits.append(digit)
        except:
            pass
    target = int(input("Target: "))
    twoSum(digits, target)


def twoSum(l, t):

    list = l
    tgt = t
    for n in itertools.combinations(list, 2):
        if sum(n) == tgt:
            print([list.index(number) for number in n])

main()