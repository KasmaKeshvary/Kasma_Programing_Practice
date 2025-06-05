using System;
using System.Collections.Generic;
using PhoneBook.Core.Entities;
using Microsoft.Data.SqlClient;
using System.Threading.Tasks;
using Microsoft.Extensions.Options;
using PhoneBook.Core.Settings;

namespace PhoneBook.Infrastructure.Services;

public class UserService
{
    private readonly string _connectionString;

    // دریافت رشته اتصال از طریق تنظیمات strongly typed که با IOptions تزریق می‌شود.
    public UserService(IOptions<DatabaseSettings> options)
    {
        _connectionString = options.Value.DBString;
    }

    public async Task<User?> ValidateUserAsync(string username, string password)
    {
        using var connection = new SqlConnection(_connectionString);
        await connection.OpenAsync();

        var query = "SELECT TOP 1 * FROM Users WHERE Username = @username AND Password = @password";
        using var command = new SqlCommand(query, connection);
        command.Parameters.AddWithValue("@username", username);
        command.Parameters.AddWithValue("@password", password);

        using var reader = await command.ExecuteReaderAsync();
        if (await reader.ReadAsync())
        {
            return new User
            {
                Id = Convert.ToInt32(reader["Id"]),
                Username = reader["Username"].ToString() ?? string.Empty,
                DisplayName = reader["DisplayName"].ToString() ?? string.Empty,
                Password = reader["Password"].ToString() ?? string.Empty
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
        int count = (int)await command.ExecuteScalarAsync();
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