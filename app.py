import json
from flask import request
from flask import Flask, render_template
app = Flask(__name__)
from crawler import crawl
from resume_pdf import get_resume

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/output.html', methods=['GET', 'POST'])
def output():
    return render_template('output.html')


@app.route('/input.html', methods=['GET', 'POST'])
def input():
    if request.method == "POST":
        output = request.get_json()
        result = json.loads(output)
        url = crawl(result.get("job")).strip()
        print(url)
        resume = get_resume(result.get("resume"))
        print(resume)
        return render_template('output.html', value = url)
    else:
        return render_template("input.html")

if __name__ == '__main__':
   app.run()
