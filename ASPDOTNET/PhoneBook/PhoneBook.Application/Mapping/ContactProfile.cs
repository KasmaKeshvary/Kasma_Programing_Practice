using AutoMapper;
using PhoneBook.Application.DTOs;
using DomainContact = PhoneBook.Core.Entities.Contact;

namespace PhoneBook.Application.Mapping
{
    public class ContactProfile : Profile
    {
        public ContactProfile()
        {
            CreateMap<DomainContact, ContactDto>();
            // CreateMap<ContactDto, Contact>();
        }
    }
}