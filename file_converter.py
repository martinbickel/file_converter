import time
import pandas as pd
import numpy as np

CITY_DATA = '/Users/acemartinb/Documents/Projekte_Python/convert_to_files/test_file.csv'

def load_data():
    """
    Loads the source file.

    Args:

    Returns:
        df - Pandas DataFrame containing the data from the .csv
    """
    df = pd.read_csv('/Users/acemartinb/Documents/Projekte_Python/convert_to_files/test_file.csv')
    print(df)
    return df


def main():
    while True:
        df = load_data()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
