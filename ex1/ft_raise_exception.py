"""Learning to catch and raise our own type of errors"""


def input_temperature(temp_str: str) -> int:
    """
    string input to int and checks it
    raises a Exception if temp is out of range
    tries to return tmp if it crashes
    error will be caught by test_temp
    """
    tmp = int(temp_str)
    if tmp < 0:
        raise Exception(f"{tmp}ºC is too cold for plants (min 0ºC)")
    if tmp > 40:
        raise Exception(f"{tmp}ºC is too hot for plants (max 40ºC)")
    return tmp


def test_temperature() -> None:
    """
    Test for valid, invalid or extreme values
    loops through different values
    tries input_temp
    if error Exception is caught and printed
    """
    test_data = ["25", "abc", "100", "-50"]
    for data in test_data:
        print(f"\nInput data is '{data}'")
        try:
            tmp = input_temperature(data)
            print(f"Temperature is now {tmp}ºC")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")


def main() -> None:
    """displays hardcoded text and calls test"""
    print("=== Garden Temperature Checker ===")
    test_temperature()
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
