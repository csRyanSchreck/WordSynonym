from flask import Flask, render_template, request,jsonify
from main import createGraph
app = Flask(__name__,template_folder='templates')
app.config['STATIC_FOLDER'] = 'static'

#Call the function createGraph to get the graph object
graph = createGraph()

#Main url that renders the home template for users to submit the words for the shortest path
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
    if algorithm=="bfs":
        shortest, execution_time, shortest_path = graph.bfs(word1, word2)
    elif algorithm=="dijkstra":
        shortest, execution_time, shortest_path = graph.djikstra(word1, word2)
    else:
        shortest="nothing"
    
    #json data for the shortest path, time taken,nodes, and edges
    data = {
        'shortestpath': shortest,
        'time':execution_time,
        'nodes':shortest_path
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()
