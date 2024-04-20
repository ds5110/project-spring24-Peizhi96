import uuid
from jinja2 import Environment, FileSystemLoader
from template_data import ReportData, UserInput
import os
import model
import argparse

# Parse command line
def parse() -> UserInput:
    # Check valid input
    parser = argparse.ArgumentParser(description="Generate a report")
    parser.add_argument("--start_year", type=int, help="starting year of this report", required=True)
    parser.add_argument("--end_year", type=int, help="ending year of this report", required=True)
    parser.add_argument("--report_name", type=str, help="Name of the report", required=True)
    parser.add_argument("--region", type=str, help="Landing region (Maine or New England)", required=True)

    args = parser.parse_args()  

    user_input = UserInput()
    user_input.start_year = args.start_year
    user_input.end_year = args.end_year
    user_input.report_name = str(args.report_name).replace(' ', '_')
    user_input.region = args.region
    
    return user_input
    

def main():
    # Report dataclass
    report_data = ReportData()
    report_data.user_input = parse()

    # Report uuid
    report_data.report_id = uuid.uuid1()
    
    # Make sure the report_name is unique by using UUID
    output_file_name = report_data.user_input.report_name

    if os.path.exists(f'{output_file_name}.html'):
        output_file_name = f'{output_file_name}_{report_data.report_id}'

    # Load report template
    template_loader = FileSystemLoader(searchpath="src/")
    templateEnv = Environment(loader=template_loader)
    template = templateEnv.get_template("template.html")

    # Calcualte data
    model.process(data=report_data)

    # Render the template with data object
    report_html = template.render(report_data=report_data)

    # Save the generated report
    with open(f'{output_file_name}.html', "w") as f:
        f.write(report_html)

    # Open the generated report in the default browser
    os.system(f"open {output_file_name}.html")

    print(f"Report generated successfully: {output_file_name}.html")

if __name__ == '__main__':
    main()
