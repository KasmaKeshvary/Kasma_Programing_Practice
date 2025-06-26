using MediatR;
using PhoneBook.Application.DTOs;

namespace PhoneBook.Application.Contact.Commands
{
    public class AddContactCommand : IRequest<Unit>
    {
        public ContactDto _contactDtoAdd;
        public AddContactCommand(ContactDto _contactDto)
        {
            _contactDtoAdd = _contactDto;
        }
    }
}