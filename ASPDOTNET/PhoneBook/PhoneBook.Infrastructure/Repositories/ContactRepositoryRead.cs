using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using PhoneBook.Core.Entities;
using PhoneBook.Core.Interfaces;
using PhoneBook.Infrastructure.Data;

namespace PhoneBook.Infrastructure.Repositories
{
    public class ContactRepositoryRead : IContactRepositoryRead // اضافه کردن پیاده‌سازی
    {
        private readonly ReadDbContext _context; // ✅ استفاده از ReadDbContext

        public ContactRepositoryRead(ReadDbContext context) // ✅ مقداردهی در constructor
        {
            _context = context;
        }


        // متدی برای دریافت لیست مخاطبین از دیتابیس به کمک EF
        public async Task<List<Contact>> GetContactsAsync()
        {
            return await _context.Contacts.ToListAsync();
        }

        // متد جستجو برای مخاطبین به کمک EF و کوئری‌های LINQ
        public async Task<List<Contact>> SearchContactsAsync(string searchQuery)
        {
            // اگر عبارت جستجو خالی یا null باشد، تمام مخاطبین را برگردانید
            if (string.IsNullOrWhiteSpace(searchQuery))
            {
                return await _context.Contacts.ToListAsync();
            }

            return await _context.Contacts
                .Where(c =>
                    c.FirstName.Contains(searchQuery) ||
                    c.LastName.Contains(searchQuery) ||
                    c.PhoneNumber.Contains(searchQuery) ||
                    c.Address.Contains(searchQuery))
                .ToListAsync();
        }
    } 
}