cities = {
    'New York': {
        'country': 'United States',
        'population': 8_336_817,
        'fact': 'The city that never sleeps',
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 37_393_000,
        'fact': 'Hosted the 1964 Summer Olympics',
    },
    'Paris': {
        'country': 'France',
        'population': 2_140_526,
        'fact': 'Known as the City of Love',
    },
}

# Print information about each city
for city, infos in cities.items():
    print(f'{city}')
    for info, data in infos.items():
        print(f'\t{info} = {data}')
