using Microsoft.EntityFrameworkCore;
using PhoneBook.Core.Entities; // دسترسی به مدل‌های دامین

namespace PhoneBook.Infrastructure.Data
{
    public class PhoneBookContext : DbContext
    {
        public PhoneBookContext(DbContextOptions<PhoneBookContext> options)
            : base(options)
        {
        }

        // DbSet ها برای هر مدل
        public DbSet<Contact> Contacts { get; set; }
        public DbSet<User> Users { get; set; }
    }
}