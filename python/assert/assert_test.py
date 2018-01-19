#!/usr/bin/env python
# coding=utf-8

from typing import Dict, Any


def apply_discount(product: Dict[str, Any], discount: float) -> int:
    """Apply a discount coupon.

    :param product: dictionary containing information on the product
    :param discount: discount as a fractional percentage (i.e. 0.25 -> 25% discount)
    :return: discounted price (cents)
    """
    # product price is stored as an integer number of cents
    initial_price_cents = product['price']
    discounted_price_cents = int(initial_price_cents * (1.0 - discount))
    assert 0 <= discounted_price_cents <= initial_price_cents
    return discounted_price_cents


if __name__ == '__main__':
    shoes = {'name': 'Fancy Shoes', 'price': 14900}

    good_discount = 0.25
    invalid_discount = 2.0

    good_price = apply_discount(shoes, good_discount)
    print('With a {0:0.2f}% discount, the shoes will cost ${1:0.2f}'.format(good_discount * 100, good_price / 100.0))

    invalid_price = apply_discount(shoes, invalid_discount)
    print('With a {0:0.2f}% discount, the shoes will cost ${1:0.2f}'.format(invalid_discount * 100, invalid_price / 100.0))
