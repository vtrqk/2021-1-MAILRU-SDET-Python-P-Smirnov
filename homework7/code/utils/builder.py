from dataclasses import dataclass

import faker

fake = faker.Faker()


@dataclass
class Topic:
    name: str = None
    surname: str = None
    job: str = None


class Builder:

    @staticmethod
    def create_name(name=None):
        if name is None:
            name = fake.first_name()

        return Topic(name=name)

    @staticmethod
    def create_surname(surname=None):
        if surname is None:
            surname = fake.last_name()

        return Topic(name=surname)

    @staticmethod
    def create_job(job=None):
        if job is None:
            job = fake.job()

        return Topic(name=job)
