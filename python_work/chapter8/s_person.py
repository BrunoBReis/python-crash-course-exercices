def build_person(first_name: str, last_name: str, age=None):
    """Return a dictionary of a person"""
    person = {
        'first': first_name.title(),
        'last': last_name.title()}
    if age:
        person['age'] = age
    return person


person = build_person('bruno', 'reis')
print(person)
person1 = build_person('bruno', 'reis', 21)
print(person1)