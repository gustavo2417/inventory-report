from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class inventory:
    def simple_report(path):
        result = None
        divide = path.split('.')
        if divide[1] == ('.csv'):
            result = CsvImporter(path)
        elif divide[1] == ('.json'):
            result = JsonImporter(path)
        else:
            result = XmlImporter(path)

        return result

    def complete_report(path):
        result = None
        divide = path.split('.')
        if divide[1] == ('.csv'):
            result = CsvImporter(path)
        elif divide[1] == ('.json'):
            result = JsonImporter(path)
        else:
            result = XmlImporter(path)

        return result

    @staticmethod
    def import_data(path, type):
        result = None
        if type == "simples":
            list = inventory.simple_report(path)
            result = SimpleReport(list)

        elif type == "completo":
            list = inventory.complete_report(path)
            result = CompleteReport(list)

        return result
