from flask import Flask, render_template, request,jsonify
from main import createGraph
app = Flask(__name__,template_folder='templates')
app.config['STATIC_FOLDER'] = 'static'

#Call the function createGraph to get the graph object
graph = createGraph()

@app.route('/',methods=['GET'])
def index():
    return render_template('home.html')


#Simple API to get back the distance and the word path 
@app.route('/results', methods=['POST'])
def get_results():
    word1 = request.form.get('word1')
    word2 = request.form.get('word2')
    algorithm = request.form.get('algorithm')
    
    #Use the graph object to call the correct algorithm and get the data for the shortest path, time elapsed, and the data for visualization
    
    data = {
        'message': algorithm,
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()