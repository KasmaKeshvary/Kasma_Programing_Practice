using PhoneBook.Application.DTOs;

namespace PhoneBook.Application.Services
{
    public interface IUserService
    {
        Task<List<UserDto>> GetAllUsersAsync();
        Task<UserDto?> GetUserByUsernameAsync(string username);
        Task<UserDto?> GetUserByUsernameAndPasswordAsync(string username, string password);
        Task<UserDto> ValidateUserAsync(string username, string password);
        Task<bool> CheckUserExistsAsync(string username);
        Task RegisterUserAsync(string username, string password, string displayName);
    }
}