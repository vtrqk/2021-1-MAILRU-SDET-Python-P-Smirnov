from dataclasses import dataclass

import faker

fake = faker.Faker()


class Builder:

    @staticmethod
    def create_name(name=None):
        if name is None:
            name = fake.first_name()

        return name

    @staticmethod
    def create_surname(surname=None):
        if surname is None:
            surname = fake.last_name()

        return surname

    @staticmethod
    def create_job(job=None):
        if job is None:
            job = fake.job()

        return job
