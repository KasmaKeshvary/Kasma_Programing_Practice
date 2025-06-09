using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.EntityFrameworkCore;
using Microsoft.IdentityModel.Tokens;
using PhoneBook.Core.Interfaces;
using PhoneBook.Core.Setting;
using PhoneBook.Infrastructure.Data;
using PhoneBook.Infrastructure.Repositories;
using PhoneBook.Infrastructure.Services;
using System.Text;

var builder = WebApplication.CreateBuilder(args);

// خواندن تنظیمات JWT از appsettings.json و مقداردهی `JwtSettings`
builder.Services.Configure<JwtSettings>(builder.Configuration.GetSection("JwtSettings"));

var jwtSettingsSection = builder.Configuration.GetSection("JwtSettings");
var secretKey = jwtSettingsSection["SecretKey"];

if (string.IsNullOrEmpty(secretKey))
{
    throw new InvalidOperationException("SecretKey برای JWT مقداردهی نشده است.");
}

var key = Encoding.ASCII.GetBytes(secretKey);


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

builder.Services.AddAuthentication(options =>
{
    Console.WriteLine("Executing AddAuthentication ..."); // 🔹 بررسی اینکه تنظیمات JWT اجرا می‌شود.
    options.DefaultAuthenticateScheme = JwtBearerDefaults.AuthenticationScheme;
    options.DefaultChallengeScheme = JwtBearerDefaults.AuthenticationScheme;
})
.AddJwtBearer(options =>
{
    // خواندن توکن از کوکی (به جای header)
    options.Events = new JwtBearerEvents
    {
        OnMessageReceived = context =>
        {
            var token = context.Request.Cookies["jwt"];
            
            if (!string.IsNullOrEmpty(token))
            {
                context.Token = token;
            }
            return Task.CompletedTask;
        }
    };
    options.TokenValidationParameters = new TokenValidationParameters
    {
        ValidateIssuerSigningKey = true,
        IssuerSigningKey = new SymmetricSecurityKey(key),
        ValidateIssuer = true,
        ValidIssuer = jwtSettingsSection["Issuer"],
        ValidateAudience = true,
        ValidAudience = jwtSettingsSection["Audience"],
        ValidateLifetime = true,
        ClockSkew = TimeSpan.Zero
    };
});

var app = builder.Build();

app.UseStaticFiles();
app.UseRouting();

// فعال‌سازی احراز هویت و مجوز دسترسی
app.UseAuthentication();
app.UseAuthorization();

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}",
    defaults: new { controller = "Home", action = "Index" }
);

app.Run();
