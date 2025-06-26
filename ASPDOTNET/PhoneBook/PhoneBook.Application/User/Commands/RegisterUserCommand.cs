using MediatR;

namespace PhoneBook.Application.User.Commands
{
    public class RegisterUserCommand : IRequest<Unit>
    {
        public string Username { get; init; }
        public string Password { get; init; }
        public string DisplayName { get; init; }

        public RegisterUserCommand(string username, string password, string displayName)
        {
            Username = username;
            Password = password;
            DisplayName = displayName;
        }
    }
}