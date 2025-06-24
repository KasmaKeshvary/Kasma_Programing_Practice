using AutoMapper;
using FluentValidation;
using MediatR;
using Microsoft.Extensions.DependencyInjection;
using System.Reflection;
using PhoneBook.Application.Services;


namespace PhoneBook.Application
{
    public static class DependencyInjectionApp
    {
        public static IServiceCollection AddApplication(this IServiceCollection services)
        {
            // 1. MediatR برای Handlerهای CQRS
            services.AddMediatR(Assembly.GetExecutingAssembly());

            // 2. AutoMapper برای Mapping
            services.AddAutoMapper(Assembly.GetExecutingAssembly());

            // 3. Validatorها اگر لازم دارین
            // services.AddValidatorsFromAssembly(Assembly.GetExecutingAssembly());

            // 4. Serviceهای Use Case
            services.AddScoped<IUserService, UserService>();
            services.AddScoped<IContactService, ContactService>();

            return services;
        }
    }
}