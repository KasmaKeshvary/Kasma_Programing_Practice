using System.Collections.Generic;
using System.Threading.Tasks;
using PhoneBook.Core.Entities;

namespace PhoneBook.Core.Interfaces
{
    public interface IContactRepositoryWrite
    {
        Task AddContactAsync(string firstName, string lastName, string phoneNumber, string address, string email);
    }
}