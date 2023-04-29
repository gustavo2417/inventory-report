from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(path):
        result = None
        if path.endswith(".xml"):
            with open(path) as file:
                file_read = file.read()
                result = xmltodict.parse(file_read)["dataset"]["record"]
        else:
            raise ValueError("Arquivo inválido")

        return result
