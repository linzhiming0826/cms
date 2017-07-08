
//检查参数
function checkParams() {
    var userName = $.trim($('#userName').val())
    if (userName == undefined || userName.length <= 0) {
        alert('用户名不能为空')
        return false
    }
    var password = $.trim($('#password').val())
    if (password == undefined || password.length <= 0) {
        alert('密码不允许为空')
        return false
    }
    return true
}
//清除内容
function clearContent() {
    $('#userName').val('');
    $('#password').val('');
    $('#msg').val('');
}
//登录方法
function login() {
    var check = checkParams()
    if (!check) return
    var userName = encodeURIComponent($.trim($('#userName').val()))
    var password = encodeURIComponent($.trim($('#password').val()))
    $.ajax({
        type: "post",
        dataType: 'json',
        url: "/signIn",
        data: { userName: userName, password: password, i: Math.random() },
        success: function (data) {
            if (data.code == 1) {
                self.location = '/';
            }
            else {
                $("#msg").html(data.msg)
                clearContent();
            }
        }
    });
}