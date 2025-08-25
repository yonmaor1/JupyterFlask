import os
import argparse

BARE_APP = '''from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
'''

INDEX_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask App</title>
</head>
<body>
    <h1>Welcome to your Flask app!</h1>
</body>
</html>
'''

def create_flask_app(target_dir):
    os.makedirs(target_dir, exist_ok=True)
    templates_dir = os.path.join(target_dir, 'templates')
    static_dir = os.path.join(target_dir, 'static')
    os.makedirs(templates_dir, exist_ok=True)
    os.makedirs(static_dir, exist_ok=True)
    # Create app.py
    app_py_path = os.path.join(target_dir, 'app.py')
    with open(app_py_path, 'w') as f:
        f.write(BARE_APP)
    # Create index.html
    index_html_path = os.path.join(templates_dir, 'index.html')
    with open(index_html_path, 'w') as f:
        f.write(INDEX_HTML)
    # Create requirements.txt
    requirements_path = os.path.join(target_dir, 'requirements.txt')
    with open(requirements_path, 'w') as f:
        f.write('Flask\n')
    print(f"Flask app scaffolded in {target_dir}")

def main():
    parser = argparse.ArgumentParser(description='Scaffold a bare-bones Flask app in a target directory.')
    parser.add_argument('target_dir', help='Directory to create the Flask app in')
    args = parser.parse_args()
    create_flask_app(args.target_dir)

if __name__ == '__main__':
    main()
