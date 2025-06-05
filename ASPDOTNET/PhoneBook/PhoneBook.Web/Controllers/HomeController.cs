using Microsoft.AspNetCore.Mvc;
using PhoneBook.Infrastructure.Services;
using PhoneBook.Core.Entities;
using System.Threading.Tasks;

namespace PhoneBook.Web.Controllers;

public class HomeController : Controller
{
    private readonly UserService _userService;

    // از Dependency Injection استفاده می‌کنیم (در Program.cs این سرویس به DI اضافه شده است)
    public HomeController(UserService userService)
    {
        _userService = userService;
    }

    [HttpGet]
    public IActionResult Index(User user)
    {
        return View(user);
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
            // ثبت شناسه کاربر در Session
            HttpContext.Session.SetString("IsAuthenticated", "true");
            HttpContext.Session.SetString("DisplayName", user.DisplayName);

            // استفاده از کوکی
            // var claims = new List<Claim>
            // {
            //     new Claim(ClaimTypes.Name, user.DisplayName),
            //     new Claim(ClaimTypes.Role, user.Username.ToLower() == "admin" ? "Admin" : "User")
            // };

            // var claimsIdentity = new ClaimsIdentity(claims, CookieAuthenticationDefaults.AuthenticationScheme);
            // var authProperties = new AuthenticationProperties
            // {
            //     // مدت تایید، یعنی کوکی پس از 1 روز منقضی خواهد شد
            //     ExpiresUtc = DateTimeOffset.UtcNow.AddDays(1),
            //     IsPersistent = true
            // };

            // await HttpContext.SignInAsync(
            // CookieAuthenticationDefaults.AuthenticationScheme,
            // new ClaimsPrincipal(claimsIdentity),
            // authProperties);

            // در صورتی که از مدل استفاده می‌کنید:
            return RedirectToAction("Index", user);
        }
        else
        {
            // ارسال پیغام خطا به ویو ورود؛ می‌توانید این مورد را به ViewBag ارسال کنید
            ViewBag.Error = "کاربری با این مشخصات وجود ندارد.";
            return View(); // بازگردانی همان ویو Login با پیام خطا
        }
    }

    // نمایش فرم ثبت‌نام (GET)
    [HttpGet]
    public IActionResult Register()
    {
        return View();
    }

    // پردازش ثبت‌نام (POST)
    [HttpPost]
    public async Task<IActionResult> Register(string username, string password, string displayName)
    {
        bool exists = await _userService.CheckUserExistsAsync(username);
        if (exists)
        {
            ViewBag.Error = "این نام کاربری قبلاً ثبت شده است.";
            return View();
        }
        else
        {
            await _userService.RegisterUserAsync(username, password, displayName);
            TempData["RegistrationSuccess"] = true;
            // در اینجا می‌توانید همان ویو ثبت‌نام را رندر کنید.
            return RedirectToAction("Register");
        }

    }
    
    [HttpGet]
    public IActionResult Logout()
    {
        HttpContext.Session.Clear();
        // await HttpContext.SignOutAsync(CookieAuthenticationDefaults.AuthenticationScheme);

        return RedirectToAction("Login");
    }


}