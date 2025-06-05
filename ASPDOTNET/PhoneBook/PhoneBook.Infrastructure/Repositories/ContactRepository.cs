using System;
using System.Collections.Generic;
using Microsoft.Data.SqlClient;
using System.Threading.Tasks;
using Microsoft.Extensions.Options;
using PhoneBook.Core.Entities;
using PhoneBook.Core.Settings;

namespace PhoneBook.Infrastructure.Repositories
{
    public class ContactRepository
    {
        private readonly string _connectionString;

        // دریافت رشته اتصال از طریق تنظیمات strongly typed که با IOptions تزریق می‌شود.
        public ContactRepository(IOptions<DatabaseSettings> options)
        {
            _connectionString = options.Value.DBString;
        }

        // متدی برای دریافت لیست مخاطبین از دیتابیس
        public async Task<List<Contact>> GetContactsAsync()
        {
            var contacts = new List<Contact>();

            using var connection = new SqlConnection(_connectionString);

            await connection.OpenAsync();
            // اجرای کوئری جهت دریافت اطلاعات مخاطبین
            var query = "SELECT Id, FirstName, LastName, PhoneNumber, Address FROM Contacts";

            using var command = new SqlCommand(query, connection);

            using var reader = await command.ExecuteReaderAsync();
                    
            while (await reader.ReadAsync())
            {
                var contact = new Contact
                {
                    Id = reader.GetInt32(0),
                    FirstName = reader.GetString(1),
                    LastName = reader.GetString(2),
                    PhoneNumber = reader.GetString(3),
                    Address = reader.GetString(4)
                };
                contacts.Add(contact);
            }

            return contacts;
        }
    }
}