using MediatR;
using PhoneBook.Application.Services;

namespace PhoneBook.Application.User.Queries
{
    public class CheckUserExistsQueryHandler : IRequestHandler<CheckUserExistsQuery, bool>
    {
        private readonly IUserService _userService;

        public CheckUserExistsQueryHandler(IUserService userService)
        {
            _userService = userService;
        }

        public async Task<bool> Handle(CheckUserExistsQuery request, CancellationToken cancellationToken)
        {
            return await _userService.CheckUserExistsAsync(request.Username);
        }
    }
}