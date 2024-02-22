import pandas as pd
import pandera as pa
import numpy as np
from faker import Faker


np.random.seed(42)


def generate_fake_email() -> str:
    """ 
    Função para gerar alguns emails fakes.

    Returns:
        str: Um fake email.
    """
    fake = Faker()
    faker = fake.email()
    return faker


def generate_fake_df(num_rows: int) -> pd.DataFrame:
    """
    Função para gerar um DataFrame mockado com colunas pré-definidas e valores aleatórios.

    O Dataframe consistirá em 6 colunas: 
        string_column: String que irá variar entre apple, banana e grape
        int_column: Inteiro que varia de 1 a 100
        float_column: Float que varia de 1.0 a 100.0
        datetime_column: Datetime que irá variar entre 2010-01-01' e '2024-12-31'
        email_column: String em formato fake de email.

    Args:
        num_rows(int): Um inteiro informado o número de linhas fakes no dataframe.

    Returns:
        pd.DataFrame: Um pandas Dataframe contendo registros fakes.
    """

    try:

        data = {}

        data['string_column'] = np.random.choice(
            ['apple', 'banana', 'grape'], size=num_rows)

        data['int_column'] = np.random.randint(1, 100, size=num_rows)

        data['float_column'] = np.random.uniform(1.0, 100.0, size=num_rows)

        data['datetime_column'] = pd.to_datetime(np.random.choice(
            pd.date_range('2010-01-01', '2024-12-31'), size=num_rows))

        data['email_column'] = [generate_fake_email()
                                for _ in range(num_rows)]

        return pd.DataFrame(data)

    except Exception as e:
        raise (e)


if __name__ == '__main__':

    df = generate_fake_df(10)