using System.Collections.Generic;
using System.Threading.Tasks;
using PhoneBook.Core.Entities;

namespace PhoneBook.Core.Interfaces
{
    public interface IUserRepositoryRead
    {
        Task<List<User>> GetUsersAsync();
        Task<User?> GetUserByUsernameAsync(string username);
        Task<User?> GetUserByUsernameAndPasswordAsync(string username, string password);
    }
}