import os
import shutil
import leafmap.maplibregl as leafmap

url = "https://github.com/giswqs/leafmap/archive/refs/heads/master.zip"
out_zip = "leafmap-master.zip"
leafmap.download_file(url, out_zip)

in_dir = "leafmap-master/docs/maplibre"
out_dir = "maplibre"

ignore_files = [
    "3d_pmtiles.ipynb",
    "animate_a_line.ipynb",
    "fields_of_the_world.ipynb",
    "mapillary.ipynb",
    "live_update_feature.ipynb",
]


leafmap.execute_maplibre_notebook_dir(
    in_dir, out_dir, replace_api_key=True, ignore_files=ignore_files
)

shutil.rmtree("leafmap-master")
os.remove("leafmap-master.zip")

in_dir = "demos"
out_dir = "demos-html"
shutil.copytree(in_dir, out_dir)
leafmap.execute_maplibre_notebook_dir(
    in_dir, out_dir, keep_notebook=True, replace_api_key=True
)

html_files = leafmap.find_files(out_dir, "*.html")
for file in html_files:
    shutil.copyfile(file, os.path.join("demos", os.path.basename(file)))

shutil.rmtree(out_dir)

leafmap.generate_index_html("demos")


def generate_index_html(directories, output_file):
    # Start the HTML content
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Directory Listing</title>
</head>
<body>
    <h1>Directory Listing</h1>
    <ul>
"""

    for directory in directories:
        if os.path.isdir(directory):
            html_content += f"<li><strong>{directory}</strong></li><ul>"
            all_files = []
            for root, dirs, files in os.walk(directory):
                for filename in files:
                    file_path = os.path.join(root, filename)
                    all_files.append(file_path)

            # Sort files alphabetically
            all_files.sort()

            for file_path in all_files:
                # Get the relative path to the file from the base directory
                relative_path = os.path.relpath(file_path, start=directory)
                html_content += f'<li><a href="{directory}/{relative_path}">{relative_path}</a></li>'
            html_content += "</ul>"

    # Close the HTML content
    html_content += """
    </ul>
</body>
</html>
"""

    # Write the HTML content to the output file
    with open(output_file, "w") as f:
        f.write(html_content)


# Specify the directories to list
directories_to_list = ["styles", "demos", "maplibre"]
# Specify the output HTML file
output_html_file = "index.html"

generate_index_html(directories_to_list, output_html_file)
