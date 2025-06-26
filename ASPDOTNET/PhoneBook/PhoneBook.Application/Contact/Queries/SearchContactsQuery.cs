using MediatR;
using PhoneBook.Application.DTOs;

namespace PhoneBook.Application.Contact.Queries
{
    public class SearchContactsQuery : IRequest<List<ContactDto>>
    {
        public string _query;
        public SearchContactsQuery(string query)
        {
            _query = query;
        }
    }
}