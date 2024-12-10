"""
This module defines various tasks for the AI project, including industry research,
market standards analysis, resource collection, final proposal creation, link collection,
table formatting, and annual report collection.
"""

# Import Task class from crewai module
from crewai import Task

# Import tool from tools module
from tools import tool

# Import agents from agents module
from agents import (
    industry_research_agent,
    market_standards_agent,
    resource_collection_agent,
    final_proposal_agent,
    link_collector_agent,
    table_maker_agent,
    annual_report_collector_agent
)

# Define industry research task
industry_research_task = Task(
    description="""
        ## Industry and Company Analysis

        **Input:** name of a company

        **Tasks:**

        1. **Identify the Industry and Segment:**
           - determine the primary industry {company} operates in.
           - Further refine the industry into a specific segment (e.g., "Retail - E-commerce").

        2. **Company Analysis:**
           - **Key Offerings:** Research and list the {company}'s main products or services.
           - **Strategic Focus Areas:** Identify the {company}'s current strategic priorities.
           - **Vision and Product Information:** Gather information about the {company}'s overall vision and product details.
           - **Main Competitors:** Identify the {company}'s main competitors.

        3. **Collect Links:**
           - Store all URLs used during research for the Link Collector Agent.
           - Pass the competitor's name to the Annual Report Collector Agent.
           
        """,
    
    expected_output="""
            - **Company:** [company name]
             - **Industry:** [Industry Name]
             - **Segment:** [Specific Segment]
             - **Key Offerings:** [Bullet point list]
             - **Strategic Focus Areas:** [Bullet point list]
             - **Vision/Product Info:** [Brief summary]
             - **Main Competitors:** [List]
             - **All Links:** [List of all URLs used during research]
        """,
    tools=[tool],
    agent=industry_research_agent,
    async_execution=False
)

# Define market standards task
market_standards_task = Task(
    description="""
        ## Market Standards and Use Case Generation

        **Input:** Output from the Industry and Company Research Agent, including:

        - **Industry:** [Industry Name]
        - **Segment:** [Specific Segment]
        - **Company:** [Company Name]
        - **Strategic Focus Areas (Optional):** [Strategic Focus Areas]

        **Tasks:**

        1. **Analyze Industry Trends:**
           - Research current trends in AI, ML, automation, GenAI, and LLMs within the specified industry/segment.
           - Identify how companies are using these technologies, focusing on process improvement, customer experience, and operational efficiency.

        2. **Propose Relevant Use Cases:**
           - Generate at least 5 specific use cases where the company (or companies in this industry/segment) can leverage these technologies.
           - Tailor use cases to the industry/segment and the company's strategic focus areas (if provided).
           - For each use case:
             - **Title:** Clear and concise title.
             - **Description:** How the use case works and the technologies involved.
             - **Benefits:** Potential benefits (e.g., cost savings, increased efficiency).
             - **Example:** Concrete example of implementation.

        3. **Collect Links:**
           - Store all URLs used during research for the Link Collector Agent.
        """,
    
    expected_output="""
            - **Industry Trends:** [Summary with source URLs]
             - **Proposed Use Cases:**
               - **Use Case 1:**
                 - **Title:** ...
                 - **Description:** ...
                 - **Benefits:** ...
                 - **Example:** ...
               - (Repeat for at least 5 use cases)
             - **All Links:** [List of all URLs used during research]
        """,
    tools=[tool],
    agent=market_standards_agent,
    async_execution=False
)

# Define resource collection task
resource_collection_task = Task(
    description="""
        ## Resource Asset Collection

        **Input:** List of use cases from the Market Standards & Use Case Generation Agent:

        - **Use Case [Number]:**
          - **Title:** ...
          - **Description:** ...
          - **Benefits:** ...
          - **Example:** ...

        **Tasks:**

        1. **Dataset Search:**
           - For each use case, search for relevant datasets on Kaggle, HuggingFace, and GitHub.
           - Consider the "Description" and "Example" to determine the type of data needed.

        2. **GenAI Solution Exploration:**
           - If applicable, identify GenAI solutions like:
             - Document Search
             - Automated Report Generation
             - AI-Powered Chat Systems

        3. **Collect Links:**
           - Store all URLs used during research for the Link Collector Agent.
        """,
    
    expected_output="""
            # GenAI & ML Use Cases for {company}
            - ## **Use Case [Number]:** [Use Case Title]
               - **Datasets:**
                 - [Dataset Name 1] - [Link] (Brief description)
                 - [Dataset Name 2] - [Link] (Brief description)
               - **GenAI Solutions:**
                 - [Solution Name 1] - [Link] (Description of use)
                 - [Solution Name 2] - [Link] (Description of use)
             - **All Links:** [List of all URLs used during research, including dataset and GenAI solution links]
        """,
    tools=[tool],
    agent=resource_collection_agent,
    async_execution=False
)

