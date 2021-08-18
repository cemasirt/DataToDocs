#!/usr/bin/env python3

# This is free and unencumbered software released into the public
# domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a
# compiled binary, for any purpose, commercial or non-commercial, and
# by any means.

# In jurisdictions that recognize copyright laws, the author or
# authors of this software dedicate any and all copyright interest in
# the software to the public domain. We make this dedication for the
# benefit of the public at large and to the detriment of our heirs
# and successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to
# this software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# For more information, please refer to <http://unlicense.org>

# @author  Cem Asirt
# @version 0.1, 18/08/21

import os
import argparse
import yaml
import jinja2 

parser = argparse.ArgumentParser(description='This is a simple script that takes a YAML structured data file and creates a document using the data provided.')
parser.add_argument('data', type=str, help='YAML data file to be used')
parser.add_argument('template', type=str, help='templated HTML file to be used')
args = parser.parse_args()

# Initialize jinja environment
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# Open our example data file and load it with yaml module. Variables in our template file will be substituted with these.
with open(args.data) as fd:
    template_values = yaml.load(fd, Loader=yaml.FullLoader)

# Get the template file and then render it with values taken on previous step. Than output resulting page code to terminal.
template = JINJA_ENVIRONMENT.get_template(args.template)
site = template.render(template_values)
print(f'{site}')