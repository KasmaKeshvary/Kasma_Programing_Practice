using PhoneBook.Core.Interfaces;
using System.Threading.Tasks;

namespace PhoneBook.Application.User.Commands
{
    public class CheckUserExistsCommand
    {
        private readonly IUserService _userService;

        public CheckUserExistsCommand(IUserService userService)
        {
            _userService = userService;
        }

        public async Task<bool> Execute(string username)
        {
            return await _userService.CheckUserExistsAsync(username);
        }
    }
}
