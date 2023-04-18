// Execute the following procedures only after the page has loaded
function  bindEmailCaptchaClick(){
    $("#captcha-btn").click(function (event) {
        var $this = $(this);
        //Block default events
        event.preventDefault();

        var email = $("input[name='email']").val();
        $.ajax({
            url: "/auth/captcha/email?email=" + email,
            method: "GET",
            success: function (result) {
                var code = result['code'];
                if (code == 200) {
                    var countdown = 60;
                    // Cancel the button click event before the countdown begins
                    $this.off("click")
                    var timer = setInterval(function () {
                        $this.text(countdown);
                        countdown -= 1;
                        if (countdown <= 0) {
                            clearInterval(timer);
                            $this.text("Get Captcha");
                            bindEmailCaptchaClick();
                        }
                    }, 1000);
                    alert("The captcha has been successfully sent to your email!!");
                } else {
                    alert(result['message']);
                }
            },
            fail: function (error) {
                console.log(error);
            }
        })
    });
}

$(function () {
    bindEmailCaptchaClick();
});
