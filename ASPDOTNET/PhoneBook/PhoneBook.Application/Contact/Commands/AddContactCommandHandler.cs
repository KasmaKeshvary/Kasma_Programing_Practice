using MediatR;
using PhoneBook.Application.Services;

namespace PhoneBook.Application.Contact.Commands
{
    public class AddContactCommandHandler : IRequestHandler<AddContactCommand, Unit>
    {
        private readonly IContactService _contactService;

        public AddContactCommandHandler(IContactService contactService)
        {
            _contactService = contactService;
        }

        public async Task<Unit> Handle(AddContactCommand request, CancellationToken cancellationToken)
        {
            await _contactService.AddContactAsync(request._contactDtoAdd);

            return Unit.Value;
        }
    }
}