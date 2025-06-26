using MediatR;

namespace PhoneBook.Application.User.Commands
{
    public class CheckUserExistsCommand : IRequest<Unit>
    {
        public string Username { get; init; }
        
        public CheckUserExistsCommand(string username)
        {
            Username = username;
        }
    }
}