
# Туристические агентства предлагают следующие туры.
# Вояж - Мексика,Канада,Израиль, Италия, США.
# Рейна Тур - Англия, Япония, Канада, ЮАР.
# Радуга - США,Испания, Швеция, Австралия.
# Определить в каких турагенствах можно приобрести туры в Канаду, а в каких в США


voyage = {"Мексика", "Канада", "Израиль", "Италия", "США"}
reyna_tour = {"Англия", "Япония", "Канада", "ЮАР"}
raduga = {"США", "Испания", "Швеция", "Австралия"}


canada_agencies = {"Вояж"} if "Канада" in voyage else set()
canada_agencies |= {"Рейна Тур"} if "Канада" in reyna_tour else set()
canada_agencies |= {"Радуга"} if "Канада" in raduga else set()

usa_agencies = {"Вояж"} if "США" in voyage else set()
usa_agencies |= {"Рейна Тур"} if "США" in reyna_tour else set()
usa_agencies |= {"Радуга"} if "США" in raduga else set()

print(f"Туры в Канаду можно приобрести в: {', '.join(canada_agencies)}")
print(f"Туры в США можно приобрести в: {', '.join(usa_agencies)}")
