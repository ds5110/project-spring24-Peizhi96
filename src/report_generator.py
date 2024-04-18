import uuid
from jinja2 import Environment, FileSystemLoader
import matplotlib.pyplot as plt
from template_data import ReportData, UserInput
import os
import model
import argparse

# Parse command line
def parse() -> UserInput:
    # Check valid input
    parser = argparse.ArgumentParser(description="Generate a report")
    parser.add_argument("--start-year", type=int, help="starting year of this report", required=True)
    parser.add_argument("--end-year", type=str, help="ending year of this report", required=True)
    parser.add_argument("--report_name", type=str, help="Name of the report", required=True)
    
    args = parser.parse_args()  
    user_input = UserInput()
    user_input.start_year = args.start_year
    user_input.end_year = args.end_year
    user_input.report_name = args.report_name
    
    return user_input
    

def main():
    # Report dataclass
    report_data = ReportData()
    report_data.user_input = parse()

    # Report uuid
    report_data.report_id = uuid.uuid1()
    
    # Make sure the report_name is unique by using UUID
    report_data.user_input.report_name = report_data.user_input.report_name + "_" + str(report_data.report_id)
    

    # Load report template
    template_loader = FileSystemLoader(searchpath="src/")
    templateEnv = Environment(loader=template_loader)
    template = templateEnv.get_template("template.html")

    # Calcualte data
    model.process(data=report_data)

    # Render the template with data object
    report_html = template.render(report_data=report_data)

    # Save the generated report
    # if the report_name.html exists, then create the file with name report_name_uuid.html
    with open(report_data.user_input.report_name + ".html", "w") as f:
        f.write(report_html)

    # Open the generated report in the default browser
    os.system(f"open {report_data.user_input.report_name}.html")

    print(f"Report generated successfully: {report_data.user_input.report_name}.html")

if __name__ == '__main__':
    main()
