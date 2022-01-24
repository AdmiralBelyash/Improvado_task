import json
from report.writer.writer_data import Writer


class WriterJson(Writer):
    def __init__(self, indent):
        self.indent = indent

    def write(self, filename, data):
        with open(filename, 'w', encoding='UTF-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=self.indent)
