using MediatR;
using PhoneBook.Application.Services;

namespace PhoneBook.Application.User.Commands
{
    public class CheckUserExistsCommandHandler : IRequestHandler<CheckUserExistsCommand, Unit>
    {
        private readonly IUserService _userService;

        public CheckUserExistsCommandHandler(IUserService userService)
        {
            _userService = userService;
        }

        public async Task<Unit> Handle(CheckUserExistsCommand request, CancellationToken cancellationToken)
        {
            await _userService.CheckUserExistsAsync(
                request.Username);

            return Unit.Value;
        }
    }
}