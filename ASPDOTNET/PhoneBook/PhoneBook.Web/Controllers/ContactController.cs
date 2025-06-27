using Microsoft.AspNetCore.Mvc;
using MediatR;
using PhoneBook.Application.Contact.Commands;
using PhoneBook.Application.Contact.Queries;
using PhoneBook.Application.DTOs;
using System.Text.RegularExpressions;


namespace PhoneBook.Web.Controllers
{
    public class ContactController : Controller
    {
        private readonly IMediator _mediator;

        public ContactController(IMediator mediator)
        {
            _mediator = mediator;
        }

        [HttpGet]
        public async Task<IActionResult> List()
        {
            var contacts = await _mediator.Send(new GetContactsQuery());
            return PartialView("_ContactListPartial", contacts);
        }

        [HttpGet]
        public async Task<IActionResult> Search(string query)
        {
            var contacts = await _mediator.Send(new SearchContactsQuery(query));
            return PartialView("_SearchPartial", contacts);
        }

        
        [HttpPost]
        public async Task<IActionResult> Add(string firstName, string lastName, string phoneNumber, string address, string email)
        {
            // اعتبارسنجی ورودی‌ها
            if (string.IsNullOrWhiteSpace(firstName) || !Regex.IsMatch(firstName, @"^[\p{L}]+$"))
            {
                TempData["AddContactSuccess"] = false;
                TempData["AddContactMessage"] = "نام معتبر نمی‌باشد.";
                return RedirectToAction("Index", "Home");
            }

            if (string.IsNullOrWhiteSpace(lastName) || !Regex.IsMatch(lastName, @"^[\p{L}]+$"))
            {
                TempData["AddContactSuccess"] = false;
                TempData["AddContactMessage"] = "نام خانوادگی معتبر نمی‌باشد.";
                return RedirectToAction("Index", "Home");
            }

            if (!Regex.IsMatch(phoneNumber, @"^09\d{9}$"))
            {
                TempData["AddContactSuccess"] = false;
                TempData["AddContactMessage"] = "شماره موبایل باید با 09 شروع شده و 11 رقمی باشد.";
                return RedirectToAction("Index", "Home");
            }

            if (!Regex.IsMatch(email, @"^\S+@\S+\.\S+$"))
            {
                TempData["AddContactSuccess"] = false;
                TempData["AddContactMessage"] = "فرمت ایمیل معتبر نیست.";
                return RedirectToAction("Index", "Home");
            }

            if (string.IsNullOrWhiteSpace(address) || address.Length < 30)
            {
                TempData["AddContactSuccess"] = false;
                TempData["AddContactMessage"] = "آدرس باید حداقل 30 کاراکتر باشد.";
                return RedirectToAction("Index", "Home");
            }

            try
            {
                var dto = new ContactDto
                {
                    FirstName = firstName,
                    LastName = lastName,
                    PhoneNumber = phoneNumber,
                    Address = address,
                    Email = email
                };

                await _mediator.Send(new AddContactCommand(dto));
                TempData["AddContactSuccess"] = true;
                TempData["AddContactMessage"] = "ثبت اطلاعات تماس با موفقیت انجام شد.";
            }
            catch (Exception ex)
            {
                // در صورت بروز خطا در ثبت اطلاعات
                TempData["AddContactSuccess"] = false;
                TempData["AddContactMessage"] = "خطا در ثبت اطلاعات تماس: " + ex.Message;
            }

            // به عنوان مثال، اگر view مربوط به لیست مخاطبین "List.cshtml" است
            return RedirectToAction("Index", "Home");

        }
    }
}

