// فایل registrationModal.js

// تابع نمایش modal
function showRegistrationModal() {
    var modal = document.getElementById("registrationModal");
    if (modal) {
        modal.style.display = "block";
        // پس از 5 ثانیه پیام modal بسته شود و کاربر به صفحه ورود هدایت گردد
        setTimeout(function () {
            modal.style.display = "none";
            window.location.href = "/Home/Login";  // تغییر مسیر به صفحه Login
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