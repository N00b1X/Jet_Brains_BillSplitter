import random

print("Enter the number of friends joining (including you):")
persons = int(input())

friends = {}
if persons <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for friend in range(persons):
        name = input()
        friends[name] = 0

    print("Enter the total bill value:")
    bill = int(input())
    personal_bill = "{:.2f}".format(bill / persons)

    friends = {x: float(personal_bill) for x in friends}

    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
    lucky = input()

    if lucky == "No":
        print("No one is going to be lucky")
        print()
        print(friends)

    elif lucky == "Yes":
        lucky_one = random.choice(list(friends.keys()))
        print("{} is the lucky one!".format(lucky_one))
        print()
        bill = "{:.2f}".format((float(bill) / (persons - 1)))
        friends = {x: float(bill) for x in friends}
        friends[lucky_one] = 0
        print(friends)
