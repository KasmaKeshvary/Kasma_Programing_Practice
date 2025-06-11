using Microsoft.EntityFrameworkCore;
using PhoneBook.Core.Entities;

namespace PhoneBook.Infrastructure.Data
{
    public class WriteDbContext : DbContext
    {
        public WriteDbContext(DbContextOptions<WriteDbContext> options) : base(options) { }

        public DbSet<User> Users { get; set; }
        public DbSet<Contact> Contacts { get; set; }
    }
}