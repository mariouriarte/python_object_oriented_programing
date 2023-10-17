from contact import Contact

class Supplier(Contact):
    def order(self, order: "Order") -> None:
        print(
            "If this were a real system we would send "
            f"'{order}' order to '{self.name}'"
        )

class Order():
    def __init__(self, item: str) -> None:
        self.item = item

    def list(self) -> str:
        return f"{self.item.title}"
    
    def __repr__(self) -> str:
        return self.list()
