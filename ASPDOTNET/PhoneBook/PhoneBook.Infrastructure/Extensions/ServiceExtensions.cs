using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using PhoneBook.Infrastructure.Data;
using PhoneBook.Application.Settings;

namespace PhoneBook.Infrastructure.Extensions
{
    public static class ServiceExtensions
    {
        public static void ConfigureDatabase(this IServiceCollection services, IConfiguration configuration)
        {
            services.AddDbContext<ReadDbContext>(options =>
                options.UseSqlServer(configuration.GetConnectionString("PhonebookDB_Read")));

            services.AddDbContext<WriteDbContext>(options =>
                options.UseSqlServer(configuration.GetConnectionString("PhonebookDB_Write")));
        }

        public static void ConfigureJwtSettings(this IServiceCollection services, IConfiguration configuration)
        {
            JwtSettings jwtSettings = new();
            configuration.GetSection("JwtSettings").Bind(jwtSettings);
            services.AddSingleton(jwtSettings);
        }
    }
}