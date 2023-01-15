import json
from flask import request
from flask import Flask, render_template, redirect, url_for, session
app = Flask(__name__)
from crawler import crawl
from resume_pdf import get_resume

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/output.html', methods=['GET', 'POST'])
def output():
    with open('job.txt', 'r') as file:
        job = file.read()
    with open('resume.txt', 'r') as file:
        resume = file.read()
    return render_template('output.html', job=job, resume=resume)


@app.route('/input.html', methods=['GET', 'POST'])
def input():
    if request.method == "POST":
        output = request.get_json()
        result = json.loads(output)
        job = crawl(result.get("job")).strip()
        print(job)
        with open('job.txt', 'w') as f:
            f.write(job)
        resume = get_resume(result.get("resume"))
        print(resume)
        with open('resume.txt', 'w') as f:
            f.write(resume)
        return render_template("output.html")
    else:
        return render_template("input.html")

if __name__ == '__main__':
   app.run()
