$(document).ready(function () {
    // رویداد کلیک منوهای اصلی در نوار کناری
    $(".menu-item").on("click", function () {
        // ذخیره محتوای اولیه mainSection هنگام لود صفحه
        var originalMainSection = $("#mainSection").html();

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
                // ابتدا محتوای اصلی mainSection (شامل defaultContent و searchSection) را بازیابی می‌کنیم
                $("#mainSection").html(`
                            <div id="searchSection" style="display: none;">
                                <!-- فیلد ورودی جستجو به صورت استاتیک -->
                                <input type="text" id="searchInput" placeholder="متن جستجو را وارد کنید..."
                                       style="width: 100%; padding: 8px; margin-bottom: 10px;" />
                                <!-- ناحیه نمایش نتایج جستجو -->
                                <div id="searchResults">
                                    <p>هیچ نتیجه‌ای برای نمایش موجود نیست.</p>
                                </div>
                            </div>`);
                
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
                $("#mainSection").html(`
                            <form action="/Contact/Add" method="post">
                                <input type="text" name="firstName" id="firstName" placeholder="نام" style="width: 10%; padding: 8px; margin-bottom: 10px;" required />
                                <input type="text" name="lastName" id="lastName" placeholder="نام خانوادگی" style="width: 10%; padding: 8px; margin-bottom: 10px;" required />
                                <input type="text" name="phoneNumber" id="phoneNumber" placeholder="شماره موبایل" style="width: 11%; padding: 8px; margin-bottom: 10px;" required />
                                <input type="text" name="address" id="address" placeholder="آدرس" style="width: 25%; padding: 8px; margin-bottom: 10px;" required />
                                <input type="text" name="email" id="email" placeholder="ایمیل" style="width: 15%; padding: 8px; margin-bottom: 10px;" required />
                                <button type="submit" id="contactSubmit">ثبت‌ اطلاعات تماس</button>
                            </form>`);
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

