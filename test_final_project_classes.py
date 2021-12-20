import unittest
import final_project


class TestPizza(unittest.TestCase):

    def test_pizza_base(self):
        pz = final_project.PizzaBase('XL')

        self.assertIsInstance(pz, final_project.PizzaBase)
        self.assertEqual(pz.name, None)
        self.assertEqual(pz.size, 'XL')
        self.assertEqual(pz.ingredients, {})
        self.assertEqual(pz.time_to_make, None)
        self.assertEqual(pz.icon, None)

    def test_margherita_properties(self):
        pz = final_project.Margherita('XL')

        self.assertIsInstance(pz, final_project.Margherita)
        self.assertEqual(pz.name, 'Margherita')
        self.assertEqual(pz.size, 'XL')
        self.assertEqual(pz.ingredients, {'sauce': 'tomato sauce', 'cheese': 'mozzarella', 'toppings': ['tomatoes']})
        self.assertEqual(pz.average_time_to_make, 20)
        self.assertEqual(pz.icon, '🧀')

    def test_pepperoni_properties(self):
        pz = final_project.Pepperoni('L')

        self.assertIsInstance(pz, final_project.Pepperoni)
        self.assertEqual(pz.name, 'Pepperoni')
        self.assertEqual(pz.size, 'L')
        self.assertEqual(pz.ingredients, {'sauce': 'tomato sauce', 'cheese': 'mozzarella', 'toppings': ['pepperoni']})
        self.assertEqual(pz.average_time_to_make, 25)
        self.assertEqual(pz.icon, '🍕')

    def test_hawaiian_properties(self):
        pz = final_project.Hawaiian('L')

        self.assertIsInstance(pz, final_project.Hawaiian)
        self.assertEqual(pz.name, 'Hawaiian')
        self.assertEqual(pz.size, 'L')
        self.assertEqual(pz.ingredients, {'sauce': 'tomato sauce', 'cheese': 'mozzarella',
                                          'toppings': ['chicken', 'pineapples']})
        self.assertEqual(pz.average_time_to_make, 30)
        self.assertEqual(pz.icon, '🍍')

    def test_wrong_size(self):
        with self.assertRaises(ValueError):
            final_project.Margherita('M')
            # final_project.Pepperoni(['hello'])
            # final_project.Hawaiian(123)

    def test_dict(self):
        pz1 = final_project.Margherita('L')
        expected1 = 'tomato sauce: 100g \nmozzarella: 150g \n[\'tomatoes\']: 200g \n'
        pz2 = final_project.Margherita('XL')
        expected2 = 'tomato sauce: 200g \nmozzarella: 300g \n[\'tomatoes\']: 400g \n'

        self.assertEqual(expected1, pz1.dict())
        self.assertEqual(expected2, pz2.dict())

    def test_equal(self):
        pz1 = final_project.Margherita('L')
        pz21 = final_project.Margherita('XL')
        pz22 = 'Margerita'
        pz23 = final_project.Margherita('L')

        self.assertNotEqual(pz1, pz21)
        self.assertNotEqual(pz1, pz22)
        self.assertEqual(pz1, pz23)

    def test_repr(self):
        pz1 = final_project.Pepperoni('XL')
        expected1 = 'Pizza Pepperoni of size XL'
        pz2 = final_project.Hawaiian('L')
        expected2 = 'Pizza Hawaiian of size L'

        self.assertEqual(str(pz1), expected1)
        self.assertEqual(str(pz2), expected2)

    def test_hash(self):
        pz1 = final_project.Pepperoni('XL')
        pz2 = final_project.Pepperoni('L')
        pz3 = final_project.Pepperoni('XL')

        self.assertEqual(hash(pz1), hash(pz3))
        self.assertNotEqual(hash(pz1), hash(pz2))


if __name__ == '__main__':
    pass

