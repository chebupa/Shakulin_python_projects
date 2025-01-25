
def count_guests(guests):
    guest_quantity: int = 0
    for guest in guests: guest_quantity += 1

    if guest_quantity == 0:
        print("Никто не пришел на вечеринку")
    elif guest_quantity == 1:
        print(f"На вечеринке {guests[0]}")
    elif guest_quantity == 2:
        print(f"На вечеринке {guests[0]} и {guests[1]}")
    else:
        print(f"На вечеринке {guests[0]}, {guests[1]} и {guests.__len__() - 2} остальных")

count_guests(["Гость1", "Гость2", "Гость3", "Гость4"])
