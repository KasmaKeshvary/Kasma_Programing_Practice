using System.Collections.Generic;
using System.Threading.Tasks;
using PhoneBook.Application.DTOs;

namespace PhoneBook.Application.Services
{
    public interface IContactService
    {
        // برگرداندن همه مخاطبین
        Task<List<ContactDto>> GetContactsAsync();

        // جستجوی مخاطبین بر اساس متن ورودی
        Task<List<ContactDto>> SearchContactsAsync(string query);

        // ثبت یک مخاطب جدید
        Task AddContactAsync(ContactDto contact);

        //— اگر خواستی بعداً اضافه کنی —
        // Task<ContactDto?> GetContactByIdAsync(int id);
        // Task UpdateContactAsync(ContactDto contact);
        // Task DeleteContactAsync(int id);
    }
}