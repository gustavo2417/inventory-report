from inventory_report.inventory.product import Product


def test_cria_produto():
    new_product = Product(
        3,
        'Pneu de carro',
        'Mercado livre',
        '2023-05-22',
        '2050-05-22',
        '8853059',
        'sla'
    )

    assert new_product.id == 3
    assert new_product.nome_do_produto == 'Pneu de carro'
    assert new_product.nome_da_empresa == 'Mercado livre'
    assert new_product.data_de_fabricacao == '2023-05-22'
    assert new_product.data_de_validade == '2050-05-22'
    assert new_product.numero_de_serie == '8853059'
    assert new_product.instrucoes_de_armazenamento == 'sla'
