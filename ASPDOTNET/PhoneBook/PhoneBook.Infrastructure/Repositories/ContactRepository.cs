using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using PhoneBook.Core.Entities;
using PhoneBook.Core.Interfaces;
using PhoneBook.Infrastructure.Data;

namespace PhoneBook.Infrastructure.Repositories
{
    public class ContactRepository : IContactRepository // اضافه کردن پیاده‌سازی
    {
        private readonly PhoneBookContext _context;

        // دریافت PhoneBookContext از طریق DI
        public ContactRepository(PhoneBookContext context)
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

        // ثبت contact جدید به کمک EF
        public async Task AddContactAsync(string firstName, string lastName, string phoneNumber, string address, string email)
        {
            var newContact = new Contact
            {
                FirstName = firstName,
                LastName = lastName,
                PhoneNumber = phoneNumber,
                Address = address,
                Email = email
            };
            
            _context.Contacts.Add(newContact);
            await _context.SaveChangesAsync();
        }
    }
    
}