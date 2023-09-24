# 1

try:
    hour = int(input("Enter hours: "))
    rate = float(input("Enter rate: "))
except:
    print("Error, please enter a numeric number!")
else:
    if hour > 40:
        extra_hours = hour - 40
        extra_rate = rate * 1.5
        salary = (40 * rate) + (extra_hours * extra_rate)
        print("Pay: "+str(float(salary)))
    else:
        salary = hour * rate
        print("Pay: " + str(salary))

# 2

score = int(input("Enter Score: "))

if score>=90 and score<=100:
    print("Grade is A")
elif score>=80 and score<=90:
    print("Grade is B")
elif score>=70 and score<=80:
    print("Grade is C")
elif score>=60 and score<=70:
    print("Grade is D")
elif score >= 0 and score <= 60:
    print("Grade is F")
else:
    print("Error, please enter numeric input between 0 and 100")
    
# 3    

total = 0
count = 0    
while True:
    try:
        inp = input('Enter a number: ')
        if inp == 'done': 
            break
        value = float(inp)
        total = total + value
        count = count + 1
        average = total / count
    except:
        print("invalid input. enter a number")

print("Sum of input numbers: ", total)
print("Number of input: ", count)
print('Average of input numbers: ', average)

    

    
