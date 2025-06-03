from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
from order import pizza

# Initialize FastMCP server
mcp = FastMCP("mcpPizza", host="0.0.0.0", port="8000")

# Constants
PIZZA_API_BASE = "http://localhost:8000"
USER_AGENT = "pizza-app/1.0"

async def create_pizza_order_api_call(url: str, order: pizza.PizzaOrder) -> dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, content=order, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

@mcp.tool()
async def order_pizza(order: pizza.PizzaOrder) -> str:
    """Place an pizza order for a customer. 

    Args:
        PizzaOrder is a data structure which accepts:

        1. pizzaType - pizza flavour that customer will be ordering. We have many 
           different types of pizza Mozzarella Stuffed Crust - Classic Cheese, Mozzarella Stuffed Crust - Pepperoni Cheese and many more.
           Need to ask user specifically what type of pizza they are trying to order

        2. pizzaCurst - this is the type of crust that comes with the pizza type. We have the followings.
           a) Large San Francisco Style 
           b) Large Pan 
           c) Large Thin and Crispy
           d) Large Gluten Free
           e) Extra Large Thin and Crispy

           Not all pizzaType have the same pizza crust. 
    """
    
    url = f"{PIZZA_API_BASE}/local"
    data = await create_pizza_order_api_call(url, order)

    print("results from REST api to NWS endpoint", data)

    # if not data or "features" not in data:
    #     return "Unable to fetch alerts or no alerts found."

    # if not data["features"]:
    #     return "No active alerts for this state."

    #alerts = [format_alert(feature) for feature in data["features"]]
    #return "\n---\n".join(alerts)
    return data

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='sse')