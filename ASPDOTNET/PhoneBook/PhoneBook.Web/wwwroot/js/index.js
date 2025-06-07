$(document).ready(function () {
    // رویداد کلیک منوهای اصلی در نوار کناری
    $(".menu-item").on("click", function () {
        var id = $(this).attr("id");

        switch (id) {
            case "displayList":
                // دریافت لیست کامل مخاطبین
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
                // زمانی که روی منوی جستجو کلیک می‌شود:
                // - بخش defaultContent را پنهان می‌کنیم.
                // - بخش searchSection را نمایش می‌دهیم.
                $("#defaultContent").hide();
                $("#searchSection").show();
                
                // فراخوانی اولیه اکشن Search با query تهی برای نمایش PartialView جستجو
                $.ajax({
                    url: '/Contact/Search',
                    type: 'GET',
                    data: { query: "" },
                    success: function (result) {
                        $("#searchResults").html(result);
                    },
                    error: function () {
                        $("#searchResults").html("<p>خطا در بارگذاری بخش جستجو.</p>");
                    }
                });
                break;

            case "addPerson":
                // در اینجا می‌توانید کد مربوط به بخش افزودن مخاطب را قرار دهید
                $("#mainSection").html("<h2>اضافه کردن نفر</h2><p>فرم اضافه کردن مخاطب در اینجا قرار می‌گیرد.</p>");
                break;

            case "logout":
                window.location.href = "/Home/Login"; // هدایت به صفحه ورود
                break;

            default:
                $("#mainSection").html("<p>لطفاً یک گزینه انتخاب کنید.</p>");
                break;
        }
    });

    // رویداد keyup برای فیلد جستجو داخل PartialView
    // از event delegation برای المانی که به صورت داینامیک به #mainSection اضافه می‌شود استفاده می‌کنیم.
    $("#mainSection").on("keyup", "#searchInput", function () {
        var query = $(this).val();

        // استفاده از debounce برای جلوگیری از ارسال درخواست‌های مکرر
        clearTimeout(window.searchDebounceTimeout);
        window.searchDebounceTimeout = setTimeout(function () {
            $.ajax({
                url: '/Contact/Search',
                type: 'GET',
                data: { query: query },
                success: function (result) {
                    // نتایج جستجو را در container مخصوص (با شناسه searchResults) درج می‌کنیم.
                    $("#searchResults").html(result);
                },
                error: function () {
                    $("#searchResults").html("<p>خطا در جستجو.</p>");
                }
            });
        }, 300);
    });
});

