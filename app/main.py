class Person:
    people = {}
    def __init__(self, name: str, age: int):

        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []
    for p in people:
        person = Person(p["name"], p["age"])
        persons.append(person)

    for p in people:
        person = Person.people[p["name"]]
        if p.get("wife"):
            person.wife = Person.people[p["wife"]]
        if p.get("husband"):
            person.husband = Person.people[p["husband"]]

    return persons