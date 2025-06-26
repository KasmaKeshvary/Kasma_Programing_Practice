using MediatR;
using PhoneBook.Application.DTOs;

namespace PhoneBook.Application.Contact.Queries
{
    public class GetContactsQuery : IRequest<List<ContactDto>>
    {
        // چون هیچ پارامتری نداره، خالی می‌مونه
    }
}