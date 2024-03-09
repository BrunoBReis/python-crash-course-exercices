def describe_city(city, country='Unknown'):
    """Describes a city"""
    print(f"{city} is in {country}.")

# Calling the function for three different cities
describe_city('Reykjavik', 'Iceland')
describe_city('New York', 'United States')
describe_city('Paris')  # Default country will be 'Unknown'