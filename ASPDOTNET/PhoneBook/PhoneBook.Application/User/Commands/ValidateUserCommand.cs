using PhoneBook.Core.Interfaces;
using PhoneBook.Core.Entities;
using System.Threading.Tasks;

namespace PhoneBook.Application.User.Commands
{
    public class ValidateUserCommand
    {
        private readonly IUserService _userService;

        public ValidateUserCommand(IUserService userService)
        {
            _userService = userService;
        }

        public async Task<PhoneBook.Core.Entities.User?> Execute(string username, string password)
        {
            return await _userService.ValidateUserAsync(username, password);
        }
    }
}
