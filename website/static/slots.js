var stateObject={
    "Andaman and Nicobar Islands":[
    {district_id:"3",district_name:"Nicobar"},	
	{district_id:"1",district_name:"North and Middle Andaman"},
	{district_id:"2",district_name:"South Andaman"}
  ],
  
  "Andhra Pradesh":
	[
    {district_id:"9",district_name:"Anantapur"},	
	{district_id:"10",district_name:"Chittoor"},
	{district_id:"11",district_name:"East Godavari"},
	{district_id:"5",district_name:	"Guntur	"},
	{district_id:"4",district_name:"Krishna	"},
	{district_id:"7",district_name:"Kurnool	"},
	{district_id:"12",district_name:"Prakasam	"},
	{district_id:"13"	,district_name:"Sri Potti Sriramulu Nellore"},
	{district_id:"14",district_name:"Srikakulam	"},
	{district_id:"8",district_name:"Visakhapatnam	"},
	{district_id:"15",district_name:"Vizianagaram"},
	{district_id:"16",district_name:"West Godavari"},
	{district_id:"6",district_name:"YSR District, Kadapa (Cuddapah)"}
]
  }/**
	"Assam":[{"46":"Baksa	Assam"},
	{"47":"Barpeta	Assam"},
	{"765":"Biswanath	Assam"},
	{"57":"Bongaigaon	Assam"},
	{"66":"Cachar	Assam"},
	{"766"	:"Charaideo	Assam"},
	{"58"	:"Chirang	Assam"},
	{"48"	:"Darrang	Assam"},
	{"62"	:"Dhemaji	Assam"},
	{"59"	:"Dhubri	Assam"},
	{"43":"Dibrugarh	Assam"},
	{"67"	:"Dima Hasao	Assam"},
	{"60"	:"Goalpara	Assam"},
	{"53"	:"Golaghat	Assam"},
	{"68"	:"Hailakandi	Assam"}]
  }
  */
/**var stateObject = {
  "India": 
  [ "Delhi",
  "Kerala",
  "Goa",
  ],
  "Australia":
   [
  "South Australia",
  "Victoria"
  ], 
  "Canada": 
  [
  "Alberta",
  "Columbia"
  ],
  }*/
  window.onload = function ()
   {
  var countySel = document.getElementById("countySel")
  var stateSel = document.getElementById("stateSel")
  for (var country in stateObject) 
  {
  countySel.options[countySel.options.length] = new Option(country, country);
  }
  countySel.onchange = function () 
  {
  stateSel.length = 1; // remove all options bar first
  if (this.selectedIndex < 1) return; // done
  for (var state in stateObject[this.value])
   {
     state=stateObject[this.value][state].district_name;
  stateSel.options[stateSel.options.length] = new Option(state, state);
  }
  }
  countySel.onchange(); // reset in case page is reloaded
  stateSel.onchange = function () {
  if (this.selectedIndex < 1) return; // done
  var id_final;
  for(var state in stateObject[countySel.value])
  {
      if(stateSel.value===state.district_name)
       id_final=state.district_id
  }
  }
}
