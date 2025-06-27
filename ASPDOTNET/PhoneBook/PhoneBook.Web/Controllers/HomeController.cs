using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Options;
using Microsoft.IdentityModel.Tokens;
using PhoneBook.Application.Settings;
using PhoneBook.Application.DTOs;
using PhoneBook.Application.User.Queries;
using PhoneBook.Application.User.Commands;
using System.Globalization;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;
using MediatR;

namespace PhoneBook.Web.Controllers
{
    public class HomeController : Controller
    {
        private readonly IMediator _mediator;
        private readonly JwtSettings _jwtSettings;

        public HomeController(IMediator mediator, IOptions<JwtSettings> jwtOptions)
        {
            _mediator = mediator;
            _jwtSettings = jwtOptions.Value;
        }

        [HttpGet]
        public IActionResult Index(UserDto? user)
        {
            string remainingSeconds = "نامشخص";

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

        [HttpGet]
        public IActionResult Login() => View();

        [HttpPost]
        public async Task<IActionResult> Login(string username, string password)
        {
            var user = await _mediator.Send(new ValidateUserCommand(username, password));
            if (user != null)
            {
                var tokenHandler = new JwtSecurityTokenHandler();
                var key = Encoding.ASCII.GetBytes(_jwtSettings.SecretKey);

                var claims = new[]
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
                    SigningCredentials = new SigningCredentials(
                        new SymmetricSecurityKey(key),
                        SecurityAlgorithms.HmacSha256Signature)
                };

                var token = tokenHandler.CreateToken(tokenDescriptor);
                var tokenString = tokenHandler.WriteToken(token);

                Response.Cookies.Append("jwt", tokenString, new CookieOptions
                {
                    HttpOnly = true,
                    Secure = true,
                    SameSite = SameSiteMode.Strict,
                    Expires = tokenDescriptor.Expires
                });

                return RedirectToAction("Index", user);
            }

            ViewBag.Error = "کاربری با این مشخصات وجود ندارد.";
            return View();
        }

        [HttpGet]
        public IActionResult Register() => View();

        [HttpPost]
        public async Task<IActionResult> Register(string username, string password, string displayName)
        {
            bool exists = await _mediator.Send(new CheckUserExistsQuery(username));
            if (exists)
            {
                TempData["RegistrationSuccess"] = false;
                TempData["RegistrationMessage"] = "این نام کاربری قبلاً ثبت شده است.";
                return View();
            }

            try
            {
                await _mediator.Send(new RegisterUserCommand(username, password, displayName));

                TempData["RegistrationSuccess"] = true;
                TempData["RegistrationMessage"] = "ثبت نام با موفقیت انجام شد.";
            }
            catch (Exception ex)
            {
                TempData["RegistrationSuccess"] = false;
                TempData["RegistrationMessage"] = $"خطا در ثبت‌نام: {ex.Message}";
            }

            return RedirectToAction("Register");
        }

        [HttpGet]
        public IActionResult Logout()
        {
            Response.Cookies.Delete("jwt");
            return RedirectToAction("Login");
        }
    }
}