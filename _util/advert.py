import os
import sys
import yaml

email = """
To: scan-seminar-l@cornell.edu
Subject: SCAN seminar: {name}, 1:25 pm, {date:%x}

Title: {title}
Speaker: {name}
Time: {date:%x}, 1:25-2:15
Location: 406 Gates

Abstract:
{abstract}
"""

for fname in sys.argv[1:]:
    # Slurp up the post file
    with open(fname, 'r') as f:
        lines = f.readlines()

    # Extract date
    date = yaml.load(os.path.basename(fname)[0:10])

    # Split out header block and body text
    header = ""
    body = ""
    in_header = True
    for l in lines[1:]:
        if in_header:
            if l == "---\n":
                in_header = False
            else:
                header += l
        else:
            body += l

    # Parse header block and plug in date
    hdata = yaml.load(header)
    hdata['name'] = "{name} ({affil})".format(**hdata['speaker'])
    hdata['date'] = date
    hdata['abstract'] = body

    # Format the email
    print(email.format(**hdata))
