using PhoneBook.Core.Interfaces;
using PhoneBook.Application.DTOs;
using AutoMapper;

namespace PhoneBook.Application.Services
{
    public class UserService : IUserService
    {
        private readonly IUserRepositoryRead _userRepositoryRead;
        private readonly IUserRepositoryWrite _userRepositoryWrite;
        private readonly IMapper _mapper;

        public UserService(
        IUserRepositoryRead userRepositoryRead,
        IUserRepositoryWrite userRepositoryWrite,
        IMapper mapper
        )
        {
            _userRepositoryRead = userRepositoryRead;
            _userRepositoryWrite = userRepositoryWrite;
            _mapper = mapper;
        }

        public async Task<UserDto> ValidateUserAsync(string username, string password)
        {
            var user = await _userRepositoryRead.GetUserByUsernameAndPasswordAsync(username, password);
            if (user is null)
                throw new KeyNotFoundException("کاربری با این مشخصات یافت نشد.");

            return _mapper.Map<UserDto>(user);
        }

        public async Task<bool> CheckUserExistsAsync(string username)
        {
            var user = await _userRepositoryRead.GetUserByUsernameAsync(username);
            return user != null;
        }

        public async Task RegisterUserAsync(string username, string password, string displayName)
        {
            await _userRepositoryWrite.AddUserAsync(username, password, displayName);
        }

    }
}