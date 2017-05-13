function serializejson(){
	ar = [];
	$("#container").children().each(function(index, element){
		if ($(this).hasClass("post")){
			ar.push('{"type":"text","content":"' + $(this).val() + '"}');
		}else if($(this).nodeName = 'p'){
			
		}	
	});
	
	return ar;
}