from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        result = None
        if path.endswith(".json"):
            with open(path) as file:
                result = json.load(file)
        else:
            raise ValueError("Arquivo inválido")

        return result
