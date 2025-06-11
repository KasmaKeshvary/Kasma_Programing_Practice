using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using PhoneBook.Core.Entities;
using PhoneBook.Core.Interfaces;
using PhoneBook.Infrastructure.Data;

namespace PhoneBook.Infrastructure.Repositories
{
    public class UserRepositoryRead : IUserRepositoryRead
    {
        private readonly ReadDbContext _context; // ✅ استفاده از ReadDbContext

        public UserRepositoryRead(ReadDbContext context) // ✅ مقداردهی در constructor
        {
            _context = context;
        }

        public async Task<List<User>> GetUsersAsync()
        {
            return await _context.Users.ToListAsync(); // ✅ عملیات خواندن از ReadDbContext
        }

        public async Task<User?> GetUserByUsernameAsync(string username)
        {
            return await _context.Users.FirstOrDefaultAsync(u => u.Username == username); 
        }

        public async Task<User?> GetUserByUsernameAndPasswordAsync(string username, string password)
        {
            return await _context.Users.FirstOrDefaultAsync(u => u.Username == username || u.Password == password );
        }
    }
}