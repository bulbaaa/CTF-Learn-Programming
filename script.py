with open ("data.dat") as file:
    numbers = file.readlines()
    counter = 0

    for i in numbers:
        if (i.count("1") % 2 == 0) or (i.count("0") % 3 == 0):
            counter += 1

    print(counter)
