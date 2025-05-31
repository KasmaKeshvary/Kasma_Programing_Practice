using Microsoft.AspNetCore.Mvc;

namespace MyFirstApi.Controllers;

[ApiController]
[Route("api/[controller]")]  // ← Makes route "/api/data"
public class DataController : ControllerBase
{
    [HttpPost]
    public IActionResult Post([FromBody] Person person)
    {
        return Ok($"Hello {person.Name}! Age: {person.Age}");
    }
}

public class Person
{
    public string? Name { get; set; }
    public int Age { get; set; }
}