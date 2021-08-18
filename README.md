# DataToDocs
## _Using YAML formatted data in documents with template support_

[![Python](https://www.python.org/static/community_logos/python-powered-w-70x28.png)](https://www.python.org/)

This is a simple script that takes a YAML structured data file and creates a document using the data provided.
For referencing data in the document Jinja2 templating engine is used. For info on usage and syntax, please visit official [Jinja2] website.

## Installation
```bash
git clone --depth=1 https://github.com/cemasirt/DataToDocs.git
cd DataToDocs
python3 -m venv converter
.\converter\Scripts\activate (OR source bin/activate on Linux)
pip3 install -r requirements.txt
```

## Usage
```bash
.\converter\Scripts\python.exe converter.py example_data.yml example_template.html > policy.html
```

```bash
usage: converter.py [-h] data template

This is a simple script that takes a YAML structured data file and creates a document using the data provided.

positional arguments:
  data        YAML data file to be used
  template    templated HTML file to be used

optional arguments:
  -h, --help  show this help message and exit
```

[Jinja2]:  <https://jinja.palletsprojects.com/en/3.0.x>