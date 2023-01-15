import json
from flask import request
from flask import Flask, render_template
app = Flask(__name__)
from crawler import crawl
from resume_pdf import get_resume


@app.route('/')
def index():
    return render_template('input.html')

@app.route('/test', methods=['POST'])
def test():
    output = request.get_json()
    result = json.loads(output)
    url = crawl(result.get("job"))
    print(url)
    resume = get_resume(result.get("resume"))
    print(resume)
    return result
