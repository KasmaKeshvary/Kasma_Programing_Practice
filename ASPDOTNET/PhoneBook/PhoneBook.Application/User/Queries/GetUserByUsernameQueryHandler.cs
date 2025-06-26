using MediatR;
using PhoneBook.Application.DTOs;
using PhoneBook.Application.Services;

namespace PhoneBook.Application.User.Queries
{
    public class GetUserByUsernameQueryHandler : IRequestHandler<GetUserByUsernameQuery, UserDto?>
    {
        private readonly IUserService _userService;

        public GetUserByUsernameQueryHandler(IUserService userService)
        {
            _userService = userService;
        }

        public async Task<UserDto?> Handle(GetUserByUsernameQuery request, CancellationToken cancellationToken)
        {
            return await _userService.GetUserByUsernameAsync(request.UserName);
        }
    }
}