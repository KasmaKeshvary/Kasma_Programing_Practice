using PhoneBook.Core.Entities;
using PhoneBook.Core.Interfaces;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace PhoneBook.Application.Contact.Queries
{
    public class SearchContactsQuery
    {
        private readonly IContactRepositoryRead _contactRepositoryRead;

        public SearchContactsQuery(IContactRepositoryRead contactRepositoryRead)
        {
            _contactRepositoryRead = contactRepositoryRead;
        }

        public async Task<List<PhoneBook.Core.Entities.Contact>> Execute(string searchQuery)
        {
            return await _contactRepositoryRead.SearchContactsAsync(searchQuery);
        }
    }

}
