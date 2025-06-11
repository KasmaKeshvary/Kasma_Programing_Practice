using PhoneBook.Core.Entities;
using PhoneBook.Core.Interfaces;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace PhoneBook.Application.User.Queries
{
    public class GetUserByUsernameQuery
    {
        private readonly IUserRepositoryRead _userRepositoryRead;

        public GetUserByUsernameQuery(IUserRepositoryRead userRepositoryRead)
        {
            _userRepositoryRead = userRepositoryRead;
        }

        public async Task<PhoneBook.Core.Entities.User?> Execute(string username)
        {
            return await _userRepositoryRead.GetUserByUsernameAsync(username);
        }
    }
}
