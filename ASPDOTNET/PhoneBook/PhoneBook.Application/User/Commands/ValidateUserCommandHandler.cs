using MediatR;
using PhoneBook.Application.DTOs;
using PhoneBook.Application.Services;

namespace PhoneBook.Application.User.Commands
{
    public class ValidateUserCommandHandler : IRequestHandler<ValidateUserCommand, UserDto>
    {
        private readonly IUserService _userService;

        public ValidateUserCommandHandler(IUserService userService)
        {
            _userService = userService;
        }

        public async Task<UserDto> Handle(ValidateUserCommand request, CancellationToken cancellationToken)
        {
            return await _userService.ValidateUserAsync(
                request.Username,
                request.Password);
        }
    }
}