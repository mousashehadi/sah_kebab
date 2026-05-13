def calculate_profit(revenues: list[dict], expenses: list[dict]) -> dict:
    total_revenue = sum(item["amount"] for item in revenues)
    total_expenses = sum(item["amount"] for item in expenses)
    profit = total_revenue - total_expenses

    return {
        "total_revenue": total_revenue,
        "total_expenses": total_expenses,
        "profit": profit,
        "is_profitable": profit > 0,
    }


def print_report(revenues: list[dict], expenses: list[dict]) -> None:
    print("=" * 40)
    print("ОТЧЁТ О ПРИБЫЛИ")
    print("=" * 40)

    print("\nДОХОДЫ:")
    for item in revenues:
        print(f"  {item['name']:<25} {item['amount']:>10.2f} руб.")

    print("\nРАСХОДЫ:")
    for item in expenses:
        print(f"  {item['name']:<25} {item['amount']:>10.2f} руб.")

    result = calculate_profit(revenues, expenses)

    print("\n" + "-" * 40)
    print(f"  {'Итого доходов:':<25} {result['total_revenue']:>10.2f} руб.")
    print(f"  {'Итого расходов:':<25} {result['total_expenses']:>10.2f} руб.")
    print(f"  {'Прибыль:':<25} {result['profit']:>10.2f} руб.")
    print("-" * 40)

    status = "ПРИБЫЛЬ" if result["is_profitable"] else "УБЫТОК"
    print(f"\nРезультат: {status}")
    print("=" * 40)


if __name__ == "__main__":
    revenues = [
        {"name": "Продажа шаурмы", "amount": 85000.00},
        {"name": "Продажа напитков", "amount": 12000.00},
        {"name": "Доставка", "amount": 8500.00},
    ]

    expenses = [
        {"name": "Аренда", "amount": 25000.00},
        {"name": "Продукты и ингредиенты", "amount": 30000.00},
        {"name": "Зарплата сотрудников", "amount": 20000.00},
        {"name": "Коммунальные услуги", "amount": 5000.00},
        {"name": "Упаковка", "amount": 3000.00},
    ]

    print_report(revenues, expenses)
