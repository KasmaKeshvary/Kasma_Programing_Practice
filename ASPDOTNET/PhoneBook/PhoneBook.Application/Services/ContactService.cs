using PhoneBook.Core.Interfaces;
using PhoneBook.Application.DTOs;
using AutoMapper;

namespace PhoneBook.Application.Services
{
    public class ContactService : IContactService
    {
        private readonly IContactRepositoryRead _contactRepositoryRead;
        private readonly IContactRepositoryWrite _contactRepositoryWrite;
        private readonly IMapper _mapper;

        public ContactService(
            IContactRepositoryRead contactRepositoryRead,
            IContactRepositoryWrite contactRepositoryWrite,
            IMapper mapper)
        {
            _contactRepositoryRead = contactRepositoryRead;
            _contactRepositoryWrite = contactRepositoryWrite;
            _mapper = mapper;
        }

        public async Task<List<ContactDto>> GetContactsAsync()
        {
            var contacts = await _contactRepositoryRead.GetContactsAsync();
            return contacts == null ? new List<ContactDto>() : _mapper.Map<List<ContactDto>>(contacts);
        }

        public async Task<List<ContactDto>> SearchContactsAsync(string query)
        {
            var contacts = await _contactRepositoryRead.SearchContactsAsync(query);
            return contacts == null ? new List<ContactDto>() : _mapper.Map<List<ContactDto>>(contacts);
        }

        public async Task AddContactAsync(ContactDto contact)
        {
            await _contactRepositoryWrite.AddContactAsync(contact.FirstName, contact.LastName, contact.PhoneNumber, contact.Address, contact.Email);
        }
    }
}