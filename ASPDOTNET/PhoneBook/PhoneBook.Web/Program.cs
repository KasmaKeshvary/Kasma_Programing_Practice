using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.IdentityModel.Tokens;
using PhoneBook.Application;
using PhoneBook.Infrastructure;
using System.Text;
using PhoneBook.Application.Settings;

var builder = WebApplication.CreateBuilder(args);

// تنظیمات JWT
builder.Services.Configure<JwtSettings>(builder.Configuration.GetSection("JwtSettings"));
var jwtSettingsSection = builder.Configuration.GetSection("JwtSettings");
var secretKey = jwtSettingsSection["SecretKey"];
if (string.IsNullOrEmpty(secretKey))
{
    throw new InvalidOperationException("SecretKey برای JWT مقداردهی نشده است.");
}
var key = Encoding.ASCII.GetBytes(secretKey);

// ثبت سرویس‌های مورد نیاز
builder.Services.AddControllersWithViews();

// builder.Services.AddApplication();

builder.Services
   .AddInfrastructure(builder.Configuration)   // اول repo/DbContext/Serviceهای infra
   .AddApplication();                     // بعد mediator/mapper/validator و serviceهای app

// تنظیمات JWT Authentication
builder.Services.AddAuthentication(options =>
{
    options.DefaultAuthenticateScheme = JwtBearerDefaults.AuthenticationScheme;
    options.DefaultChallengeScheme = JwtBearerDefaults.AuthenticationScheme;
})
.AddJwtBearer(options =>
{
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
app.UseAuthentication();
app.UseAuthorization();
app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}",
    defaults: new { controller = "Home", action = "Index" }
);

app.Run();