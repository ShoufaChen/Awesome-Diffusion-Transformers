import json
from datetime import datetime

content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <title>Awesome Diffusion Transformers</title>
    <link rel="icon" type="image/png" href="assets/smiley.png">
    <link href="./assets/style.css" rel="stylesheet">
    <style>
        .title-with-icon-container {
            display: flex;
            justify-content: center; /* Center the container's content */
            align-items: center;
            position: relative; /* Needed for absolute positioning of the icon */
        }
        .title {
            display: inline; /* Display inline for tighter control over positioning */
        }
        .github-link {
            margin-left: 10px; /* Small gap between the title and the icon, adjust as needed */
            font-size: 24px; /* Adjust size as needed */
            color: black; /* Icon color */
            vertical-align: middle; /* Align with the middle of the text if needed */
        }
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            text-align: center;
            padding: 8px;
        }
        td:first-child, th:first-child {
            text-align: left;
        }
        th#dateHeader {
            min-width: 110px; /* Adjust as needed */
            cursor: pointer; /* Change cursor on hover */
            position: relative; /* Allows absolute positioning of sort icons */
        }
        /* Initial grey arrows */
        th#dateHeader::after, th#dateHeader::before {
            font-size: 0.8em;
            color: grey; /* Grey color by default */
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
        }
        th#dateHeader::after {
            content: "▲";
            right: 5px; /* Adjust as needed */
        }
        th#dateHeader::before {
            content: "▼";
            right: 20px; /* Adjust as needed */
        }
        /* Active state styles - ensure specificity to override */
        th#dateHeader.active.asc::after, th#dateHeader.active.desc::before {
            color: black; /* Darker color for active state */
        }
    </style>
    <script>
        // Initial sort direction
        let sortDirection = 'asc';

        function sortTableByDate() {
            var table, rows, switching, i, x, y, shouldSwitch;
            table = document.getElementById("myTable");
            switching = true;

            while (switching) {
                switching = false;
                rows = table.rows;

                for (i = 1; i < rows.length - 1; i++) {
                    shouldSwitch = false;

                    x = rows[i].getElementsByTagName("TD")[1];
                    y = rows[i + 1].getElementsByTagName("TD")[1];

                    let date1 = parseDate(x.innerHTML.trim());
                    let date2 = parseDate(y.innerHTML.trim());

                    if (sortDirection === 'asc' && date1 > date2) {
                        shouldSwitch = true;
                        break;
                    } else if (sortDirection === 'desc' && date1 < date2) {
                        shouldSwitch = true;
                        break;
                    }
                }

                if (shouldSwitch) {
                    rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                    switching = true;
                }
            }

            // Toggle the direction for next sort
            sortDirection = sortDirection === 'asc' ? 'desc' : 'asc';
            updateSortIndicator();
        }

        function parseDate(dateStr) {
            // Parses date strings in the format "28 Dec 2022" to Date objects
            const parts = dateStr.match(/(\d{1,2}) (\w+) (\d{4})/);
            return new Date(parts[3], 'JanFebMarAprMayJunJulAugSepOctNovDec'.indexOf(parts[2]) / 3, parts[1]);
        }

        function updateSortIndicator() {
            const header = document.querySelector("#dateHeader");
            // Remove previous states
            header.classList.remove("active", "asc", "desc");
            
            // Add 'active' class and current sort direction as class
            header.classList.add("active");
            if (sortDirection === 'asc') {
                header.classList.add("asc");
            } else {
                header.classList.add("desc");
            }
        }

        function filterTableByTask() {
            var filterValue, table, tr, td, i, img, matchFound;
            filterValue = document.getElementById("taskFilter").value.toUpperCase();
            table = document.getElementById("myTable");
            tr = table.getElementsByTagName("tr");

            for (i = 1; i < tr.length; i++) {
                tr[i].style.display = "none"; // Default to hiding rows, to be shown based on matching criteria
                td = tr[i].getElementsByTagName("td")[3]; // Assuming the Task is in the 4th column
                if (td) {
                    img = td.getElementsByTagName("img");
                    matchFound = false;
                    for (var j = 0; j < img.length; j++) {
                        var altText = img[j].alt.toUpperCase();
                        if (filterValue === "ALL") {
                            matchFound = true;
                            break;
                        } else if (filterValue === "OTHERS") {
                            if (["IMAGE", "VIDEO", "3D", "SPEECH"].indexOf(altText) === -1) {
                                matchFound = true;
                                break;
                            }
                        } else if (altText === filterValue) {
                            matchFound = true;
                            break;
                        }
                    }
                    if (matchFound) {
                        tr[i].style.display = ""; // Show row if a match is found
                    }
                }
            }
        }
    </script>
</head>
<body>

<div class="title-with-icon-container">
    <h1 class="title">Awesome Diffusion Transformers</h1>
    <a href="https://github.com/ShoufaChen/Awesome-Diffusion-Transformers" class="github-link" target="_blank">
        <i class="fab fa-github"></i>
    </a>
</div>

<div class="content">
    <table id="myTable" border="1">
        <tr>
            <th>Title</th>
            <th id="dateHeader" class="sort-indicator" onclick="sortTableByDate()">Date</th>
            <th>Venue</th>
            <th>
                Task
                <select id="taskFilter" onchange="filterTableByTask()">
                    <option value="all">All Tasks</option>
                    <option value="Image">Image</option>
                    <option value="Video">Video</option>
                    <option value="3D">3D</option>
                    <option value="Speech">Speech</option>
                    <!-- Add other task types as needed -->
                    <option value="Others">Others</option>
                </select>
            </th>
            <th>Resource</th>
        </tr>
"""

badges = {
    "image": '<img src="./assets/image.svg" alt="Image"/>',
    "video": '<img src="./assets/video.svg" alt="Video"/>',
    "3d": '<img src="./assets/3d.svg" alt="3D"/>',
    "speech": '<img src="./assets/speech.svg" alt="Speech"/>',
    "others": '<img src="./assets/others.svg" alt="Others"/>',
    "code": '<a href="{}"><img src="./assets/code.svg" alt="Code"/></a>',
    "website": '<a href="{}"><img src="./assets/website.svg" alt="Website"/></a>',
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
    content += f'<tr><td><a href="{row["Link"]}">{row["Title"]}</a></td><td>{row["Initial Date"]}</td><td>{row["Venue"]}</td><td>'
    for task in row['Task']:
        content += f'{badges[task.lower()]} '
    content += '</td><td>'
    for k, v in row['Resource'].items():
        content += badges[k.lower()].format(v) + " "
    content += '</td></tr>\n'

content += """
</table>
</div>
</body>
</html>
"""
with open("index.html", "w") as html:
    html.write(content)
