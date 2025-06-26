using MediatR;
using PhoneBook.Application.Services;
using PhoneBook.Application.DTOs;

namespace PhoneBook.Application.Contact.Queries
{
    public class GetContactsQueryHandler : IRequestHandler<GetContactsQuery, List<ContactDto>>
    {
        private readonly IContactService _contactService;

        public GetContactsQueryHandler(IContactService contactService)
        {
            _contactService = contactService;
        }

        public async Task<List<ContactDto>> Handle(GetContactsQuery request, CancellationToken cancellationToken)
        {
            return await _contactService.GetContactsAsync(); 
        }
    }
}