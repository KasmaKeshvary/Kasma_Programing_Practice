using PhoneBook.Infrastructure.Services;
using PhoneBook.Infrastructure.Repositories;
using PhoneBook.Infrastructure.Data;
using Microsoft.AspNetCore.Authentication.Cookies;
using Microsoft.EntityFrameworkCore;
using PhoneBook.Core.Interfaces;


var builder = WebApplication.CreateBuilder(args);

// خواندن Connection String از بخش ConnectionStrings در appsettings.json
var connectionString = builder.Configuration.GetConnectionString("DefaultConnection");

// ثبت DbContext برای استفاده از EF Code First
builder.Services.AddDbContext<PhoneBookContext>(options =>
    options.UseSqlServer(connectionString)
);

// افزودن سرویس‌های مورد نیاز برای MVC
builder.Services.AddControllersWithViews();
// ثبت سرویس‌ها با استفاده از interface
builder.Services.AddScoped<IUserService, UserService>();
builder.Services.AddScoped<IContactRepository, ContactRepository>();

//افزودن سرویس Session به DI با مدت زمان یک روز (24 ساعت)
builder.Services.AddSession(options =>
{
    // این مقدار نشانگر انقضای سشن پس از عدم فعالیت است
    options.IdleTimeout = TimeSpan.FromDays(1);
    options.Cookie.HttpOnly = true;
    options.Cookie.IsEssential = true;
});

// // افزودن سرویس احراز هویت با استفاده از کوکی
// builder.Services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme).AddCookie(options =>
// {
//     options.ExpireTimeSpan = TimeSpan.FromDays(1); // مدت اعتبار یک روز
//     options.LoginPath = "/Home/Login"; // مسیر ورود
// });


var app = builder.Build();

app.UseStaticFiles();
app.UseRouting();

// فعال‌سازی Session قبل از Middleware های دیگر که به سشن نیاز دارند
app.UseSession();


// // فعال‌سازی احراز هویت و مجوز دسترسی
// app.UseAuthentication();
// app.UseAuthorization();


app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Login}/{id?}");


app.Run();
