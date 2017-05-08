addEventListener("keydown", keydown);
autosize(document.querySelector('textarea'));

$(".field").change(function() {
	if($(this).hasClass("incorrect")){
		$(this).removeClass("incorrect");
		show_error(false);	
	}
});

function getXmlHttp() {
    var xmlhttp;
    try {
        xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
    } catch (e) {
        try {
            xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        } catch (E) {
            xmlhttp = false;
        }
    }
    if (!xmlhttp && typeof XMLHttpRequest != 'undefined') {
        xmlhttp = new XMLHttpRequest();
    }
    return xmlhttp;
}

function send_push(){
	
	if(fields_incorrect() === false){
		//alert('incorrect');
	}else{
		result();
	}
}

function result() {
	
    var a = "title=" + document.getElementById("title").value + "&name=" + document.getElementById("name").value + "&post=" + document.getElementById("post").value;
    var xmlhttp = getXmlHttp();
    xmlhttp.open('POST', '', true);
    xmlhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xmlhttp.send(a);
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4) {
            if (xmlhttp.status == 200)
                document.location.href = xmlhttp.responseText;
        }
    }
}

function keydown(e){
	if (e.keyCode === 13) {
		nextfocus();
    }
}

function nextfocus(){
	if($("#name").is(":focus") ){
		document.getElementById('post').focus();
			
	}
	if($("#title").is(":focus") ){
		document.getElementById('name').focus();			
	}
}

function fields_incorrect(){
	var title = $("#title").val();
	var name = $("#name").val();
	var post = $("#post").val();
	var key = true;
	
	if ($("#title").val().length <= 2){
		$("#title").addClass("incorrect");
		show_error(true, "field is too short");
		key = false;	
	}
	if ($("#name").val().length <= 1){
		$("#name").addClass("incorrect");
		show_error(true, "field is too short");
		key = false;	
	}
	return key;
}

function show_error(status = true, value = "", add = false){
	if(status === true){
		if(add === true){
			var t = $("#error").text();
			$("#error").text(t + "<br>" + value);
		}else{
			$("#error").text(value);
		}		
	}else if(status === false){
		$("#error").text('');
	}	
}