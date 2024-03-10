def build_profile(first: str, last: str, **user_info: dict):
    """Build an dictionary of people"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


person = build_profile('bruno', 'reis',
                       location='brasilia', age=21,
                       hobbie='music')

print(person)