from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        result = []
        if path.endswith(".csv"):
            with open(path, encoding="utf-8") as file:
                data = csv.DictReader(file, delimiter=",")
                for i in data:
                    result.append(i)
        else:
            raise ValueError("Arquivo inválido")

        return result
