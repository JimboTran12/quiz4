from dataclasses import dataclass
@dataclass
class RectangularPrism:
    width: float
    length: float
    height: float


def main() -> None:
    rectangle =  RectangularPrism(5.0,4.0,3.0)
    r2 = RectangularPrism(5,4,3)
    print(rectangle)
    print(rectangle == r2)

if __name__ == "__main__":
    main()