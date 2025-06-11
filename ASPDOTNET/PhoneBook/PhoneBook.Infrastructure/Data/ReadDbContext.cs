using Microsoft.EntityFrameworkCore;
using PhoneBook.Core.Entities;

namespace PhoneBook.Infrastructure.Data
{
    public class ReadDbContext : DbContext
    {
        public ReadDbContext(DbContextOptions<ReadDbContext> options) : base(options) { }

        public DbSet<User> Users { get; set; }
        public DbSet<Contact> Contacts { get; set; }
    }
}