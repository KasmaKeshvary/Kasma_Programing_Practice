using MediatR;
using PhoneBook.Application.DTOs;

namespace PhoneBook.Application.User.Queries
{
    public class GetUsersQuery : IRequest<List<UserDto>>
    {
        // چون هیچ پارامتری نداره، خالی می‌مونه
    }
}