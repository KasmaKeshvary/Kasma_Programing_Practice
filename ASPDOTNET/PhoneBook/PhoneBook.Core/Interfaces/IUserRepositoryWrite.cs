using System.Threading.Tasks;
using PhoneBook.Core.Entities;

namespace PhoneBook.Core.Interfaces
{
    public interface IUserRepositoryWrite
    {
        Task AddUserAsync(string username, string password, string displayName);
    }
}