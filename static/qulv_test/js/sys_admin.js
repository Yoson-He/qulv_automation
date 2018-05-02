/*----- 登录-----*/

function login()
{
   var user_name=document.getElementById("user_name").value;
   var password=document.getElementById("password").value;
   if (user_name == "") {
       $("#user_name").val(user_name);
       alert('请输入账号')
       return  false
   }
   else if(password == ""){
       alert('请输入密码')
       return  false;
   } else{
   var md5 = hex_md5(password);
   var sha1 = hex_sha1(password);
   $("#password").val(md5+sha1);
   var password=document.getElementById("password").value;
        $.ajax({
                cache: true,
                type: "POST",
                url:"/",
                data:{'user_name':user_name,'password':password},
                async: false,
                success: function(data) {
                    $("#commonLayout_appcreshi").parent().html(data);
                }
            });
    }

   window.location.reload()

}





/*----- 登出 -----*/

function logout()
{
    layer.confirm('确认要退出系统？',{ title: "Test-BMS" },function(index){
                $.ajax({
                        type:"post",
                        url:"/logout/",
                        data: {},
                        success: function (res){
                           window.location.reload()
                        },
                        error: function (jqXHR){
                            parent.layer.alert(jqXHR.responseText);
                        }
                 });
    });

}


/*弹出层*/
/*
    参数解释：
    title   标题
    url     请求的url
    id      需要操作的数据id
    w       弹出层宽度（缺省调默认值）
    h       弹出层高度（缺省调默认值）
*/
function show(title,url,w,h){
    if (title == null || title == '') {
        title=false;
    };
    if (url == null || url == '') {
        url="404.html";
    };
    if (w == null || w == '') {
        w=($(window).width()*0.9);
    };
    if (h == null || h == '') {
        h=($(window).height() - 50);
    };
    layer.open({
        type: 2,
        area:[w,h],
        fix: false, //不固定
        maxmin: true,
        shadeClose: true,
        shade:0.4,
        title: title,
        content: url,
    });
}
