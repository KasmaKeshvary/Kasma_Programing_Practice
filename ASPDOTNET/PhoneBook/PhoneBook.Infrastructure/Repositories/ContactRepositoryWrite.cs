using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using PhoneBook.Core.Entities;
using PhoneBook.Core.Interfaces;
using PhoneBook.Infrastructure.Data;

namespace PhoneBook.Infrastructure.Repositories
{
    public class ContactRepositoryWrite : IContactRepositoryWrite // اضافه کردن پیاده‌سازی
    {
        private readonly WriteDbContext _context; // ✅ استفاده از ReadDbContext

        public ContactRepositoryWrite(WriteDbContext context) // ✅ مقداردهی در constructor
        {
            _context = context;
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