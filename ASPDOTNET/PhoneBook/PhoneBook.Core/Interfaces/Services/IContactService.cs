using PhoneBook.Core.Entities;

namespace PhoneBook.Core.Interfaces.Services
{
    public interface IContactService
    {
        Task<Contact> AddContactAsync(Contact contact);
        Task<IEnumerable<Contact>> GetContactsAsync(int userId);
        Task<Contact> GetContactAsync(int id, int userId);
        Task DeleteContactAsync(int id, int userId);
        Task<IEnumerable<Contact>> SearchContactsAsync(int userId, string searchTerm);
    }
}
