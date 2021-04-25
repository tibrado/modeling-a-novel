from flask import Flask, render_template, request
import pipline as pipline 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    #mode = ['new', 'generated']
    if request.method == 'POST':
        text = request.form.get('text')
        print(text)

    return render_template('index.html', mode = 'new', story = pipline.make_story())
    