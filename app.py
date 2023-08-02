from flask import Flask, render_template, request,jsonify

app = Flask(__name__,template_folder='templates')
app.config['STATIC_FOLDER'] = 'static'

@app.route('/',methods=['GET'])
def index():
    return render_template('home.html')


#Simple API to get back the distance and the word path 
@app.route('/results', methods=['POST'])
def get_results():
    word1 = request.form.get('word1')
    word2 = request.form.get('word2')
    algorithm = request.form.get('algorithm')
    
    data = {
        'message': algorithm,
    }
    return jsonify(data)