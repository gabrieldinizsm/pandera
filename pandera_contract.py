import pandas as pd
import pandera as pa
import numpy as np
from faker import Faker
from datetime import datetime


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


schema = pa.DataFrameSchema({
    'string_column': pa.Column(str, checks=[
        pa.Check(lambda x: x.str.isalpha(),
                 error="Only alphabet lettters alowed"),
        pa.Check(lambda x: x.isin(
            ['grape', 'apple', 'banana']), error="Unknown fruit")
    ]),
    'int_column': pa.Column('int32', checks=[
        pa.Check(lambda x: x >= 1,
                 error="Value should be equal or higher than 1"),
        pa.Check(lambda x: x <= 10,
                 error="Value should be equal or lower than 100")
    ]),
    'float_column': pa.Column('float64'),
    'datetime_column': pa.Column('datetime64'),
    'email_column': pa.Column(str, checks=[
        pa.Check.str_contains('@', error="Email must contain @"),
        pa.Check.str_contains('.', error="Email must contain . (dot)")
    ])
})


if __name__ == '__main__':

    np.random.seed(42)

    try:
        df = generate_fake_df(100)

        validated_df = schema(df)

    except Exception as e:
        print(e)
        raise
