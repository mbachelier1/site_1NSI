/*
<script>
function reactionText1(){
	var msg;
	var reponse=document.getElementById("reponse1");
	if (reponse.value ==='20'){
		msg='bravo';
		style='style="color:green;"';
		}
	else{msg='non, essaye encore';
	style='style="color:red;"';}
		document.getElementById("messageText1").innerHTML='<p '+style+'>'+msg+'</p>';
		
	}
function reactionText2(){
	var msg;
	var reponse=document.getElementById("reponse2");
	if (reponse.value ==='n'){
		msg='bravo';
		style='style="color:green;"';
		}
	else{msg='non, essaye encore';
	style='style="color:red;"';}
		document.getElementById("messageText2").innerHTML='<p '+style+'>'+msg+'</p>';
		setTimeout(console.log,4000,'')
	}
function reactionQCU1(){
var style;
var msg;
var reponse = document.getElementById("test1");
var rep=reponse.elements["test"].value;
console.log(rep);
if (rep=="A"){msg='bonne réponse';
style='style="color:green;"';
}
else {msg='mauvaise reponse';
style='style="color:red;"';}
document.getElementById("messageQCU1").innerHTML='<p '+style+'>'+msg+'</p>';
}
</script>
	*/