using MediatR;
using PhoneBook.Application.Services;

namespace PhoneBook.Application.User.Commands
{
    public class RegisterUserCommandHandler : IRequestHandler<RegisterUserCommand, Unit>
    {
        private readonly IUserService _userService;

        public RegisterUserCommandHandler(IUserService userService)
        {
            _userService = userService;
        }

        public async Task<Unit> Handle(RegisterUserCommand request, CancellationToken cancellationToken)
        {
            await _userService.RegisterUserAsync(
                request.Username,
                request.Password,
                request.DisplayName);

            return Unit.Value;
        }
    }
}