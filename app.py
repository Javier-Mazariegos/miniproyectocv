from flask import Flask, url_for
from jinja2 import Template, Environment, FileSystemLoader
import yaml

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

app = Flask(__name__)
with open('data.yml') as yaml_file:
    my_yaml = yaml.load(yaml_file)

@app.route('/index')
@app.route('/')
def index():
    template = env.get_template('index.html')
    image_file = url_for('static', filename=my_yaml['fotografia'])
    css = url_for('static', filename= 'style.css')
    return template.render(my_data=my_yaml, image_file= image_file, style_sheet= css)

@app.route('/CV')
def curriculum():
    template = env.get_template('cv.html')
    image_file = url_for('static', filename=my_yaml['fotografia'])
    css = url_for('static', filename= 'style.css')
    return template.render(my_data=my_yaml, image_file= image_file, style_sheet= css)

if __name__ == "__main__":
    app.run(host="localhost",port=5000,debug= True)