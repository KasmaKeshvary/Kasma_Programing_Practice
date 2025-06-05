using Microsoft.AspNetCore.Mvc;
using PhoneBook.Infrastructure.Repositories;
using System.Threading.Tasks;

namespace PhoneBook.Web.Controllers
{
    public class ContactController : Controller
    {
        private readonly ContactRepository _contactRepository;

        public ContactController(ContactRepository contactRepository)
        {
            _contactRepository = contactRepository;
        }

        [HttpGet]
        public async Task<IActionResult> List()
        {
            var contacts = await _contactRepository.GetContactsAsync();
            return PartialView("_ContactListPartial", contacts);
        }
    }
}