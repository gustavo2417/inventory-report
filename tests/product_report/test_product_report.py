from inventory_report.inventory.product import Product


def test_relatorio_produto():
    new_product = Product(
        3,
        'Pneu de carro',
        'Mercado livre',
        '2023-05-22',
        '2050-05-22',
        '8853059',
        'sla'
    )

    assert (str(new_product) ==
            "O produto Pneu de carro fabricado em 2023-05-22"
            " por Mercado livre com validade até 2050-05-22"
            " precisa ser armazenado sla.")
