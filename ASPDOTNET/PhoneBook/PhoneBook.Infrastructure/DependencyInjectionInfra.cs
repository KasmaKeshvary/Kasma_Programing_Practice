using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using PhoneBook.Infrastructure.Extensions;
using PhoneBook.Infrastructure.Repositories;
using PhoneBook.Infrastructure.Services;
using PhoneBook.Core.Interfaces;


namespace PhoneBook.Infrastructure
{
    public static class DependencyInjectionInfra
    {
        public static IServiceCollection AddInfrastructure(this IServiceCollection services, IConfiguration configuration)
        {
            services.ConfigureDatabase(configuration);
            services.AddScoped<IContactRepositoryRead, ContactRepositoryRead>();
            services.AddScoped<IContactRepositoryWrite, ContactRepositoryWrite>();
            services.AddScoped<IUserRepositoryRead, UserRepositoryRead>(); // ✅ فقط خواندن
            services.AddScoped<IUserRepositoryWrite, UserRepositoryWrite>(); // ✅ فقط نوشتن
            services.AddScoped<IUserService, UserService>(); // ✅ مدیریت منطق تجاری
            
            return services;
        }
    }
}