// فایل registrationModal.js

// تابع نمایش modal
function showRegistrationModal(title, message, bgColor) {
    var modal = document.getElementById("registrationModal");
    var registerBtn = document.getElementById("registerSubmit");

    if (modal) {
        // تنظیم عنوان و پیام modal
        modal.querySelector("h2").innerText = title;
        modal.querySelector("p").innerText = message;
        // تنظیم رنگ پس‌زمینه بخش محتوا
        modal.querySelector(".modal-content").style.backgroundColor = bgColor;
        // نمایش modal
        modal.style.display = "block";
        // پس از 5 ثانیه modal بسته شود و کاربر به صفحه ورود هدایت گردد
        setTimeout(function () {
            modal.style.display = "none";
            if (registerBtn) {
                registerBtn.addEventListener("click", function (e) {
                    window.location.href = "/Home/Login";
                });
            }
        }, 5000);
    }
}

// تنظیم رویداد بستن modal از طریق دکمه close
document.addEventListener("DOMContentLoaded", function () {
    var closeBtn = document.querySelector("#registrationModal .close");
    if(closeBtn) {
        closeBtn.onclick = function() {
            var modal = document.getElementById("registrationModal");
            if (modal) {
                modal.style.display = "none";
            }
        };
    }
});
