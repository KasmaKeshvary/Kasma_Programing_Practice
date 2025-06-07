using System.Collections.Generic;
using System.Threading.Tasks;
using PhoneBook.Core.Entities;

namespace PhoneBook.Core.Interfaces
{
    public interface IContactRepository
    {
        Task<List<Contact>> GetContactsAsync();
        Task<List<Contact>> SearchContactsAsync(string searchQuery);
    }
}