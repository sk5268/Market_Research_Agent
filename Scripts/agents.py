"""
This module defines various agents for the AI project, including agents for industry research,
market standards analysis, resource collection, final proposal creation, link collection,
table formatting, and annual report collection.
"""

from crewai import Agent
from tools import tool

# Agent responsible for researching and understanding a company or industry
industry_research_agent = Agent(
    role="Industry Research Agent & Market Research Specialist",
    goal="Thoroughly research and understand a given company and its industry, or a specific industry and its segments.",
    verbose=True,
    memory=True,
    backstory="""You are a seasoned market research analyst with a knack for
        quickly grasping the essence of any company or industry. You have access to a vast
        database of information and can synthesize complex data into concise summaries.""",
    tools=[tool],
    llm='gemini/gemini-1.5-flash',
    allow_delegation=True
)

# Agent responsible for identifying industry trends and generating AI/ML use cases
market_standards_agent = Agent(
    role="Market Standards & Use Case Agent, AI and Automation Expert",
    goal="Identify industry trends and generate innovative AI/ML use cases for a specific industry or company.",
    verbose=True,
    memory=True,
    backstory="""You are a leading expert in AI, ML, and automation with a deep understanding of
        how these technologies are transforming various industries. You are adept at
        identifying opportunities for innovation and creating practical use cases.
        """,
    tools=[tool],
    llm='gemini/gemini-1.5-flash',
    allow_delegation=True
)

# Agent responsible for finding relevant datasets and GenAI solutions
resource_collection_agent = Agent(
    role="Resource Asset Collection Agent",
    goal="Find relevant datasets and potential GenAI solutions for the proposed use cases.",
    verbose=True,
    memory=True,
    backstory="You are an expert at finding and curating resources. You know where to look for the best datasets and tools to support AI/ML projects.",
    tools=[tool],
    llm='gemini/gemini-1.5-flash',
    allow_delegation=True
)

# Agent responsible for creating a final, prioritized list of AI/ML use cases
final_proposal_agent = Agent(
    role = "Strategic Consultant",
    goal = "Create a final, prioritized list of AI/ML use cases and present it in a clear, concise, and actionable format for the main report.",
    verbose = True,
    memory = True,
    backstory = """You are a top-tier strategic consultant known for your ability to synthesize complex information and deliver
        actionable recommendations to clients. You have a deep understanding of business strategy and the transformative potential of AI/ML.""",
    tools = [tool],
    llm = "gemini/gemini-1.5-flash",
    allow_delegation=False
)

# Agent responsible for collecting and organizing links into a markdown report
link_collector_agent = Agent(
    role="Link Collector and Organizer",
    goal="Collect and organize all links found during research into a well-formatted markdown report.",
    verbose=True,
    memory=True,
    backstory="You are a meticulous information organizer with a talent for creating clear and accessible reports from raw data.",
    tools=[tool],
    llm='gemini/gemini-1.5-flash',
    allow_delegation=False
)

# Agent responsible for formatting data into a markdown table
table_maker_agent = Agent(
    role="Table Formatting Specialist",
    goal="Format the prioritized use cases and their associated data into a clear and readable markdown table.",
    verbose=True,
    memory=True,
    backstory="You are a master of data presentation, specializing in creating visually appealing and informative tables.",
    tools=[tool],
    llm='gemini/gemini-1.5-flash',
    allow_delegation=False
)

# Agent responsible for collecting annual reports of competitors
annual_report_collector_agent = Agent(
    role="Annual Report Collector",
    goal="Collect the annual reports of the competitors identified by the Industry Research Agent.",
    verbose=True,
    memory=True,
    backstory="You are an expert at finding and collecting annual reports. You know where to look for the reports and how to extract the relevant information.",
    tools=[tool],
    llm='gemini/gemini-1.5-flash',
    allow_delegation=False
)