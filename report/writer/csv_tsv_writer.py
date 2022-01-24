import csv
from report.writer.writer_data import Writer


class WriterCsvTsv(Writer):
    def __init__(self, delimiter):
        self.delimiter = delimiter

    def write(self, filename, data):
        with open(filename, 'w', encoding='utf-8') as file:
            fieldnames = ['first_name', 'last_name', 'country', 'city', 'birth_date', 'sex']

            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=self.delimiter)
            writer.writeheader()
            for person in data:
                writer.writerow({'first_name': person['first_name'], 'last_name': person['last_name'],
                                 'country': person['country'], 'city': person['city'],
                                 'birth_date': person['birth_date'], 'sex': person['sex']})
