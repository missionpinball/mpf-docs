import os
import yaml
from jinja2 import Environment, FileSystemLoader

# Get script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the absolute path to the templates directory
templates_dir = os.path.join(script_dir, '../docs/projects')
templates_dir = os.path.abspath(templates_dir)
print(f"Templates directory: {templates_dir}")

# Use templates_dir as the base for your FileSystemLoader
env = Environment(loader=FileSystemLoader(templates_dir))

# Then you can access your templates like so
project_template = env.get_template('_project_template.md')
index_template = env.get_template('_project_list_template.md')

# Loop over all .md files in /docs/projects directory and delete them unless they start with "_"
for filename in os.listdir(templates_dir):
    if filename.endswith(".md") and not filename.startswith("_"):
        os.remove(os.path.join(templates_dir, filename))

# Define directories for .yaml files and output
root_dir = os.path.join(script_dir, '../projects')
output_dir = templates_dir
index_links = []

for filename in os.listdir(root_dir):
    if filename.startswith("_") or not filename.endswith(".yaml"):
        continue

    with open(os.path.join(root_dir, filename), 'r') as stream:
        try:
            # Load yaml file
            print(f"Processing {filename}")
            data = yaml.safe_load(stream)

            # Generate markdown content using the template
            md_content = project_template.render(data)

            # Write markdown content to file
            output_filename = filename.replace(".yaml", ".md")
            with open(os.path.join(output_dir, output_filename), 'w') as md_file:
                md_file.write(md_content)

            # Store link to this project for the index file
            index_links.append({'name': data.get("name", ""), 'filename': output_filename})
        except yaml.YAMLError as exc:
            print(exc)

# Create index.md
with open(os.path.join(output_dir, 'index.md'), 'w') as index_file:
    index_file.write(index_template.render(projects=index_links))

print(f"Generated {len(index_links)} project pages.")
