## Story
- The Gulf of Maine Research Institute (GMRI) Coastal and Marine Economics Lab is conducting a project to analyze the market dynamics and competition in the New England groundfish fishery. The project aims to provide insights into the factors influencing the decisions and behaviors of stakeholders in the coastal and marine resource sector, with a specific focus on the groundfish market.

- New England has a significant groundfish fishery that supplies various whitefish species, including culturally important ones such as cod and haddock. However, the region also imports a substantial amount of whitefish from the Northeast Atlantic, creating direct competition between locally harvested and imported fish.

- The primary objective of this project is to understand the market competition and relationships between the New England groundfish fishery and imports from the Northeast Atlantic, particularly from countries like Norway, Iceland, and Scotland. By analyzing data from sources such as the Portland Fish Exchange, NOAA Landings, and Foreign Trade databases, the project will examine the market dynamics, price fluctuations, and trade patterns.

- The findings of this project will provide valuable information to stakeholders in the New England groundfish industry, including fishermen, processors, distributors, and policymakers. It will help them make informed decisions regarding resource management, market strategies, and policy development to ensure the sustainability and competitiveness of the local groundfish fishery in the face of international competition.

## Approach
- In 1-2 paragraphs (maximum) describe specific project objectives designed to address the project story/goals.
    - This project aims to generate annual reports that comprehensively analyze market competition between Maine and the Northeast Atlantic for key groundfish species. These reports will quantify year-to-year market changes (value, import volume, etc.) for each species, visualize these trends with informative plots, and provide clear written summaries to illuminate market dynamics.

- Include the proposed approach for achieving these objectives.
    - User Input: Employ a command-line interface to capture user-defined year ranges or specific years for analysis.
    - Data Analysis: Utilize Pandas to analyze and compare market data for Maine and the Northeast Atlantic.
    - Visualization: Generate market competition visualizations using Seaborn and Matplotlib.
    - Data Integration: Design a predefined, formatted HTML template to structure the reports. Python scripts will dynamically inject data and visualizations into this template.
    - Automated Reporting: Automate the entire report generation process, producing comprehensive final reports.

- Identify any risks that may prevent achieving the objectives.
    - Incomplete or missing data for specific species could disrupt the report template.

- Include a description of the unique contribution from your team, especially if it builds from a previous project.
    - Automates groundfish market competition analysis, providing efficient and insightful reporting for stakeholders.

- The project idea should have technical detail understandable by anyone in this class.  
    - The technical procedures for generating a report are shown below:
        - Take user input years through command line flags.
        - Use Pandas to analyze comparisons and utilize Seaborn and Matplotlib to generate market competition pictures of Maine against Northeast Atlantic.
        - Wrap the result with a data class and inject it into a pre-defined template using jinja2.
        - Output report file.