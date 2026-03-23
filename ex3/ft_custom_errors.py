"""Learning to catch all types of errors even customised ones with hierarchy"""


class GardenError(Exception):
    """
    Defining the GardenError class which inherits from pythons Exception
    class, thus to print an error, message is passed to super's init.
    """
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    """defines the error class specific of plants"""
    def __init__(self, message: str = "Unknwown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    """defines the error class specific of water"""
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def raise_plant_error() -> None:
    """function that raises the specific error class of plants"""
    raise PlantError("The tomato plant is wilting!")


def raise_water_error() -> None:
    """function that raises the specific error class of water"""
    raise WaterError("Now enought water in the tank!")


def test_custom_errors() -> None:
    """tests and displays specific errors and also at a parent level"""
    print("\nTesting PlantError...")
    try:
        raise_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        raise_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    for func in [raise_plant_error, raise_water_error]:
        try:
            func()
        except GardenError as e:
            print(f"Caught GardenError: {e}")


def main() -> None:
    """displays hardcoded text and calls test function"""
    print("=== Custom Garden Errors Demo ===")
    test_custom_errors()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
