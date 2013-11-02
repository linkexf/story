$('.timeselcss').bind('click',function(){
    var _xsrf = getCookie('_xsrf');
    var dt = $(this).attr('data-action');
    var category = $('#hiddencategory').val();
    window.location = "/"+category+"/"+dt;
});


$('.categoryselcss').bind('click',function(){
    var _xsrf = getCookie('_xsrf');
    var dt = $(this).attr('data-action');
    var stime = $('#hiddentime').val();
    window.location = "/"+dt+"/"+stime;
});

function categorychange(){
    var _xsrf = getCookie('_xsrf');
    var cat = $('#categorychangesel').val();
    var stime = $('#hiddentime').val();
    window.location = "/"+cat+"/"+stime;
}

function timechange(){
    var _xsrf = getCookie('_xsrf');
    var stime = $('#timechangesel').val();
    var cat = $('#hiddencategory').val();
    window.location = "/"+cat+"/"+stime;
}
