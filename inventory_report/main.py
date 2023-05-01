import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")

    result = None

    _, path, type = sys.argv

    if path.endswith(".csv"):
        result = InventoryRefactor(CsvImporter).import_data(path, type)
    if path.endswith(".json"):
        result = InventoryRefactor(JsonImporter).import_data(path, type)
    if path.endswith(".xml"):
        result = InventoryRefactor(XmlImporter).import_data(path, type)

    sys.stdout.write(result)
