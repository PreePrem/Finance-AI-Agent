from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv
load_dotenv()


#Web Search Agent (Agent 1)
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the websites for gathering informations",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

#Financial Agent (Agent 2)
finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
    instructions=["Use table to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent = Agent(
    team=[web_search_agent,finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources","Use table to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for Tesla",stream=True)

