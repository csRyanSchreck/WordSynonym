//Function for the button onclick. This function prevents automatic reloading and will fetch the data from the api and update the DOM content
async function resultsUpdate(event){
    event.preventDefault(); //Prevent the reloading when form submitted

    const distanceDiv = document.getElementById('distance'); 
    const timeDiv =document.getElementById('time')
    //Get the json of the data by fetching from the api 
    const response  = await fetch('/results', {method: 'POST',body: new FormData(document.forms["form"])})
    const data = await response.json()
    distanceDiv.textContent = data.shortestpath;
    timeDiv.textContent = data.time;
    
    //Call the function to create the graph visualization
    createGraph(data.nodes);
}

//This function will create the graph visualization by taking in the vertcies in the shortest word path
function createGraph(vertices){
  //This for loop will create a list of dictionaries that assign a unique id to a vertex
  //Also edges are made where it connects vertex to the next vertex
  let dictVert = [];
  let dictEdge=[]
  for(let i=0;i<vertices.length;i++)
  {
    dictVert.push({id:i,label:vertices[i]});
    if(i!=vertices.length-1)
      dictEdge.push({from:i, to:i+1})
  }

  //Assign the nodes and edges
  var nodes = new vis.DataSet(dictVert);

  var edges = new vis.DataSet( dictEdge);

  // code template from vis.js documentation example https://visjs.github.io/vis-network/docs/network/
  var container = document.getElementById("mynetwork");
  var data = {
    nodes: nodes,
    edges: edges
  };
  var options = {width:'1000px',height:'500px',edges:{arrows:{to:{enabled:true}}}};
  var network = new vis.Network(container, data, options);
}