using PhoneBook.Core.Entities;

namespace PhoneBook.Core.Interfaces.Repositories
{
     public interface IContactRepository
    {
        Task<Contact> AddAsync(Contact contact);
        Task<IEnumerable<Contact>> GetAllForUserAsync(int userId);
        Task<Contact> GetByIdAsync(int id, int userId);
        Task DeleteAsync(int id, int userId);
        Task<IEnumerable<Contact>> SearchAsync(int userId, string searchTerm);
    }
}
