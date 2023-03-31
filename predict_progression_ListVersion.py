def add_to_list(msg, c_pass, c_defer, c_fail):
    data_list.append([msg, c_pass, c_defer, c_fail])


def show_list():
    for item in data_list:
        print(item[0], " - ", item[1], ",", item[2], ",", item[3], sep="")


def show_histogram(_pros, _trailers, _retriever, _excludes, total):
    print('-' * 64)
    # indentation out of style because it is a triple quoted formatted string
    print(f'''
Histogram
Progress {_pros}  : {'*' * _pros}
Trailer {_trailers}   : {'*' * _trailers}
Retriever {_retriever} : {'*' * _retriever}
Excluded {_excludes}  : {'*' * _excludes}

{total} outcomes in total
''')
    print('-' * 64)
    print("program is terminated...")


credit = (0, 20, 40, 60, 80, 100, 120)
_pros = 0  # number of progressed students
_trailers = 0  # number of trailed students
_retriever = 0  # number of retrieved students
_excludes = 0  # number of excluded students

data_list = []

while True:  # Using while True with keywords break and False rather than using condition checking
    try:
        c_pass = int(input("Please enter your total PASS credits: "))
        if c_pass not in credit:
            print("Out of range.")
            continue

        while True:
            try:
                c_defer = int(input("Please enter your total DEFER credits: "))
                if c_defer not in credit:
                    print("Out of range.")
                else:
                    break
            except ValueError:  # expecting value errors for inputs
                print("Integer required.")
                continue

        while True:
            try:
                c_fail = int(input("Please enter your total FAIL credits: "))
                if c_fail not in credit:
                    print("Out of range.")
                else:
                    break
            except ValueError:  # expecting value errors for inputs
                print("Integer required.")
                continue

        total_credit = c_pass + c_defer + c_fail

        if total_credit != 120:
            print("Total incorrect.")
            continue

        if c_pass >= 100:
            if c_pass == 120:
                _pros += 1
                msg = "Progress"
                print(msg)
                add_to_list(msg, c_pass, c_defer, c_fail)

            else:
                _trailers += 1
                msg = "Progress (module trailer)"
                print(msg)
                add_to_list(msg, c_pass, c_defer, c_fail)

        else:
            if c_fail >= 80:
                _excludes += 1
                msg = "Exclude"
                print(msg)
                add_to_list(msg, c_pass, c_defer, c_fail)

            else:
                _retriever += 1
                msg = "Do not Progress (module retriever)"
                print(msg)
                add_to_list(msg, c_pass, c_defer, c_fail)

        total = _pros + _trailers + _retriever + _excludes

    except ValueError:  # expecting value errors for inputs
        print("Integer required.")
        continue

    option = input('''
Would you like to enter another set of data?
Enter 'y or any' for yes or 'q' to quit and view results: ''')
    print("")

    if option.lower() == "q":
        show_histogram(_pros, _trailers, _retriever, _excludes, total)
        break

print()
show_list()
print(data_list)
