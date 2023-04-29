from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def simple_report(path):
        divide = path.split('.')
        if divide[1] == ('csv'):
            result = CsvImporter.import_data(path)
            return result
        elif divide[1] == ('json'):
            result = JsonImporter.import_data(path)
            return result
        elif divide[1] == ('xml'):
            result = XmlImporter.import_data(path)
            return result

    def complete_report(path):
        divide = path.split('.')
        if divide[1] == ('csv'):
            result = CsvImporter.import_data(path)
            return result
        elif divide[1] == ('json'):
            result = JsonImporter.import_data(path)
            return result
        elif divide[1] == ('xml'):
            result = XmlImporter.import_data(path)
            return result

    @staticmethod
    def import_data(path, type):
        if type == "simples":
            lks = Inventory.simple_report(path)
            result = SimpleReport.generate(lks)

        elif type == "completo":
            lks = Inventory.complete_report(path)
            result = CompleteReport.generate(lks)

        return result
