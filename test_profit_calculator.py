import unittest

from profit_calculator import calculate_profit


class TestCalculateProfit(unittest.TestCase):
    def test_positive_profit(self):
        revenues = [{"name": "Продажи", "amount": 1000.0}]
        expenses = [{"name": "Аренда", "amount": 400.0}]

        result = calculate_profit(revenues, expenses)

        self.assertEqual(result["total_revenue"], 1000.0)
        self.assertEqual(result["total_expenses"], 400.0)
        self.assertEqual(result["profit"], 600.0)
        self.assertTrue(result["is_profitable"])

    def test_loss(self):
        revenues = [{"name": "Продажи", "amount": 300.0}]
        expenses = [{"name": "Аренда", "amount": 500.0}]

        result = calculate_profit(revenues, expenses)

        self.assertEqual(result["profit"], -200.0)
        self.assertFalse(result["is_profitable"])

    def test_break_even(self):
        revenues = [{"name": "Продажи", "amount": 500.0}]
        expenses = [{"name": "Аренда", "amount": 500.0}]

        result = calculate_profit(revenues, expenses)

        self.assertEqual(result["profit"], 0.0)
        self.assertFalse(result["is_profitable"])

    def test_empty_lists(self):
        result = calculate_profit([], [])

        self.assertEqual(result["total_revenue"], 0)
        self.assertEqual(result["total_expenses"], 0)
        self.assertEqual(result["profit"], 0)
        self.assertFalse(result["is_profitable"])

    def test_multiple_items(self):
        revenues = [
            {"name": "Шаурма", "amount": 85000.00},
            {"name": "Напитки", "amount": 12000.00},
            {"name": "Доставка", "amount": 8500.00},
        ]
        expenses = [
            {"name": "Аренда", "amount": 25000.00},
            {"name": "Продукты", "amount": 30000.00},
            {"name": "Зарплата", "amount": 20000.00},
            {"name": "Коммуналка", "amount": 5000.00},
            {"name": "Упаковка", "amount": 3000.00},
        ]

        result = calculate_profit(revenues, expenses)

        self.assertEqual(result["total_revenue"], 105500.00)
        self.assertEqual(result["total_expenses"], 83000.00)
        self.assertEqual(result["profit"], 22500.00)
        self.assertTrue(result["is_profitable"])

    def test_only_revenues(self):
        revenues = [{"name": "Продажи", "amount": 1500.0}]

        result = calculate_profit(revenues, [])

        self.assertEqual(result["profit"], 1500.0)
        self.assertTrue(result["is_profitable"])

    def test_only_expenses(self):
        expenses = [{"name": "Аренда", "amount": 750.0}]

        result = calculate_profit([], expenses)

        self.assertEqual(result["profit"], -750.0)
        self.assertFalse(result["is_profitable"])

    def test_float_precision(self):
        revenues = [{"name": "A", "amount": 0.1}, {"name": "B", "amount": 0.2}]
        expenses = [{"name": "C", "amount": 0.1}]

        result = calculate_profit(revenues, expenses)

        self.assertAlmostEqual(result["profit"], 0.2, places=9)


if __name__ == "__main__":
    unittest.main()
