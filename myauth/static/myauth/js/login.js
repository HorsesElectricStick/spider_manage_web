function keyLogin() {
    if (event.keyCode == 13){
        login.click()
    }
}

function form_check() {
    if (document.getElementsByName("用户名")[0].value.length==0){
        alert('用户名不能为空');
    } else if (document.getElementsByName("密码")[0].value.length==0){
        alert('密码不能为空');
    } else if (document.getElementsByName("验证码")[0].value.length==0){
        alert('验证码不能为空');
    } else {
        document.login_form.submit();
    }
}

