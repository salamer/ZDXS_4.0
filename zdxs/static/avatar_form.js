$(document).ready(function(){
	$(".avatar_choose").click(function(){
		$(this).css("border","2px solid grey");
		
		
	});
	$(".avatar_choose").mouseover(function(){
		$(this).css("border","2px solid black");
	});
	$(".img-responsive").click(function(){
		href=$(this).attr("src");
		$("#id_avatar").val(href);
	})
})