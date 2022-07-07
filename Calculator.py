n = input("Hello, please enter you name: ")
print("\nWelcome,", n,"\nNice to meet you!")
print("\nThis calculator 🧮 helps with simple algebric equations.\n Let's get started!")
o = input("\n*ONLY input lowercase*: \n\na - addition, \ns - subtraction, \nm - multiplication, \nsq - squared, \nd - division, \np - pi, \npn - positive/negative, \nc - comparing, \nr - random \n\nEnter the operation : ")

if o == "a":
    an1 = input("\nEnter the first number *ONLY input numbers*: ")
    an2 = input("\nEnter the second number *ONLY input numbers*: ")
    answer = (int(an1) + int(an2))
    print("\nHere's your sum: ", answer,"\nAwesome!")

if o == "s":
    sn1 = input("\nEnter the first number *ONLY input numbers*: ")
    sn2 = input("\nEnter the second number *ONLY input numbers*: ")
    answer = (int(sn1) - int(sn2))
    print("\nHere's your difference: ", answer, "\nSplendid!")

if o == "m":
    mn1 = input("\nEnter the multiplicand *ONLY input numbers*: ")
    mn2 = input("\nEnter the multiplicator *ONLY input numbers*: ")
    answer = (int(mn1) * int(mn2))
    print("\nHere's the product:", answer,"\nMarvelous!")
    
if o == "sq":
    an1 = input("\nEnter the number *ONLY input numbers*: ")
    an2 = input("\nEnter the power *ONLY input numbers*: ")
    answer = (int(an1) ** int(an2))
    print("\nHere's your square: ", answer, "\nSuper!")
    
if o == "d":
    dn1 = input("\nEnter the dividend *ONLY input numbers*: ")
    dn2 = input("\nEnter the divisor *ONLY input numbers*: ")
    answer = (int(dn1) / int(dn2))
    print("\nHere's the quotient:", answer,"\nDashing!")

if o == "p":
    print("\nπ = 3.1415926535897932384626433832795 \nπ ≈ 3.14")

if o == "pn":
    pnn = input("\n± Enter the number *ONLY input numbers*: ")
    if pnn > '0':
        print("\nHere's your result: \n", pnn, "is positive. \nPerfect!")
    if pnn < '0':
        print("\nHere's your result: \n", pnn, "is negative. \nNice!")
    if pnn == '0':
        print("\nHere's your result: \n", pnn, "is neither positive nor negative. \nPerfectly Nice!")

if o == "c":
    cn1 = input("\nEnter the first number *ONLY input numbers*: ")
    cn2 = input("\nEnter the second number *ONLY input numbers*: ")
    if cn1 > cn2:
        print("\nHere's your comparision: ", cn1, "> (greater than)", cn2, "\nComparing Incredible!")
    if cn1 < cn2:
        print("\nHere's your comparision: ", cn1, "< (less than)", cn2, "\nComparing Incredible!")
    elif cn1 == cn2:
        print("\nHere's your comparision: ", cn1, "= (equal to)", cn2, "\nComparing Incredible!")

if o == "r":
    import random
    max = int(input("\nEnter the maximum value of range: "))
    r = random.randint(1, max)
    print("\nHere's your random value: ", r, "\n\nRan-tastic!")

restart = input("\nWant to input a new equation? (ONLY answer lowercase 'yes' or 'no'): ")

while restart == "yes":
    o = input("\n*ONLY input lowercase*: \n\na - addition, \ns - subtraction, \nm - multiplication, \nsq - squared, \nd - division, \np - pi, \npn - positive/negative, \nc - comparing, \nr - random \n\nEnter the operation : ")

    if o == "a":
        an1 = input("\nEnter the first number *ONLY input numbers*: ")
        an2 = input("\nEnter the second number *ONLY input numbers*: ")
        answer = (int(an1) + int(an2))
        print("\nHere's your sum: ", answer,"\nAwesome!")

    if o == "s":
        sn1 = input("\nEnter the first number *ONLY input numbers*: ")
        sn2 = input("\nEnter the second number *ONLY input numbers*: ")
        answer = (int(sn1) - int(sn2))
        print("\nHere's your difference: ", answer, "\nSplendid!")

    if o == "m":
        mn1 = input("\nEnter the multiplicand *ONLY input numbers*: ")
        mn2 = input("\nEnter the multiplicator *ONLY input numbers*: ")
        answer = (int(mn1) * int(mn2))
        print("\nHere's the product:", answer,"\nMarvelous!")
    
    if o == "sq":
        an1 = input("\nEnter the number *ONLY input numbers*: ")
        an2 = input("\nEnter the power *ONLY input numbers*: ")
        answer = (int(an1) ** int(an2))
        print("\nHere's your square: ", answer, "\nSuper!")
    
    if o == "d":
        dn1 = input("\nEnter the dividend *ONLY input numbers*: ")
        dn2 = input("\nEnter the divisor *ONLY input numbers*: ")
        answer = (int(dn1) / int(dn2))
        print("\nHere's the quotient:", answer,"\nDashing!")

    if o == "p":
        print("\nπ = 3.1415926535897932384626433832795 \nπ ≈ 3.14")

    if o == "pn":
        pnn = input("\n± Enter the number *ONLY input numbers*: ")
        if pnn > '0':
            print("\nHere's your result: \n", pnn, "is positive. \nPerfect!")
        if pnn < '0':
            print("\nHere's your result: \n", pnn, "is negative. \nNice!")
        if pnn == '0':
            print("\nHere's your result: \n", pnn, "is neither positive nor negative. \nPerfectly Nice!")

    if o == "c":
        cn1 = input("\nEnter the first number *ONLY input numbers*: ")
        cn2 = input("\nEnter the second number *ONLY input numbers*: ")
        if cn1 > cn2:
            print("\nHere's your comparision: ", cn1, "> (greater than)", cn2, "\nComparing Incredible!")
        if cn1 < cn2:
            print("\nHere's your comparision: ", cn1, "< (less than)", cn2, "\nComparing Incredible!")
        elif cn1 == cn2:
            print("\nHere's your comparision: ", cn1, "= (equal to)", cn2, "\nComparing Incredible!")

    if o == "r":
        import random
        max = int(input("\nEnter the maximum value of range: "))
        r = random.randint(1, max)
        print("\nHere's your random value: ", r, "\n\nRan-tastic!")

    restart = input("\nWant to input a new equation? (Answer lowercase 'yes' or 'no'): ")

while restart == "no":
    print("\nSorry to see you go! You can use this calculator anytime and anywhere.")
    f = input("\nWant to give feedback? \nPlease tell us about your experience [Answer lowercase: 'good', 'bad', or 'so-so'.]: ")
    if f == 'good':
        print("\nThat's good to hear! Glad you enjoyed it. Thank you!")
        quit()
    if f == 'bad':
        print("\nSorry to hear that! \nPlease go here to report your issues: https://forms.gle/2qWwFUsXWBam7VYd7.")
        print("\nThank you for using Idea Calculator,",n,"! Have an awesome day ☀ ~")
        quit()
    if f == 'so-so':
        print("\nAnything we can do better to improve your experience? \n\nPlease go here to tell us about what you think: https://forms.gle/2qWwFUsXWBam7VYd7")
        print("\nThank you for using Idea Calculator,",n,"! Have an awesome day ☀ ~")
        quit()
