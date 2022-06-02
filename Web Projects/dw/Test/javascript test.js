// JavaScript Document
function ok(){
	document.getElementById('ok').innerHTML='Hello';
	document.getElementById('ok').style.fontSize='5px';
	window.alert('hai Friends');
	window.print();
}
function hee(){
	var y,x,zz,z,zzz,t,tt,xx,d,h;
	xx = [1,45,23,22,45,2,7];
	zz="hello"
	zzz=zz.replace("hello","hai")
	/*zz=undefined*/
	xx.sort(function(a,b){return(a-b)});
	y=10;
	y+=10;
	t=1.7687435;
	tt=t.toFixed(4)
	z={hello:"34",Hai:"56",he:"87"}
	z.hello="55555"
	document.getElementById("he").style.color = "red";
	document.getElementById("he").style.fontSize = "12px";
	x=["hello","frinds","how r u"]
	x.push("push");
	x=x.concat("haiii");
	x.splice(2,0,"uu","vvv");
	x.splice(1,1);
	x.sort();
	h=(y>4)? "ok" : "no" ;
	d=new Date();
	/*d.setFullYear(2000)*/
	document.getElementById('he').innerHTML=/*[]    y +"<br>"+ typeof y +"<br>"+ x +"<br>"+ typeof x + "<br>" + z.hello+"<br>"+typeof z +"<br>"+typeof zz + "<br>"+d +"<br>"+d.toUTCString()+"<br>"+new Date(2012,11,30,12,33,9)+"<br>"+Date.parse(2021,09,17)+"<br>"+d.getFullYear()+"<br>"+ zz.slice(1,4)+ "<br>" + zzz.substr(0) + "<br>" + zz.concat(zzz,"how are you")+"<br>"+zz[0]+"<br>"+zz.charAt(2)   /*   +"<br>"+zz.charCodeAt(3) + "<br>"+zz.indexOf("h")+"<br>"+ zz.codePointAt(1)  */   /*[]      +"<br>"+zz.length+"<br>"+"biney value of 10 is :"+y.toString(2)+"<br>"+y.toExponential(20)+"<br>"+t+"<br>"+tt+"<br>"+y.valueOf()+"<br>"+Number("10")+"<br>"+Number("10 90")+"<br>"+parseInt("12 90")+"<br>"+parseInt("78 hai")+"<br>"+x[1]+"<br>"+x.slice(1)+"<br>"+x.slice(2,6)+"<br>"+xx+"<br>"+xx.reverse()+"<br>"+xx.indexOf(2)+"<br>"+Math.round(t)+"<br>"+Math.ceil(t)+"<br>"+Math.floor(t)+"<br>"+Math.sign(t)+"<br>"+Math.trunc(t)    []*/
		Math.pow(2,3)+"<br>"+Math.sqrt(400)+"<br>"+Math.abs(-23456789)+"<br>"+Math.sin(90*Math.PI/180)+"<br>"+Math.cos(0*Math.PI/180)+"<br>"+Math.min(1,3,56,23,4,7,8)+"<br>"+Math.max(57,1,08,02,8,99,0)+"<br>"+Math.random()+"<br>"+Math.log(1)+"<br>"+Math.floor(Math.random()*100+1)+"<br>"+h+"<br>"+typeof d +"<br>"+ d.constructor;
	
}
function remove(){
document.getElementById("hide").style.display="none";
}
function random(min,max){
	document.getElementById("random").innerHTML= Math.floor(Math.random()*(max-min+1/*to include max*/))+min/*for start from min*/;
	console.log("hai");
}