def check_conditions(credit_01, credit_02):
    if credit_01 >= 100:
        if credit_01 == 120:
            print("Progress")
        else:
            print("Progress (module trailer)")
    else:
        if credit_02 >= 80:
            print("Exclude")
        else:
            print("Do not Progress – module retriever")


credit = (0, 20, 40, 60, 80, 100, 120)

while True:  # Using while True with keywords break and False rather than using condition checking
    try:
        c_pass = int(input("Please enter your total PASS credits: "))
        if c_pass not in credit:
            print("Out of range.")
            continue

        while True:
            c_defer = int(input("Please enter your total DEFER credits: "))
            if c_defer not in credit:
                print("Out of range.")
            else:
                break

        while True:
            c_fail = int(input("Please enter your total FAIL credits: "))
            if c_fail not in credit:
                print("Out of range.")
            else:
                break

        total_credit = c_pass + c_defer + c_fail

        if total_credit != 120:
            print("Total incorrect.")
            continue

        check_conditions(c_pass, c_fail)
        break

    except ValueError:  # expecting value errors for user inputs
        print("Integer required.")
