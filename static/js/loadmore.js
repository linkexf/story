$(window).scroll(function(){
    loaddata();
});

function _loadmore(){
    var _xsrf = getCookie('_xsrf');
	var pageNum = $("#hiddenpage").val();
    var stime = $('#hiddentime').val();
    var cat = $('#hiddencategory').val();
    pageNum = parseInt(pageNum)+1;
    
    $.ajax({    
		type:'post',   
		url:'/indexloadmore', 
		data:{_xsrf:_xsrf,page:pageNum,cat:cat,stime:stime}, 
		async:true,
		success:function(data){
		    var json_data = $.parseJSON(data);
            $(".section_ul").append(json_data['html']);
            $('#hiddenpage').val(pageNum);
            
            if(json_data['isloadmore'] == '0'){
                $(".bottom_loading").text('囧，内容被看光啦！');
            } else {
                $(".bottom_loading").hide();
            }
		}
	});
}

function loaddata(){
    if($(".bottom_loading").css("display") == "none"){
	    totalheight = parseFloat($(document).height()) + parseFloat($(document).scrollTop());
        if ( $(document).height() <= totalheight) {
	        $(".bottom_loading").show();
            setTimeout(_loadmore,1000);
	    }
    }
}
