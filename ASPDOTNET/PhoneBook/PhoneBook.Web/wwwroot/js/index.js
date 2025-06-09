document.addEventListener("DOMContentLoaded", function () {
    // رویداد کلیک برای منوهای اصلی در نوار کناری
    document.querySelectorAll(".menu-item").forEach(item => {
        item.addEventListener("click", function () {
            const mainSection = document.getElementById("mainSection");
            const id = this.id;

            switch (id) {
                case "displayList":
                    fetch('/Contact/List')
                        .then(response => response.text())
                        .then(result => mainSection.innerHTML = result)
                        .catch(() => mainSection.innerHTML = "<p>خطا در بارگذاری لیست مخاطبین.</p>");
                    break;

                case "search":
                    mainSection.innerHTML = `
                        <div id="searchSection" style="display: none;">
                            <input type="text" id="searchInput" placeholder="متن جستجو را وارد کنید..."
                                   style="width: 100%; padding: 8px; margin-bottom: 10px;" />
                            <div id="searchResults">
                                <p>هیچ نتیجه‌ای برای نمایش موجود نیست.</p>
                            </div>
                        </div>`;
                    
                    document.getElementById("searchSection").style.display = "block";

                    fetch('/Contact/Search?query=')
                        .then(response => response.text())
                        .then(result => document.getElementById("searchResults").innerHTML = result)
                        .catch(() => document.getElementById("searchResults").innerHTML = "<p>خطا در بارگذاری بخش جستجو.</p>");
                    break;

                case "addPerson":
                    mainSection.innerHTML = `
                        <form action="/Contact/Add" method="post">
                            <input type="text" name="firstName" id="firstName" placeholder="نام" required />
                            <input type="text" name="lastName" id="lastName" placeholder="نام خانوادگی" required />
                            <input type="text" name="phoneNumber" id="phoneNumber" placeholder="شماره موبایل" required />
                            <input type="text" name="address" id="address" placeholder="آدرس" required />
                            <input type="text" name="email" id="email" placeholder="ایمیل" required />
                            <button type="submit" id="contactSubmit">ثبت‌ اطلاعات تماس</button>
                        </form>`;
                    break;

                case "logout":
                    fetch("/Home/Logout", { method: "GET" })
                        .then(response => {
                            if (response.redirected) {
                                localStorage.removeItem("visitCount");
                                window.location.href = response.url;
                            }
                        });
                    break;

                default:
                    mainSection.innerHTML = "<p>لطفاً یک گزینه انتخاب کنید.</p>";
                    break;
            }
        });
    });

    // رویداد keyup برای فیلد جستجو
    document.getElementById("mainSection").addEventListener("keyup", function (event) {
        if (event.target.id === "searchInput") {
            clearTimeout(window.searchDebounceTimeout);
            window.searchDebounceTimeout = setTimeout(() => {
                fetch(`/Contact/Search?query=${event.target.value}`)
                    .then(response => response.text())
                    .then(result => document.getElementById("searchResults").innerHTML = result)
                    .catch(() => document.getElementById("searchResults").innerHTML = "<p>خطا در جستجو.</p>");
            }, 300);
        }
    });

    let remainingTime = document.getElementById("remainingTime").innerHTML;
    
    function updateTokenTime() {
        if (remainingTime > 0) {
            remainingTime--;

            let minutes = Math.floor(remainingTime / 60); // محاسبه دقیقه
            let seconds = remainingTime % 60; // محاسبه ثانیه

            document.getElementById("remainingTime").innerText = `${minutes} دقیقه و ${seconds} ثانیه`;
        } else {
            document.getElementById("remainingTime").innerText = "منقضی شد!";
        }
    }

    setInterval(updateTokenTime, 1000); // هر ۱ ثانیه مقدار را کاهش بده

    // شمارش ورود مجدد به سایت
    // let visitCount = localStorage.getItem("visitCount");
    let visitCount = 1;

    if (!sessionStorage.getItem("sessionActive")) {
        console.log("session");
        visitCount = visitCount ? parseInt(visitCount ?? 1, 10) + 1 : 1;
        localStorage.setItem("visitCount", visitCount);
    }

    sessionStorage.setItem("sessionActive", "true");
    document.getElementById("visitCounter").innerText = `${visitCount}`;
});