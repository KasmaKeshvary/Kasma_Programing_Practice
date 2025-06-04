using PhoneBook.Infrastructure.Services;

var builder = WebApplication.CreateBuilder(args);

// افزودن سرویس‌های مورد نیاز برای MVC
builder.Services.AddControllersWithViews();
builder.Services.AddScoped<UserService>();

var app = builder.Build();

app.UseStaticFiles();
app.UseRouting();
app.UseEndpoints(endpoints =>
{
    endpoints.MapControllerRoute(
        name: "default",
        pattern: "{controller=Home}/{action=Login}/{id?}");
});


app.Run();
