from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
from phi.model.openai import OpenAIChat


load_dotenv()

def get_company_symbol(company_name):
    """Use this function to get the company symbol for a given company name
    Args:
        company_name (str): Name of the company
    Returns:
        str: Company symbol
    """
    
    symbols = {
        "Apple": "AAPL",
        "Basavaraj": "MSFT"
    }

    return symbols.get(company_name, "Company not found")

print("----------------- Grog AI -----------------")
grog_agent = Agent(
    model= Groq(
        id = "llama-3.3-70b-versatile",
    ),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True),
        get_company_symbol
    ],
    show_tool_calls=True,
    markdown=True,
    instructions=["use tables to display data", "If you don't know the company symbol, use the get_company_symbol function to get it"],
    # debug_mode=True

)

grog_agent.print_response("Summarize and compare analyst recommendations and fundamentals for Apple and Salesforce")

print("----------------- OpenAI Chat -----------------")

openai_agent = Agent(
    model = OpenAIChat(id="gpt-4o"),
    markdown=True,
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True),
        get_company_symbol
    ],
    instructions=["use tables to display data", "If you don't know the company symbol, use the get_company_symbol function to get it"],
)

# openai_agent.print_response("Summarize and compare analyst recommendations and fundamentals for Apple and Basavaraj")