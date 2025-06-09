def main():
    i = input("Enter: ")
    convert(i)

def convert(f):
    f = f.replace(":)", "🙂").replace(":(", "🙁")
    print(f)

main()