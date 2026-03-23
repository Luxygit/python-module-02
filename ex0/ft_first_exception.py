"""Program meant to learn about error handling and validation"""


def input_temperature(temp_str: str) -> int:
    """converts input to int"""
    temp = int(temp_str)
    return temp


def test_temperature() -> None:
    """Testing input with different data types"""
    print("\nInput data is '25'")
    try:
        print(f"Temperature is now {input_temperature("25")}ºC")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("\nInput data is 'abc'")
    try:
        print(f"Temperature is now {input_temperature("abc")}ºC")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")


def main() -> None:
    """displays hardcoded text and calls the test function"""
    print("=== Garden Temperature ===")
    test_temperature()
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
