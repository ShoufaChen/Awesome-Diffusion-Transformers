import json
from datetime import datetime

content = """
# [Awesome Diffusion Transformers](https://www.shoufachen.com/Awesome-Diffusion-Transformers/) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

"""


# write table headers
content += "| Title | Initial Date | Venue | Task | Resource |\n"
content += "| --- | --- | --- | --- | --- |\n"

badges = {
    "image": "![](./assets/image.svg)",
    "video": "![](./assets/video.svg)",
    "3d": "![](./assets/3d.svg)",
    "speech": "![](./assets/speech.svg)",
    "others": "![](./assets/others.svg)",
    "code": "[![](./assets/code.svg)]({})",
    "website": "[![](./assets/website.svg)]({})",
}

data = json.loads(open("data.json").read())

# Convert the "Initial Date" from string to datetime object for accurate sorting
for item in data:
    item["Initial Date"] = datetime.strptime(item["Initial Date"], "%d %b %Y")

# Sort the items by "Initial Date"
data = sorted(data, key=lambda x: x["Initial Date"])

# Convert the "Initial Date" back to string format for displaying
for item in data:
    item["Initial Date"] = item["Initial Date"].strftime("%d %b %Y")

for row in data:
    content += f"| [{row['Title']}]({row['Link']}) | {row['Initial Date']} | {row['Venue']} | "
    # {row['Task']} | {row['Resource']} |\n
    for task in row['Task']:
        content += f"{badges[task.lower()]} "
    content += f"| "
    for k, v in row['Resource'].items():
        content += badges[k.lower()].format(v) + " "
    content += f"| \n"

content += \
"""

## Contributing

Your contributions are always welcome!

Feel free to add/update contents in the [data.json](./data.json) file.

This README and the [website](https://www.shoufachen.com/Awesome-Diffusion-Transformers) will be updated automatically, powered by GitHub Actions.

🚀 🚀 🚀
"""

with open("README.md", "w") as readme:
    readme.write(content)
