using System.Threading.Tasks;
using PhoneBook.Core.Entities;

namespace PhoneBook.Core.Interfaces
{
    public interface IUserService
    {
        Task<User?> ValidateUserAsync(string username, string password);
        Task<bool> CheckUserExistsAsync(string username);
        Task RegisterUserAsync(string username, string password, string displayName);
    }
}