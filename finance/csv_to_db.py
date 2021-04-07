import os

from decouple import config

from finance.models import CsvData

path = config('DOCKER_PATH_TO_DOWNLOADS') if config('DOCKER', cast=bool) else config('PATH_TO_DOWNLOADS')


def get_csv_file_write_to_db(name_of_file) -> None:
    csv_file_path = path + f'{name_of_file}.csv'
    with open(csv_file_path, 'r') as csv_file:
        csv_file.readline()
        list_ = csv_file.readlines()
        for value in list_:
            list_v = value.split(',')
            CsvData.objects.get_or_create(
                date=list_v[0],
                open=list_v[1],
                high=list_v[2],
                low=list_v[3],
                close=list_v[4],
                adj_close=list_v[5],
                volume=list_v[6]
            )


if __name__ == '__main__':
    get_csv_file_write_to_db()
