using AutoMapper;
using PhoneBook.Application.DTOs;
using DomainUser = PhoneBook.Core.Entities.User;

namespace PhoneBook.Application.Mapping
{
    public class UserProfile : Profile
    {
        public UserProfile()
        {
            CreateMap<DomainUser, UserDto>();
            // اگر نیاز به نگاشت معکوس داشتی:
            // CreateMap<UserDto, User>();
        }
    }
}