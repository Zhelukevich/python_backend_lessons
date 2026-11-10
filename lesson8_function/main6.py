def calculate_total(price: int, quantity: int, has_discount: bool) -> int:
    total = price * quantity

    if has_discount:
        total -= 10

    return total


print(calculate_total(has_discount=True, quantity=5, price=8))
