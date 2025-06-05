
time = input("What time is it? ")

h, m = time.strip().split(':')

h = int(h)
m = int(m)
ot = int(0)

# 60m = 1h
if m >= 60:
    ot = m - 60
    h += 1
    m = ot

if h >= 25:
    h = 1

# Formated time

fm = f"{m:02}"

ft = int(str(h) + str(fm))

if 700 <= ft <= 859:
    print("Breakfast time")
elif 1200 <= ft <= 1359:
    print("Lunch time")
elif 1800 <= ft <= 1959:
    print("Dinner time")
else:
    exit(0)



