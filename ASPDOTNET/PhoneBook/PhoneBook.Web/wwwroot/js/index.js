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
                        <!-- ستون سمت راست (۸۰٪ عرض) -->
                        <div class="right-panel" id="mainSection">
                            <!-- بخش جستجو (به صورت پیش‌فرض مخفی) -->
                            <div id="searchSection" style="display: none;">
                                <!-- فیلد ورودی جستجو به صورت استاتیک -->
                                <input type="text" id="searchInput" placeholder="متن جستجو را وارد کنید..."
                                       style="width: 100%; padding: 8px; margin-bottom: 10px;" />
                                <!-- ناحیه نمایش نتایج جستجو -->
                                <div id="searchResults">
                                    <p>هیچ نتیجه‌ای برای نمایش موجود نیست.</p>
                                </div>
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

