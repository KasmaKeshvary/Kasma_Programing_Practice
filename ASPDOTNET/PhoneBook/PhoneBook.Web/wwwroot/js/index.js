// فایل index.js

$(document).ready(function () {
    $(".menu-item").on("click", function () {
        var id = $(this).attr("id");
        var content;

        switch (id) {
            case "displayList":
                // فراخوانی AJAX جهت دریافت PartialView لیست مخاطبین
                $.ajax({
                    url: '/Contact/List',
                    type: 'GET',
                    success: function (result) {
                        $("#mainSection").html(result);
                    },
                    error: function () {
                        $("#mainSection").html("<p>خطا در بارگذاری لیست مخاطبین.</p>");
                    }
                });
                break;
            case "search":
                content = "<h2>جست و جو</h2><p>در این بخش امکان جستجو در بین افراد موجود است.</p>";
                break;
            case "addPerson":
                content = "<h2>اضافه کردن نفر</h2><p>در این بخش می‌توانید نفر جدیدی به سیستم اضافه کنید.</p>";
                break;
            case "logout":
                // هدایت کاربر به صفحه ورود پس از کلیک روی دکمه خروج
                window.location.href = "/Home/Login";
                return; // خروج از تابع پس از تغییر مسیر
            default:
                content = "<p>لطفاً یک گزینه انتخاب کنید.</p>";
                break;
        }
        $("#mainSection").html(content);
    });
});

// $(document).ready(function () {
//     $(".menu-item").on("click", function () {
//         var id = $(this).attr("id");
//         var content;

//         // بررسی حالت‌های مختلف منو
//         switch (id) {
//             case "displayList":
//                 // فراخوانی AJAX جهت دریافت PartialView لیست مخاطبین
//                 $.ajax({
//                     url: '/Contact/List',
//                     type: 'GET',
//                     success: function (result) {
//                         $("#mainSection").html(result);
//                     },
//                     error: function () {
//                         $("#mainSection").html("<p>خطا در بارگذاری لیست مخاطبین.</p>");
//                     }
//                 });
//                 break;
//             case "search":
//                 content = "<h2>جست و جو</h2><p>در این بخش امکان جستجو در بین افراد وجود دارد.</p>";
//                 $("#mainSection").html(content);
//                 break;
//             case "addPerson":
//                 content = "<h2>اضافه کردن نفر</h2><p>این بخش برای افزودن مخاطب جدید می‌باشد.</p>";
//                 $("#mainSection").html(content);
//                 break;
//             case "logout":
//                 // ریدایرکت کردن به صفحه Login (یا فراخوانی اکشن Logout در صورت تعریف شده)
//                 window.location.href = "/Home/Login";
//                 break;
//             default:
//                 content = "<p>لطفاً یک گزینه انتخاب کنید.</p>";
//                 $("#mainSection").html(content);
//                 break;
//         }
//     });
// });