using PhoneBook.Core.Interfaces;
using System.Threading.Tasks;

namespace PhoneBook.Application.User.Commands
{
    public class RegisterUserCommand
    {
        private readonly IUserService _userService;
    
        public RegisterUserCommand(IUserService userService)
        {
            _userService = userService;
        }
    
        public async Task Execute(string username, string password, string displayName)
        {
            await _userService.RegisterUserAsync(username, password, displayName);
        }
    }
}
