using PhoneBook.Core.Entities;
using PhoneBook.Core.Interfaces;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace PhoneBook.Application.User.Queries
{
    public class GetUsersQuery
    {
        private readonly IUserRepositoryRead _userRepositoryRead;

        public GetUsersQuery(IUserRepositoryRead userRepositoryRead)
        {
            _userRepositoryRead = userRepositoryRead;
        }

        public async Task<List<PhoneBook.Core.Entities.User>> Execute()
        {
            return await _userRepositoryRead.GetUsersAsync();
        }
    }
}
