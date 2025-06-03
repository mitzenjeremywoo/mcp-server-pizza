from pydantic import BaseModel

class PizzaOrder(BaseModel):
    pizza_type: str
    crust_type: str

    def __str__(self):
        return f"pizza type: {self.pizza_type} -> crust: {self.crust_type}"
