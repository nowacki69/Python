def no_side_effects(cities):
	print(cities)
	cities = cities + ["Birmingham","Bradford"]
	print(cities)


def side_effects(cities):
	print(cities)
	cities += ["Birmingham","Bradford"]
	print(cities)


locations = ["London","Leeds","Glasgow","Sheffield"]
no_side_effects(locations)
print(locations)

print('\n\n\n')


locations = ["London","Leeds","Glasgow","Sheffield"]
side_effects(locations)
print(locations)

print('\n\n\n')


locations = ["London","Leeds","Glasgow","Sheffield"]
side_effects(locations[:])
print(locations)
