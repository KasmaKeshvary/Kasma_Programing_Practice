using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using PhoneBook.Core.Interfaces;
using PhoneBook.Infrastructure.Data;
using PhoneBook.Infrastructure.Repositories;
using PhoneBook.Application.Services;

namespace PhoneBook.Infrastructure
{
    public static class DependencyInjectionInfra
    {
        public static IServiceCollection AddInfrastructure(
            this IServiceCollection services,
            IConfiguration configuration)      // ← IConfiguration را اضافه کردیم
        {
            // ۱) خواندن کانکشن استرینگ از فایل appsettings.json پروژه Web
            var connStr = configuration
                          .GetConnectionString("DefaultConnection")
                      ?? throw new InvalidOperationException(
                          "ConnectionStrings:DefaultConnection یافت نشد.");

            // ۲) کانفیگ DbContext با آن
            services.AddDbContext<ReadDbContext>(opt =>
                opt.UseSqlServer(connStr));
            services.AddDbContext<WriteDbContext>(opt =>
                opt.UseSqlServer(connStr));

            // ۳) ثبت Repositoryها
            services.AddScoped<IUserRepositoryRead, UserRepositoryRead>();
            services.AddScoped<IUserRepositoryWrite, UserRepositoryWrite>();
            services.AddScoped<IContactRepositoryRead, ContactRepositoryRead>();
            services.AddScoped<IContactRepositoryWrite, ContactRepositoryWrite>();

            // ۴) ثبت Serviceهای Infrastructure (پیاده‌سازی IUserService و IContactService)
            services.AddScoped<IUserService, UserService>();
            services.AddScoped<IContactService, ContactService>();

            return services;
        }
    }
}