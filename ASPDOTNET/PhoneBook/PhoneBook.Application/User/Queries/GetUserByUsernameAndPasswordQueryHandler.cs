using MediatR;
using PhoneBook.Application.DTOs;
using PhoneBook.Application.Services;

namespace PhoneBook.Application.User.Queries
{
    public class GetUserByUsernameAndPasswordQueryHandler : IRequestHandler<GetUserByUsernameAndPasswordQuery, UserDto?>
    {
        private readonly IUserService _userService;

        public GetUserByUsernameAndPasswordQueryHandler(IUserService userService)
        {
            _userService = userService;
        }

        public async Task<UserDto?> Handle(GetUserByUsernameAndPasswordQuery request, CancellationToken cancellationToken)
        {
            return await _userService.GetUserByUsernameAndPasswordAsync(request.UserName, request.Password);
        }
    }
}