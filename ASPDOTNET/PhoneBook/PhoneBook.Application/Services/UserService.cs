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
            var entities = await _userRepositoryRead.GetUserByUsernameAndPasswordAsync(username, password);
            if (entities is null)
                throw new KeyNotFoundException("کاربری با این مشخصات یافت نشد.");

            return _mapper.Map<UserDto>(entities);
        }

        public async Task<bool> CheckUserExistsAsync(string username)
        {
            var entities = await _userRepositoryRead.GetUserByUsernameAsync(username);
            return entities != null;
        }

        public async Task RegisterUserAsync(string username, string password, string displayName)
        {
            await _userRepositoryWrite.AddUserAsync(username, password, displayName);
        }

        public async Task<List<UserDto>> GetAllUsersAsync()
        {
            var entities = await _userRepositoryRead.GetUsersAsync();
            return _mapper.Map<List<UserDto>>(entities);
        }

        public async Task<UserDto?> GetUserByUsernameAsync(string username)
        {
            var entities = await _userRepositoryRead.GetUserByUsernameAsync(username);
            return entities is null ? null : _mapper.Map<UserDto?>(entities);
        }

        public async Task<UserDto?> GetUserByUsernameAndPasswordAsync(string username, string password)
        {
            var entities = await _userRepositoryRead.GetUserByUsernameAndPasswordAsync(username,password);
            return entities is null ? null : _mapper.Map<UserDto?>(entities);
        }
    }
}