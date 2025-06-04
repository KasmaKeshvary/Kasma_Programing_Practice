// using System.Text.Json;
// using Microsoft.AspNetCore.Mvc;
// using PhoneBook.Core.Entities;
// using PhoneBook.Infrastructure.Services;

// namespace PhoneBook.Web.Controllers;

// public class HomeController : Controller
// {

//     [HttpPost]
//     public IActionResult ProcessData([FromBody] JsonElement data)
//     {
//         // استخراج مقدار property "name" به روش JsonElement 
//         string? name = data.GetProperty("name").GetString();
//         string? surname = data.GetProperty("surname").GetString();

//         return Content($"سلام {name}{surname}! از سمت سرور دریافت شد.");
//     }

//     // می‌توانید از DI (Dependency Injection) برای دریافت نمونه سرویس استفاده کنید.
//     private readonly UserService _userService;

//     // در این مثال به صورت مستقیم از سازنده استفاده کرده‌ایم؛ در پروژه‌های بزرگ توصیه می‌شود
//     // سرویس‌ها در Startup/Program ثبت شوند.
//     public HomeController(UserService userService)
//     {
//         _userService = userService;
//     }

//     // اکشن Index داده‌های کاربر را دریافت کرده و به ویو ارسال می‌کند.
//     public async Task<IActionResult> Index()
//     {
//         User? user = await _userService.GetFirstUserAsync();
//         return View(user);
//     }
// }


using Microsoft.AspNetCore.Mvc;
using PhoneBook.Infrastructure.Services;
using PhoneBook.Core.Entities;

namespace PhoneBook.Web.Controllers;

public class HomeController : Controller
{
    private readonly UserService _userService;

    // از Dependency Injection استفاده می‌کنیم (در Program.cs این سرویس به DI اضافه شده است)
    public HomeController(UserService userService)
    {
        _userService = userService;
    }

    // نمایش فرم ورود
    [HttpGet]
    public IActionResult Login()
    {
        return View();
    }

    // دریافت داده‌های فرم و بررسی ورود
    [HttpPost]
    public async Task<IActionResult> Login(string username, string password)
    {
        var user = await _userService.ValidateUserAsync(username, password);
        if (user != null)
        {
            // در اینجا می‌توانید عملیات احراز هویت و ایجاد کوکی را نیز انجام دهید
            return Content($"خوش آمدید، {user.DisplayName}!");
        }
        else
        {
            return Content("کاربری با این مشخصات وجود ندارد.");
        }
    }
}