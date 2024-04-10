attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

food = input("Do you want vegetarian food? ")
print('We recommend Veggie Delight Caterers!' if food == "yes" else "We recommend Gourmet Meals Caterers!")