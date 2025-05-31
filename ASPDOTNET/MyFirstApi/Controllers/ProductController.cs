using Microsoft.AspNetCore.Mvc;

namespace MyFirstApi.Controllers;

[ApiController]
[Route("api/cart")]
public class CartController : ControllerBase
{
    private ShoppingCart _cart = new ShoppingCart();

    [HttpPost("add")]
    public IActionResult AddToCart([FromBody] Product product)
    {
        _cart.AddProduct(product);
        return Ok($"Added {product.Name} to cart.");
    }

    [HttpGet("total")]
    public IActionResult GetTotal()
    {
        return Ok($"Total: ${_cart.CalculateTotal()}");
    }
}

public class Product
{
    public int Id { get; set; }
    public string? Name { get; set; }
    public decimal Price { get; set; }
}

public class ShoppingCart
{
    private List<Product> _items = new List<Product>();

    public void AddProduct(Product product)
    {
        _items.Add(product);
    }

    public decimal CalculateTotal()
    {
        return _items.Sum(p => p.Price);
    }
}