# Define final proposal task
final_proposal_task = Task(
    description = """
        ## Final Proposal of AI/ML Use Cases (Main Report Content)

        **Input:** Reports from previous agents:

        - Market Research Report
        - Use Case Report
        - Resource Report

        **Tasks:**

        1. **Prioritize Use Cases:**
           - Review and prioritize use cases based on:
             - **Relevance:** Alignment with company's strategic focus areas (if provided) and industry trends.
             - **Feasibility:** Practicality of implementation given available resources and technology.
             - **Potential Impact:** Business value in terms of cost savings, revenue, customer satisfaction, or efficiency.
           - Select the top 3-5 most promising and actionable use cases.

        2. **Create Main Report Content:**
           - For each prioritized use case, prepare the content for the main report:
             - **Title:** Clear and concise title.
             - **Description:** Brief, easily understandable description.
             - **Strategic Alignment:** How it aligns with company goals (if provided) or addresses industry challenges.
             - **Potential Benefits:** Articulate the potential benefits.
             - **Implementation Considerations:** Discuss data requirements or technological dependencies.

        3. **Prepare Data for Other Agents:**
           - Pass the prioritized use cases (Title, Description, Resource Links) to the Table Maker Agent.
           - Pass all collected links from previous agents to the Link Collector Agent.
        """,
    
    expected_output = """
            # GenAI & ML Use Cases for {company}
            - **Executive Summary:** Summarize key findings and recommendations.
             - **Prioritized Use Cases:**
               - **Use Case 1:**
                 - **Title:** ...
                 - **Description:** ...
                 - **Strategic Alignment:** ...
                 - **Potential Benefits:** ...
                 - **Implementation Considerations:** ...
               - (Repeat for each prioritized use case)
             - **Conclusion:** Offer final thoughts and recommendations for next steps.
             - **Table Data:** [Formatted data for the Table Maker Agent]
             - **All Links:** [list of all links for the Link Collector Agent each in a new line]
        """,
    tools=[tool],
    agent=final_proposal_agent,
    async_execution=False
)

# Define collect links task
collect_links_task = Task(
    description="""
        ## Collect and Organize All Links

        **Input:**
        - Consolidated list of all links from the Final Proposal Agent.

        **Task:**
        - Organize the links into a well-structured markdown report.
        - Categorize links (e.g., Industry Research, Use Case Research, Datasets, GenAI Solutions).
        - Ensure all links are clickable and functional.
        """,
    expected_output="""
        A markdown report with a categorized list of all links. For example:

        # Supplementary Report: Relevant Links

        ## Industry Research Links

        - [Link 1 Description](URL1)
        - [Link 2 Description](URL2)

        ## Use Case Research Links

        - [Link 3 Description](URL3)
        - [Link 4 Description](URL4)

        ## Dataset Links

        - [Dataset 1](URL5) - Brief description
        - [Dataset 2](URL6) - Brief description

        ## GenAI Solution Links

        - [GenAI Solution 1](URL7) - Description of use
        """,
    tools=[tool],
    agent=link_collector_agent,
    async_execution=False
)

# Define format table task
format_table_task = Task(
    description="""
        ## Format Use Cases into a Markdown Table

        **Input:**
        - Prioritized use cases data from the Final Proposal Agent (Title, Description, Resource Links).

        **Task:**
        - Create a markdown table with the following columns:
          - Use Case Title
          - Description
          - Resource Links (clickable)
        """,
    expected_output="""
        A markdown table. For example:

        # Use Case Table Report

        | Use Case Title | Description | Resource Links |
        |---|---|---|
        | Use Case 1 | Description of Use Case 1 | [Dataset 1](URL1), [GenAI Solution 1](URL2) |
        | Use Case 2 | Description of Use Case 2 | [Dataset 2](URL3) |
        | ... | ... | ... |
        """,
    tools=[tool],
    agent=table_maker_agent,
    async_execution=False
)

# Define annual report collection task
annual_report_collection_task = Task(
    description="""
        ## Collect Competitor's Annual Reports

        **Input:**
        - List of competitors from the Industry Research Agent.

        **Task:**
        - Search for and collect the annual reports of the competitors.
        - Provide links to the annual reports.
        """,
    expected_output="""
        A markdown report with links to the annual reports of the competitors. For example:

        # Competitor's Annual Reports

        * ## Competitor 1

            - [Annual Report 2023](URL1)

        * ## Competitor 2

            - [Annual Report 2023](URL2)
        """,
    tools=[tool],
    agent=annual_report_collector_agent,
    async_execution=False
)