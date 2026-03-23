"""Learning 'finally' so the program ends properly even after an error"""


class GardenError(Exception):
    """exception class for all garden-related errors"""
    def __init__(self, message: str = "Unknown garden error") -> None:
        """initialise gardenerror with optional custom message"""
        super().__init__(message)


class PlantError(GardenError):
    """Exeception only for plant errors"""
    def __init__(self, message: str) -> None:
        """initialises planterror with optional message"""
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    """waters a plan by passing a capitalised name"""
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants: list[str]) -> None:
    """Tests every plant name, on an error stops and returns to main"""
    print("Opening watering system")
    try:
        for p in plants:
            water_plant(p)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main() -> None:
    """calling teset function with valid and invalid plant names"""
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])
    print("\nTesting invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
