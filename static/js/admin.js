(function($){
    var head_height=0;
    if($(".page_navbar").height()){
        head_height=62+$(".page_navbar").height()+1;
    }else{
        head_height=62;
    }
    $(".height-nonav").css("height", ($(window).height()-head_height) + "px");
    $(window).resize(function() {
        $(".height-nonav").css("height", ($(window).height()-head_height) + "px");
    });
    $(window).load(function(){
        $(".scroll-nonav").mCustomScrollbar({
            theme:"dark"
        });
    });
})(jQuery);