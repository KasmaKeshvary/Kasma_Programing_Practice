using MediatR;
using PhoneBook.Application.Services;
using PhoneBook.Application.DTOs;

namespace PhoneBook.Application.Contact.Queries
{
    public class SearchContactsQueryHandler : IRequestHandler<SearchContactsQuery, List<ContactDto>>
    {
        private readonly IContactService _contactService;

        public SearchContactsQueryHandler(IContactService contactService)
        {
            _contactService = contactService;
        }

        public async Task<List<ContactDto>> Handle(SearchContactsQuery request, CancellationToken cancellationToken)
        {
            return await _contactService.SearchContactsAsync(request._query); 
        }
    }
}