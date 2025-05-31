from pydantic import BaseModel

class PizzaOrder(BaseModel):
    def __init__(self, pizza_type: str, crust_size: str):
        self.pizza_type = pizza_type
        self.crust_size = crust_size

    def __str__(self):
        return f"{self.crust_size} crust {self.pizza_type} pizza"
