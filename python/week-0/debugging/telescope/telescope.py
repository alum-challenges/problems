def zoom(m, factor=500):
    return round(m * factor, 2)


def main():
    zoom = input("How many times is the image magnified? ")
    size = input("How tall is the object (in meters)? ")

    def calculate_distance():
        return zoom(size, zoom)

    distance = calculate_distance()

    print(f"The object is {distance:.1f} meters away.")


if __name__ == "__main__":
    main()
