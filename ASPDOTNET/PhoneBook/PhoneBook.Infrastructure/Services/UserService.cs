using PhoneBook.Core.Entities;
using Microsoft.Data.SqlClient;
using System.Threading.Tasks;

namespace PhoneBook.Infrastructure.Services;

public class UserService
{
    private readonly string _connectionString = "Server=DESKTOP-VNKT76F;Database=PhoneBookDB;Integrated Security=true;TrustServerCertificate=true;";

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
}