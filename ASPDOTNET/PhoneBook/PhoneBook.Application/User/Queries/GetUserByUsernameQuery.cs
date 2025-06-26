using MediatR;
using PhoneBook.Application.DTOs;

namespace PhoneBook.Application.User.Queries
{
    public class GetUserByUsernameQuery : IRequest<UserDto?>
    {
        public string UserName { get; init; }
        public GetUserByUsernameQuery(string username)
        {
            UserName = username;
        }
    }
}