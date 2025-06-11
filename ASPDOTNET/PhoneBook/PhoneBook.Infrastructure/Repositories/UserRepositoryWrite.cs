using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using PhoneBook.Core.Entities;
using PhoneBook.Core.Interfaces;
using PhoneBook.Infrastructure.Data;

namespace PhoneBook.Infrastructure.Repositories
{
    public class UserRepositoryWrite : IUserRepositoryWrite
    {
        private readonly WriteDbContext _context; // ✅ استفاده از ReadDbContext

        public UserRepositoryWrite(WriteDbContext context) // ✅ مقداردهی در constructor
        {
            _context = context;
        }
        
        public async Task AddUserAsync(string username, string password, string displayName)
        {
            var newUser = new User
            {
                Username = username,
                Password = password, // نکته: در محیط واقعی، همیشه کلمه عبور را هش کنید!
                DisplayName = displayName
            };

            _context.Users.Add(newUser);
            await _context.SaveChangesAsync();
        }
    }
}