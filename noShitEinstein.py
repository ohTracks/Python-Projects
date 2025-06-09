def main():
    m = int(input("Mass: "))
    emc(m)

def emc(s):
    c = 9*10**16

    E = s * c
    print(f"E = {E} Joules")

main()


