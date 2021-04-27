from flask import Flask, render_template, request
import pipline as pipline 

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        # random = int(request.form.get('randomness'))

        if text == '':
            text = 'Fire Ball!!'
        '''
        return render_template('index.html', mode = 'new', story = pipline.make_story(
            input_text = text, 
            randomness = 1,
            text_diversity = 40))
        '''

    return render_template('index.html', mode = 'new', story = 'Testing')

