from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        imported_data = self.importer.import_data(path)
        self.data.extend(imported_data)

        if type == "simples":
            return SimpleReport.generate(imported_data)
        elif type == "completo":
            return CompleteReport.generate(imported_data)

    def __iter__(self):
        return InventoryIterator(self.data)
