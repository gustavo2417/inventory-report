from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list):
        result = SimpleReport.generate(list)
        result += "\nProdutos estocados por empresa:\n"

        all_companys = SimpleReport.get_products_by_company(list)

        for key, value in all_companys.items():
            result += f"- {key}: {value}\n"

        return result
