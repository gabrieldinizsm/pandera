import pandas as pd
import pandera as pa
import numpy as np
from faker import Faker


def generate_fake_email() -> str:
    """ 
    Função para gerar alguns emails fakes.

    Returns:
        str: Um fake email.
    """
    fake = Faker()
    faker = fake.email()
    return faker
