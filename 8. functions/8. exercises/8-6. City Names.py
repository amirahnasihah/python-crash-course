def city_country(city_name, country):
    """Return a string like 'Santiago, Chile'"""
    return f"{city_name.title()}, {country.title()}"
    
pair = city_country('santiago', 'chile')
print(pair)

pair = city_country('kuala lumpur', 'malaysia')
print(pair)

pair = city_country('soul', 'south korea')
print(pair)