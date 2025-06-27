using MediatR;

namespace PhoneBook.Application.User.Queries
{
    public class CheckUserExistsQuery  : IRequest<bool>
    {
        public string Username { get; init; }
        
        public CheckUserExistsQuery (string username)
        {
            Username = username;
        }
    }
}