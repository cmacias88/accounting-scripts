"""Print out all the melons in our inventory."""

from melons import melon_dictionary

def print_melon_profile(melon_dictionary):
    """Print each melon with corresponding attribute information."""

    for melon, traits in melon_dictionary.items():
        print(melon.upper())
        print()
        for trait, value in traits.items():
            print(f'{trait}: {value}')
        print()

print(print_melon_profile(melon_dictionary))

# for i in melon_names:
#     print_melon(melon_names[i], melon_prices[i], melon_seedlessness[i])
