//Function for the button onclick. This function prevents automatic reloading and will fetch the data from the api and update the DOM content
async function resultsUpdate(event){
    event.preventDefault(); //Prevent the reloading when form submitted

    const contentDiv = document.getElementById('distance'); 
    
    //Get the json of the data by fetching from the api 
    const response  = await fetch('/results', {method: 'POST',body: new FormData(document.forms["form"])})
    const data = await response.json()
    contentDiv.textContent = data.shortestpath;
    
    //Call the function to create the graph visualization
    createGraph(data.nodes);
}

function createGraph(vertices){
    
  var nodes = new vis.DataSet([
    { id: 1, label: vertices[0] },
    { id: 2, label: vertices[1] },
    { id: 9, label: vertices[2] },
    { id: 4, label: vertices[3] },
    { id: 5, label: vertices[4] }
  ]);

  var edges = new vis.DataSet([
    { from: 1, to: 9 },
    { from: 1, to: 2 },
    { from: 2, to: 4 },
    { from: 2, to: 5 },
    { from: 9, to: 9 }
  ]);

  // create a network
  var container = document.getElementById("mynetwork");
  var data = {
    nodes: nodes,
    edges: edges
  };
  var options = {width:'1000px',height:'500px',edges:{arrows:{to:{enabled:true}}}};
  var network = new vis.Network(container, data, options);
}