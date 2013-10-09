$(function(){
	setInterval("ToggleShow()",5000);

	/*email tip*/
	$("#input-email").on("keydown keyup",function(){
		var mail = $.trim($(this).val());
		if(mail != ""){
			$(this).prev().addClass("hide");
		}
		else{
			$(this).prev().removeClass("hide");
		}
	});

	/*join us*/
	$("#join>ul>li").on("click", function(){
		if($(this).hasClass("cur-infor")){
			return false;
		}
		var cur_infor = $("#join>ul>li.cur-infor");
		cur_infor.removeClass("cur-infor");
		$(this).addClass("cur-infor");
	});

	/*headshot hover*/
	$("#right-photo>ul>li").hover(function(){
		var cover = $(this).children("p");
		if(cover.is(":animated")){
			return false;
		}
		$(this).children("p").fadeIn("200");
	},function(){
		$(this).children("p").fadeOut("100");
	});

	/*join us hover*/
	/*$("#right-photo>a.join-us").hover(function(){
		if($(this).is(":animated")){
			return false;
		}
		$(this).animate({opacity:1},300,function(){});
	},function(){
		$(this).animate({opacity:0.8},300);
	});*/

	/*send email*/
	$("#email-send").on("click",function(){

		//check Email
		var mail_addr = $.trim($("#input-email").val());
		if(!CheckEmail(mail_addr)){
			return false;
		}

		/*ajax*/
		$.ajax();
	});

	/*send information*/
	$("#infor-send").on("click",function(){

		//check empty
		if(!CheckEmpty("#name") || !CheckEmpty("#email") || !CheckEmpty("#msg")){
			return false;
		}

		//check Email
		var mail_addr = $.trim($("#email").val());
		if(!CheckEmail(mail_addr)){
			return false;
		}

		/*ajax*/
		$.ajax();
	});

	/*nav click*/
	$("#product a, #team>.bar a, #contact>.bar a, #right-photo>a.join-us").on("click",function(){
		var dir = $(this).attr("href");
		var top = $(dir).offset().top;
		$("html,body").animate({
			scrollTop:top
		},500,function(){});
		return false;
	});
});

/*shows toggle*/
function ToggleShow(){
	var holder = $("#show-hd");
	var shows = holder.children("li");
	var total = shows.length;
	var curShow = holder.children("li.show-cur").index();
	var nextShow = (curShow + 1) % total;
	$(shows[curShow]).fadeOut(800,function(){
		$(this).removeClass("show-cur");
	});
	$(shows[nextShow]).fadeIn(800,function(){
		$(this).addClass("show-cur");
	});
}

/*check email*/
function CheckEmail(mail_addr){
	var reg = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
	var r = reg.test(mail_addr);
	if(!r){
		alert("Invalid Email!");
		return false;
	}
	return true;
}

/*check empty*/
function CheckEmpty(box){
	var value = $.trim($(box).val());
	if(value == ""){
		alert("Please enter your " + $(box).attr("tip-data") + "...");
		return false;
	}
	return true;
}