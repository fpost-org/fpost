function serializejson(){
	ar = [];
	i = 1;
	$("#container").children().each(function(index, element){
		if ($(this).hasClass("post")){
			content = $(this).val().replace(/[\n\r]/g, '');
			ar.push('"p'+String(i)+'":{"type":"text","content":"' + encodeURIComponent(content) + '"}');
			i = i+1;
		}else if($(this).is('p')){
			
		}else if( ($(this).is('div')) && ($(this).hasClass("social_media")) ){
			c = check_link($(this).children(".postsocial").html());
			ar.push('"p'+String(i)+'":{"type":"youtube","content":"' + encodeURIComponent(c) + '"}');
			i = i+1;
		}
	});
	var st = "{";
	for (i = 0; i < ar.length; ++i) {
	    if(i!= 0){st+=","}
		st += ar[i];
	}
	st += "}";
	return st;
}