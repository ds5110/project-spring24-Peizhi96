## Story
- This is the high-level project description for a general audience.


- Revisions to the original story should include concise description of analytic objectives.

- Clearly identify any changes from the original story.

- Any changes to the original story should be based on stakeholder feedback, or otherwise explained.

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