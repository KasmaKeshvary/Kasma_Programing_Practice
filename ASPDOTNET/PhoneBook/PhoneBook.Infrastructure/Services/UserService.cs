using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using PhoneBook.Core.Entities;
using PhoneBook.Core.Interfaces;
using PhoneBook.Infrastructure.Data;

namespace PhoneBook.Infrastructure.Services
{
    public class UserService : IUserService // اضافه کردن پیاده‌سازی Interface
    {
        private readonly PhoneBookContext _context;

        // دریافت DbContext از طریق DI
        public UserService(PhoneBookContext context)
        {
            _context = context;
        }

        // اعتبارسنجی کاربر به کمک EF
        public async Task<User?> ValidateUserAsync(string username, string password)
        {
            return await _context.Users
                .FirstOrDefaultAsync(u => u.Username == username && u.Password == password);
        }

       // بررسی وجود کاربر به کمک EF
        public async Task<bool> CheckUserExistsAsync(string username)
        {
            return await _context.Users.AnyAsync(u => u.Username == username);
        }


        // ثبت کاربر جدید به کمک EF
        public async Task RegisterUserAsync(string username, string password, string displayName)
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