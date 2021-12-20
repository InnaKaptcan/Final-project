import final_project
from unittest import mock
import pytest


def test_execute_order(capsys):
    """Проверяем работу статического метода execute_order"""
    pz = final_project.Pepperoni('XL')
    # expected = 'First we\'re making the dough, and cooking the tomato sauce;\n' \
    #            'Then we\'re rolling the dough and spreading the tomato sauce;\n'\
    #            'Finally we\'re adding pepperoni and sprinkling it with mozzarella;\n' \
    #            'Your Pizza Pepperoni of size XL is ready'
    final_project.Kitchen.execute_order(pz)
    captured = capsys.readouterr()
    assert 'Pepperoni of size XL' in captured.out


def test_bake(capsys):
    """Проверяем навешивание декоратора log на функцию bake(...)"""
    pz_order = final_project.Hawaiian('L')

    with mock.patch('random.randint', lambda x, y: 30):
        pz_actual = final_project.bake(pz_order)
        captured = capsys.readouterr()
        assert '🍕Приготовили за 30с!' in captured.out
        assert pz_actual == pz_order


def test_delivering(capsys):
    """Проверяем навешивание декоратора log на функцию delivering(...)"""
    pz_order = final_project.Margherita('L')
    with mock.patch('random.randint', lambda x, y: 20):
        pz_delivered = final_project.delivering(pz_order)
        captured = capsys.readouterr()
        assert '🛵 Доставили за 20с!' in captured.out
        assert pz_order == pz_delivered


def test_pickup(capsys):
    """Проверяем навешивание декоратора log на функцию pickup(...)"""
    pz_order = final_project.Pepperoni('XL')
    with mock.patch('random.randint', lambda x, y: 25):
        pz_collected = final_project.pickup(pz_order)
        captured = capsys.readouterr()
        assert '🏠 Забрали за 25с!' in captured.out
        assert pz_order == pz_collected


def test_order_with_delivery(capsys):
    """Проверяем работу функции order с доставкой"""
    pz_str = 'Margherita'
    size_str = 'L'
    need_delivery = True
    with mock.patch('random.randint', lambda x, y: 10):
        final_project.order(pz_str, size_str, need_delivery)
        captured = capsys.readouterr()
        assert 'Your Pizza Margherita of size L is ready' in captured.out
        assert '🍕Приготовили за 10с!' in captured.out
        assert '🛵 Доставили за 10с!' in captured.out


def test_order_without_delivery(capsys):
    """Проверяем работу функции order без доставки"""
    pz_str = 'Hawaiian'
    size_str = 'L'
    need_delivery = False
    with mock.patch('random.randint', lambda x, y: 30):
        final_project.order(pz_str, size_str, need_delivery)
        captured = capsys.readouterr()
        assert 'Your Pizza Hawaiian of size L is ready' in captured.out
        assert '🍕Приготовили за 30с!' in captured.out
        assert '🏠 Забрали за 30с!' in captured.out


def test_order_not_from_menu():
    """Проверяем работу функции order при заказе несуществующего типа пиццы"""
    pz_str = 'Three_cheese'
    size_str = 'L'
    need_delivery = True
    with pytest.raises(ValueError):
        final_project.order(pz_str, size_str, need_delivery)


def test_menu(capsys):
    """Проверяем работу функции menu"""
    expected = '- Margherita 🧀: [\'tomato sauce\', \'mozzarella\', \'tomatoes\']\n' \
               '- Pepperoni 🍕: [\'tomato sauce\', \'mozzarella\', \'pepperoni\']\n' \
               '- Hawaiian 🍍: [\'tomato sauce\', \'mozzarella\', \'chicken\', \'pineapples\']'
    final_project.menu()
    captured = capsys.readouterr()
    assert captured.out[:-1] == expected


if __name__ == '__main__':
    pass
