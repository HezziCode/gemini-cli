"""This script processes a list of numbers and logs the result."""

import logging
from typing import List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_data(data: List[int]) -> int:
    """
    Calculates the sum of a list of integers.

    Args:
        data: A list of integers.

    Returns:
        The sum of the integers in the list.
    """
    logging.info(f"Processing data: {data}")
    total = sum(data)
    logging.info(f"Returning total: {total}")
    return total

def main() -> None:
    """
    Defines a list of data and prints the processed result.
    """
    data = [1, 2, 3, 4, 5]
    result = process_data(data)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
