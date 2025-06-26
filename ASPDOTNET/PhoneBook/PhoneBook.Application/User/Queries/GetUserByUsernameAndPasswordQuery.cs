using MediatR;
using PhoneBook.Application.DTOs;

namespace PhoneBook.Application.User.Queries
{
    public class GetUserByUsernameAndPasswordQuery : IRequest<UserDto?>
    {
        public string UserName { get; init; }
        public string Password { get; init; }
        public GetUserByUsernameAndPasswordQuery(string username, string password)
        {
            UserName = username;
            Password = password;
        }
    }
}