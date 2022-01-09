''' Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information
you have stored about it. '''

print("My answer:")

cities = {
    'kuala lumpur': {
        'country': 'malaysia',
        'population': 1_808_000,
        'fact': 'famous with Borneo rainforest',
        },

    'paris': {
        'country': 'france',
        'population': 2_161_000,
        'fact': 'famous with Eiffel Tower',
        },

    'london': {
        'country': 'united kingdom',
        'population': 8_982_000,
        'fact': 'biggest city in Europe and ' 
        'largest city in the world'
        },

    }

for city, city_info in cities.items():
    print(f"City: {city.title()}")
    country = city_info['country']
    population = f"{city_info['population']}"
    fact = f"{city_info['fact']}"

    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact[0].upper() + fact[1:]}")
