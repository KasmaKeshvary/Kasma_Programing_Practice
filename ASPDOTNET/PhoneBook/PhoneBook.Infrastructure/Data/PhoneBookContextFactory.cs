using System;
using System.IO;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;
using Microsoft.Extensions.Configuration;

namespace PhoneBook.Infrastructure.Data
{
    public class PhoneBookContextFactory : IDesignTimeDbContextFactory<PhoneBookContext>
    {
        public PhoneBookContext CreateDbContext(string[] args)
        {
            // تعیین مسیر پایه برای پیکربندی؛ معمولاً مسیر جاری پروژه است.
            var basePath = Directory.GetCurrentDirectory();

            // خواندن پیکربندی از فایل appsettings.json
            IConfigurationRoot configuration = new ConfigurationBuilder()
                .SetBasePath(basePath)
                .AddJsonFile("appsettings.json", optional: false, reloadOnChange: true)
                .Build();

            // استخراج رشته اتصال از بخش ConnectionStrings
            var connectionString = configuration.GetConnectionString("DefaultConnection");

            var optionsBuilder = new DbContextOptionsBuilder<PhoneBookContext>();
            optionsBuilder.UseSqlServer(connectionString);

            return new PhoneBookContext(optionsBuilder.Options);
        }
    }
}