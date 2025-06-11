using PhoneBook.Core.Entities;
using PhoneBook.Core.Interfaces;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace PhoneBook.Application.Contact.Queries
{
    public class GetContactsQuery
    {
        private readonly IContactRepositoryRead _contactRepositoryRead;

        public GetContactsQuery(IContactRepositoryRead contactRepositoryRead)
        {
            _contactRepositoryRead = contactRepositoryRead;
        }

        public async Task<List<PhoneBook.Core.Entities.Contact>> Execute()
        {
            return await _contactRepositoryRead.GetContactsAsync();
        }
    }
}
