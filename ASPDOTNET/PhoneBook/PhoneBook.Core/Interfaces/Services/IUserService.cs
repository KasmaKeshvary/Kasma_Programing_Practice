using PhoneBook.Core.Entities;

namespace PhoneBook.Core.Interfaces.Services
{
    public interface IUserService
    {
        Task<User> RegisterAsync(User user);
        Task<User> AuthenticateAsync(string username, string password);
        Task<bool> UsernameExistsAsync(string username);
    }
}
