using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Options;
using Microsoft.IdentityModel.Tokens;
using PhoneBook.Application.Settings;
using PhoneBook.Application.User.Queries;
using System;
using System.Globalization;
using System.Collections.Generic;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;
using System.Threading.Tasks;

namespace PhoneBook.Web.Controllers;

public class HomeController : Controller
{
    private readonly IUserService _userService;
    private readonly JwtSettings _jwtSettings;

    // از Dependency Injection استفاده می‌کنیم (در Program.cs این سرویس به DI اضافه شده است)
    public HomeController(IUserService userService, IOptions<JwtSettings> jwtOptions)
    {
        _userService = userService;
        _jwtSettings = jwtOptions.Value;
    }

    [HttpGet]
    public IActionResult Index(User user)
    {
        string remainingSeconds  = "نامشخص";

        if (User?.Identity?.IsAuthenticated == true)
        {
            ViewData["DisplayName"] = User?.FindFirst("DisplayName")?.Value ?? User?.Identity?.Name ?? "کاربر عزیز";

            var expClaim = User?.FindFirst(JwtRegisteredClaimNames.Exp)?.Value;
            if (!string.IsNullOrEmpty(expClaim) && long.TryParse(expClaim, out long expSeconds))
            {
                DateTime expDate = DateTimeOffset.FromUnixTimeSeconds(expSeconds).UtcDateTime;
                var remainingTime = expDate - DateTime.UtcNow;
                remainingSeconds = remainingTime.TotalSeconds.ToString("F0", CultureInfo.InvariantCulture);
            }

            int parsedSeconds = int.TryParse(remainingSeconds?.ToString(), out int result) ? result : 3600;
            ViewData["RemainingCookieTime"] = parsedSeconds > 3600 ? 3600 : parsedSeconds;

            return View(user);
        }

        return RedirectToAction("Login");
        
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
            // ایجاد توکن JWT
            var tokenHandler = new JwtSecurityTokenHandler();
            var key = Encoding.ASCII.GetBytes(_jwtSettings.SecretKey);

            if (key.Length == 0)
            {
                throw new InvalidOperationException("SecretKey مقداردهی نشده است.");
            }

            var claims = new List<Claim>
            {
                new Claim(ClaimTypes.Name, user.Username),
                new Claim("DisplayName", user.DisplayName),
                new Claim(JwtRegisteredClaimNames.Exp, 
                    DateTimeOffset.UtcNow.AddMinutes(_jwtSettings.ExpiresInMinutes).ToUnixTimeSeconds().ToString(), 
                    ClaimValueTypes.Integer)
            };
            
            var tokenDescriptor = new SecurityTokenDescriptor
            {
                Subject = new ClaimsIdentity(claims),
                Expires = DateTime.UtcNow.AddMinutes(_jwtSettings.ExpiresInMinutes),
                Issuer = _jwtSettings.Issuer,
                Audience = _jwtSettings.Audience,
                SigningCredentials = new SigningCredentials(new SymmetricSecurityKey(key), SecurityAlgorithms.HmacSha256Signature)
            };

            var token = tokenHandler.CreateToken(tokenDescriptor);
            var tokenString = tokenHandler.WriteToken(token);

            // قرار دادن توکن در یک کوکی HTTP-only
            Response.Cookies.Append("jwt", tokenString, new CookieOptions
            {
                HttpOnly = true,
                Secure = true, // در محیط تولید (production) مقدار true، در حالت توسعه ممکن است false باشد.
                SameSite = SameSiteMode.Strict,
                Expires = tokenDescriptor.Expires
            });

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
            // حالت ثبت‌نام ناموفق
            TempData["RegistrationSuccess"] = false;
            TempData["RegistrationMessage"] = "این نام کاربری قبلاً ثبت شده است.";

            return View();
        }
        else
        {
            try
            {
                await _userService.RegisterUserAsync(username, password, displayName);
                // حالت ثبت‌ نام موفق
                TempData["RegistrationSuccess"] = true;
                TempData["RegistrationMessage"] = "ثبت نام با موفقیت انجام شد.";
            }
            catch (Exception ex)
            {
                TempData["RegistrationSuccess"] = false;
                TempData["RegistrationMessage"] = "ثبت نام با خطا مواجه خطا شد!" + ex.Message;
            }
            
            // در اینجا می‌توانید همان ویو ثبت‌نام را رندر کنید.
            return RedirectToAction("Register");
        }

    }
    
    [HttpGet]
    public IActionResult Logout()
    {
        // حذف کوکی JWT
        Response.Cookies.Delete("jwt");

        return RedirectToAction("Login");
    }


}