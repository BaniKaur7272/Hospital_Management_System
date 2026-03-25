
window.onload = function(){

function createECG(chartId){

const ctx = document.getElementById(chartId);
if(!ctx) return;

// separate data for each graph
let data = [];

for(let i=0;i<40;i++){
data.push(Math.random()*2 + 78);
}

const chart = new Chart(ctx,{
type:"line",
data:{
labels:data.map((_,i)=>i),
datasets:[{
data:data,
borderColor:"#ff3b3b",
borderWidth:2,
pointRadius:0,
tension:0,

// ✨ glow effect
borderJoinStyle:'round'
}]
},
options:{
animation:false,
plugins:{legend:{display:false}},
scales:{
x:{display:false},
y:{display:false}
}
}
});

// animation
setInterval(()=>{

let spike = Math.random();

if(spike > 0.94){
data.push(96);
}else{
data.push(Math.random()*2 + 78);
}

data.shift();
chart.update();

},120);

}

// create charts for both patients
createECG("ecgChart1");
createECG("ecgChart2");

}

