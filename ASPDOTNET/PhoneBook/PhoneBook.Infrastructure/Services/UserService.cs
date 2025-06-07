using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.Data.SqlClient;
using Microsoft.Extensions.Options;
using PhoneBook.Core.Entities;
using PhoneBook.Core.Settings;

namespace PhoneBook.Infrastructure.Services
{
    public class UserService
    {
        private readonly string _connectionString;

        // دریافت رشته اتصال از طریق تنظیمات strongly typed که با IOptions تزریق می‌شود.
        public UserService(IOptions<DatabaseSettings> options) =>
            _connectionString = options.Value.DBString;

        public async Task<User?> ValidateUserAsync(string username, string password)
        {
            using var connection = new SqlConnection(_connectionString);
            await connection.OpenAsync();

            // انتخاب فقط ستون‌های مورد نیاز برای جلوگیری از تداخل با unboxing
            var query = "SELECT TOP 1 Id, Username, DisplayName, Password FROM Users WHERE Username = @username AND Password = @password";
            using var command = new SqlCommand(query, connection);
            command.Parameters.AddWithValue("@username", username);
            command.Parameters.AddWithValue("@password", password);

            using var reader = await command.ExecuteReaderAsync();
            if (await reader.ReadAsync())
            {
                // به دست آوردن اندیس ستون "Id"
                int idIndex = reader.GetOrdinal("Id");
                // استفاده از GetInt32 هنگام اطمینان از نال نبودن
                int userId = reader.GetInt32(idIndex);

                int usernameIndex = reader.GetOrdinal("Username");
                int displayNameIndex = reader.GetOrdinal("DisplayName");
                int passwordIndex = reader.GetOrdinal("Password");

                return new User
                {
                    Id = userId,
                    Username = reader.IsDBNull(usernameIndex) ? string.Empty : reader.GetString(usernameIndex),
                    DisplayName = reader.IsDBNull(displayNameIndex) ? string.Empty : reader.GetString(displayNameIndex),
                    Password = reader.IsDBNull(passwordIndex) ? string.Empty : reader.GetString(passwordIndex)
                };
            }
            return null;
        }

        // متد بررسی وجود کاربر با نام کاربری در پایگاه داده
        public async Task<bool> CheckUserExistsAsync(string username)
        {
            using var connection = new SqlConnection(_connectionString);
            await connection.OpenAsync();

            var query = "SELECT COUNT(*) FROM Users WHERE Username = @username";
            using var command = new SqlCommand(query, connection);
            command.Parameters.AddWithValue("@username", username);

            // دریافت نتیجه از ExecuteScalarAsync
            var result = await command.ExecuteScalarAsync();
            // چک کردن نتیجه برای DBNull و null قبل از تبدیل به int
            int count = (result != null && result != DBNull.Value)
                ? Convert.ToInt32(result)
                : 0;
            return count > 0;
        }

        // متد ثبت کاربر جدید در پایگاه داده
        public async Task RegisterUserAsync(string username, string password, string displayName)
        {
            using var connection = new SqlConnection(_connectionString);
            await connection.OpenAsync();

            var query = "INSERT INTO Users (Username, Password, DisplayName) VALUES (@username, @password, @displayName)";
            using var command = new SqlCommand(query, connection);
            command.Parameters.AddWithValue("@username", username);
            command.Parameters.AddWithValue("@password", password); // در محیط واقعی کلمه عبور را هش کنید!
            command.Parameters.AddWithValue("@displayName", displayName);

            await command.ExecuteNonQueryAsync();
        }
    }
}