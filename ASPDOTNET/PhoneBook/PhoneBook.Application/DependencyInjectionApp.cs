using Microsoft.Extensions.DependencyInjection;
using PhoneBook.Application.User.Queries;
using PhoneBook.Application.User.Commands;
using PhoneBook.Application.Contact.Queries;
using PhoneBook.Application.Contact.Commands;

namespace PhoneBook.Application
{
    public static class DependencyInjectionApp
    {
        public static IServiceCollection AddApplication(this IServiceCollection services)
        {
            // ثبت Queries و Commands
            services.AddScoped<GetUsersQuery>();
            services.AddScoped<RegisterUserCommand>();
            services.AddScoped<ValidateUserCommand>();
            services.AddScoped<CheckUserExistsCommand>();
            services.AddScoped<GetContactsQuery>();
            services.AddScoped<SearchContactsQuery>();
            services.AddScoped<AddContactCommand>();
            return services;
        }
    }
}