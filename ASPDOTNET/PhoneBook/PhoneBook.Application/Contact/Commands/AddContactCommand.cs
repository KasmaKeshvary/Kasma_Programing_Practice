using PhoneBook.Core.Entities;
using PhoneBook.Core.Interfaces;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace PhoneBook.Application.Contact.Commands
{
    public class AddContactCommand
    {
        private readonly IContactRepositoryWrite _contactRepositoryWrite;

        public AddContactCommand(IContactRepositoryWrite contactRepositoryWrite)
        {
            _contactRepositoryWrite = contactRepositoryWrite;
        }

        public async Task Execute(string firstName, string lastName, string phoneNumber, string address, string email)
        {
            await _contactRepositoryWrite.AddContactAsync(firstName, lastName, phoneNumber, address, email);
        }
    }
}
