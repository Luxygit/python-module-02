"""Learning to catch different types of errors"""


def garden_operations(operation_number: int) -> None:
    """triggering diff types of errors"""
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        "garden" + 1


def test_error_types() -> None:
    """catching multiple different error types in one block"""
    i = 0
    while i < 5:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            if i == 4:
                print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueEerror: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        i += 1


def main() -> None:
    """Displays hardcoded text and calls test function"""
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    main()
