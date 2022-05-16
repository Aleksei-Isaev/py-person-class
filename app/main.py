class Person:

    people = {}

    def __init__(self, name, age, wife=None, husband=None):
        self.name = name
        self.age = age

        if husband is not None:
            self.husband = husband
        if wife is not None:
            self.wife = wife

        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    result_list = []

    for person in people:
        name = person['name']
        age = person['age']
        if 'wife' in person:
            wife = person['wife']
            result_list.append(Person(name, age, wife=wife))
        if 'husband' in person:
            husband = person['husband']
            result_list.append(Person(name, age, husband=husband))

    for person in people:
        if 'wife' in person and person['wife'] is not None:
            Person.people[person['name']].wife = Person.people[person['wife']]
        if 'husband' in person and person['husband'] is not None:
            Person.people[person['name']].husband = \
                Person.people[person['husband']]

    return [Person.people[x] for x in Person.people]
