from dataclasses import dataclass
@dataclass
class RectangularPrism:
    width: float
    length: float
    height: float

    def surface_area(self) -> float:
        return 2 * (self.width * self.length + self.length * self.height + self.height * self.width)
    
    def volume(self) -> float:
        return self.width * self.length * self.height
    
    def __repr__(self) -> None:
        return f"Surface area: {self.surface_area()}\nVolume: {self.volume()}"



def main() -> None:
    rectangle =  RectangularPrism(5.0,4.0,3.0)
    r2 = RectangularPrism(5,4,3)
    print(rectangle)
    print(rectangle == r2)
 

if __name__ == "__main__":
    main()