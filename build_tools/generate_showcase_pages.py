import os
import yaml
from jinja2 import Environment, FileSystemLoader

# Get script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the absolute path to the templates directory and showcase directory
templates_dir = os.path.abspath(os.path.join(script_dir, './templates'))
showcase_source_dir = os.path.abspath(os.path.join(script_dir, '../showcase'))
showcase_target_dir = os.path.abspath(os.path.join(script_dir, '../docs/showcase'))
print(f"Templates directory: {templates_dir}")
print(f"Showcase source directory: {showcase_source_dir}")
print(f"Showcase target directory: {showcase_target_dir}")

# Use templates_dir as the base for your FileSystemLoader
env = Environment(loader=FileSystemLoader(templates_dir))

# Then you can access your templates like so
project_template = env.get_template('_project_template.md')
index_template = env.get_template('_showcase_page_template.md')

# Loop over all .md files in showcase target directory and delete them unless they start with "_"
for filename in os.listdir(showcase_target_dir):
    if filename.endswith(".md") and not filename.startswith("_"):
        os.remove(os.path.join(showcase_target_dir, filename))

index_links = []

# Transform each source showcase into a target showcase file
for filename in os.listdir(showcase_source_dir):
    if filename.startswith("_") or not filename.endswith(".yaml"):
        continue

    with open(os.path.join(showcase_source_dir, filename), 'r') as stream:
        try:
            # Load yaml file
            print(f"Processing {filename}")
            data = yaml.safe_load(stream)

            # Generate markdown content using the template
            md_content = project_template.render(data)

            # Write markdown content to file
            output_filename = filename.replace(".yaml", ".md")
            with open(os.path.join(showcase_target_dir, output_filename), 'w') as md_file:
                md_file.write(md_content)

            # Store link to this project for the index file
            index_links.append({'name': data.get("name", ""), 'filename': output_filename})
        except yaml.YAMLError as exc:
            print(exc)

# Create index.md including all generated showcases
with open(os.path.join(showcase_target_dir, 'index.md'), 'w') as index_file:
    index_file.write(index_template.render(projects=index_links))

print(f"Generated {len(index_links)} project pages.")
