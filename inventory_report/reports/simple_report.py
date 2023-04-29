from datetime import date


class SimpleReport:
    def get_oldest_manufacturing_date(list):
        result = list[0]["data_de_fabricacao"]

        for i in list:
            if i["data_de_fabricacao"] < result:
                result = i["data_de_fabricacao"]

        return result

    def get_nearest_expiration_date(list):
        today = str(date.today())
        new_list = []

        for i in list:
            if i["data_de_validade"] >= today:
                new_list.append(i["data_de_validade"])

        result = min(new_list)

        return result

    @staticmethod
    def get_products_by_company(list):
        counter = {}

        for i in list:
            if i["nome_da_empresa"] not in counter:
                counter[i["nome_da_empresa"]] = 0
            counter[i["nome_da_empresa"]] += 1

        return counter

    def get_company_with_more_products(list):
        result = SimpleReport.get_products_by_company(list)

        return max(result, key=result.get)

    @staticmethod
    def generate(list):
        oldest = SimpleReport.get_oldest_manufacturing_date(list)
        expiration_date = SimpleReport.get_nearest_expiration_date(list)
        more_products = SimpleReport.get_company_with_more_products(list)

        return (
            f"Data de fabricação mais antiga: { oldest }\n"
            f"Data de validade mais próxima: { expiration_date }\n"
            f"Empresa com mais produtos: { more_products }"
        )
