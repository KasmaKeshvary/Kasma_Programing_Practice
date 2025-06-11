using PhoneBook.Core.Entities;
using PhoneBook.Core.Interfaces;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace PhoneBook.Application.User.Queries
{
    public class GetUserByUsernameAndPasswordQuery
    {
        private readonly IUserRepositoryRead _userRepositoryRead;

        public GetUserByUsernameAndPasswordQuery(IUserRepositoryRead userRepositoryRead)
        {
            _userRepositoryRead = userRepositoryRead;
        }

        public async Task<PhoneBook.Core.Entities.User?> Execute(string username, string password)
        {
            return await _userRepositoryRead.GetUserByUsernameAndPasswordAsync(username, password);
        }
    }
}
