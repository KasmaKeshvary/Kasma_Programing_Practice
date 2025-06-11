using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using PhoneBook.Core.Entities;
using PhoneBook.Core.Interfaces;


namespace PhoneBook.Infrastructure.Services
{
    public class UserService : IUserService
    {
        private readonly IUserRepositoryRead _userRepositoryRead;
        private readonly IUserRepositoryWrite _userRepositoryWrite;

        public UserService(IUserRepositoryRead userRepositoryRead, IUserRepositoryWrite userRepositoryWrite)
        {
            _userRepositoryRead = userRepositoryRead;
            _userRepositoryWrite = userRepositoryWrite;
        }

        public async Task<User?> ValidateUserAsync(string username, string password)
        {
            return await _userRepositoryRead.GetUserByUsernameAndPasswordAsync(username, password);
        }

        public async Task<bool> CheckUserExistsAsync(string username)
        {
            var user = await _userRepositoryRead.GetUserByUsernameAsync(username);
            return user != null;
        }

        public async Task RegisterUserAsync(string username, string password, string displayName)
        {
            await _userRepositoryWrite.AddUserAsync(username, password, displayName);
        }

    }
}