class Person:
    people = {}
    def __init__(self, name: str, age: int):

        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = [Person(p["name"], p["age"]) for p in people]

    for p in people:
        person = Person.people[p["name"]]
        if p.get("wife"):
            person.wife = Person.people[p["wife"]]
        if p.get("husband"):
            person.husband = Person.people[p["husband"]]

    return persons