import yaml
from jinja2 import Template
import os

# 1. Load Intent file = Source of Truth file or device file which hold the device information and its role
data = yaml.safe_load(open("data/devices.yml"))

# 2. Load Jinja Template for compontent for which config needs to generate(ex. interface configuration)
template_text = open("templates/base.j2").read()
template = Template(template_text)

# 3. Create Output Folder(called as build) in Linux Server where this file will be running
os.makedirs("build", exist_ok=True)

# 4. loop through the each device and parse each key and put the value in template and generate the configuration 
for device in data["devices"]:
    config = template.render(**device)
    output_file = f"build/{device['hostname']}.cfg"
    with open(output_file, "w") as f:
        f.write(config)
    print("Generated:", output_file)
    print(config)
    print("-" * 40)
