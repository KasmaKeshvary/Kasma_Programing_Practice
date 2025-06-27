using MediatR;
using PhoneBook.Application.DTOs;

namespace PhoneBook.Application.Contact.Commands
{
    public class AddContactCommand : IRequest<Unit>
    {
        public ContactDto Contact { get; init; }
        public AddContactCommand(ContactDto _contactDto)
        {
            Contact = _contactDto;
        }
    }
}