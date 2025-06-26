using MediatR;
using PhoneBook.Application.DTOs;

namespace PhoneBook.Application.User.Commands
{
    public class ValidateUserCommand : IRequest<UserDto>
    {
        public string Username { get; init; }
        public string Password { get; init; }

        public ValidateUserCommand(string username, string password)
        {
            Username = username;
            Password = password;
        }
    }
}