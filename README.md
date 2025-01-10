# Finance-AI-Agent
Multi-Agent System for Stock Analysis

This Python code demonstrates the creation of a multi-agent system designed to analyze stocks. The code utilizes the Phi framework, a library for building conversational AI agents.

Subtitles:

Agent Definitions:

Web Agent:
This agent focuses on searching the web for relevant information.
It leverages the OpenAIChat model, presumably a large language model from OpenAI with the identifier "gpt-4o".
The DuckDuckGo tool is integrated to perform web searches.
The agent is instructed to consistently include sources for retrieved information and format the response in markdown. It also displays details of the tool calls made during the search process.
Finance Agent:
This agent specializes in retrieving financial data.
Similar to the web agent, it employs the OpenAIChat model (gpt-4o).
The YFinanceTools tool is utilized to gather specific financial data, including stock prices, analyst recommendations, and company information.
The agent is configured to present the data in tables and adhere to the same guidelines as the web agent regarding source inclusion, markdown formatting, and displaying tool call details.
Agent Team:
This agent combines the capabilities of both the web agent and the finance agent, forming a collaborative team.
It inherits the instructions and configurations set for the individual agents, ensuring consistent behavior.
Agent Interaction:

The code demonstrates an example interaction with the agent_team.
The print_response method is called with the prompt "Summarize analyst recommendations and share the latest news for NVDA" and sets the stream argument to True, indicating the potential for multiple responses as information is gathered.
Playground App Creation:

A Playground application is instantiated, incorporating both the web agent and the finance agent.
The get_app method retrieves the application instance.
Main Function:

The __main__ block conditionally executes the serve_playground_app function if the script is run directly.
This function launches the Playground app, enabling interactive use of the agents, most likely in a web-based interface. The reload=True argument ensures the app updates with any code changes during development.
In essence, this code establishes a framework for a multi-agent system that can be employed to comprehensively analyze stocks. The web agent retrieves relevant news articles, while the finance agent gathers financial data. By combining their efforts, the user gains valuable insights into a particular stock, including current analyst recommendations and recent news coverage.










