def describe_city(city_name, country='iceland'):
    """description on city"""
    msg = f"\n{city_name.title()} is in {country.title()}."
    print(msg)
    
describe_city('reykjavik')
describe_city(city_name='akureyri')
describe_city(city_name='kuala lumpur', country='malaysia')