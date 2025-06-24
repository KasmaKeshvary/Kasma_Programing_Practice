namespace PhoneBook.Application.DTOs
{
    public class UserDto
    {
        public int Id { get; set; }
        public required string Username { get; set; }
        public required string DisplayName { get; set; }
    }
}