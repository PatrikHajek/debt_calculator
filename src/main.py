from typing import NamedTuple, Optional

INPUT_EXIT = "continue"
INPUT_PROMPT = "Enter person: "
INPUT_PREAMBULE = """Provide name and money using CSV format (<name>;<money>);
use whatever currency you want just keep it the same for all people\n"""
VALIDATION_ERROR_MESSAGE = "Invalid input, try again"


class Person(NamedTuple):
    name: str
    payed: float
    owes: float = 0


def parse_input(value: str) -> Optional[Person]:
    splits = value.split(";")
    if len(splits) != 2:
        return None
    elif splits[0] == "" or splits[1] == "":
        return None
    else:
        return Person(name=splits[0], payed=float(splits[1]))


def calculate_total(people: list[Person]) -> float:
    sum = 0
    for person in people:
        sum += person.payed
    return sum


def calculate_owed(people: list[Person]) -> list[Person]:
    total = calculate_total(people)
    person_owes = total / len(people)
    for i in range(0, len(people)):
        person = people[i]
        people[i] = Person(
            name=person.name, payed=person.payed, owes=person_owes - person.payed
        )
    return people


def output(people: list[Person]) -> str:
    out = "\n"
    total = calculate_total(people)
    out += f"Total: {total}\n"
    out += "---------------\n"
    for person in people:
        out += f"{person.name}: {person.owes}\n"
    return out


def main():
    people: list[Person] = []
    print(INPUT_PREAMBULE)
    while True:
        value = input(INPUT_PROMPT)
        validated = parse_input(value)
        if value == INPUT_EXIT:
            break
        elif validated == None:
            print(VALIDATION_ERROR_MESSAGE)
        else:
            people.append(validated)

    people = calculate_owed(people)
    print(output(people))


if __name__ == "__main__":
    main()
