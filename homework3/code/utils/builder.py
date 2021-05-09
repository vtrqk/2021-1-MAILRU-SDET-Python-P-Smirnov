from dataclasses import dataclass

import faker

fake = faker.Faker()


@dataclass
class Topic:
    name: str = None


class Builder:

    @staticmethod
    def create_segment(name=None):
        if name is None:
            name = fake.bothify(text='???#?#?#???')

        return Topic(name=name)
