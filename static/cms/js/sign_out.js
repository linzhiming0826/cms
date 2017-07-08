
//退出登录
function signOut() {
    $.ajax({
        type: "get",
        url: "/signOut",
        success: function (data) {
            if (data.code == 1) {
                location.href = '/login'
            }
        }
    });
}