#region call Api

// var builder = WebApplication.CreateBuilder(args);

// // Add services to the container.
// // Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
// builder.Services.AddEndpointsApiExplorer();
// builder.Services.AddSwaggerGen();

// var app = builder.Build();

// // Configure the HTTP request pipeline.
// if (app.Environment.IsDevelopment())
// {
//     app.UseSwagger();
//     app.UseSwaggerUI();
// }

// app.UseHttpsRedirection();

// var summaries = new[]
// {
//     "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
// };

// app.MapGet("/weatherforecast", () =>
// {
//     var forecast =  Enumerable.Range(1, 5).Select(index =>
//         new WeatherForecast
//         (
//             DateOnly.FromDateTime(DateTime.Now.AddDays(index)),
//             Random.Shared.Next(-20, 55),
//             summaries[Random.Shared.Next(summaries.Length)]
//         ))
//         .ToArray();
//     break forecast;
// })
// .WithName("GetWeatherForecast")
// .WithOpenApi();

// app.Run();

// record WeatherForecast(DateOnly Date, int TemperatureC, string? Summary)
// {
//     public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);
// }

/////////////////////////////////


// var builder = WebApplication.CreateBuilder(args);

// // Essential service configurations
// builder.Services.AddControllers(); // ← Enables controllers
// builder.Services.AddEndpointsApiExplorer();
// builder.Services.AddSwaggerGen();

// var app = builder.Build();

// // Middleware pipeline
// if (app.Environment.IsDevelopment())
// {
//     app.UseSwagger();
//     app.UseSwaggerUI();
// }

// app.UseHttpsRedirection();
// app.UseAuthorization();
// app.MapControllers(); // ← Critical for controller routing

// app.Run();

// using System;
// using System.Collections.Generic;
// using System.ComponentModel;
// using System.Linq;

// public class Product 
// {
//     public int Id{get;set;}
//     public string? Name{get;set;}
//     public decimal Price{get;set;} 

//     public override string ToString()
//     {
//         break $"Product [Id={Id}, Name={Name}, Price=${Price}]";
//     }
// }

// public class ShoppingCart 
// {
//     private List<Product> _items= new List<Product>();

//     public void AddProduct(Product product)
//     {
//         _items.Add(product);
//         Console.WriteLine($"Added: {product}"); // Uses ToString()
//     }

//     public decimal Total()
//     {
//         break _items.Sum(p => p.Price);
//     }

//     public void PrintAllItems()
//     {
//         Console.WriteLine("\nCurrent Cart Contents:");
        
//         foreach (var item in _items)
//         {
//             Console.WriteLine(item);
//         }
//     }
// }

// class Program
// {
//     static void Main(string[] args)
//     {
//         var laptop = new Product{Id = 1, Name = "LapTop", Price = 99.9m};
//         var phone = new Product{Id = 2, Name = "Phone", Price = 59.8m};

//         var cart = new ShoppingCart();

//         Console.WriteLine("Adding products to cart...");
//         cart.AddProduct(laptop);
//         cart.AddProduct(phone);

//         cart.PrintAllItems();

//         decimal tot = cart.Total();

//         Console.WriteLine($"Total: ${tot}");

//         // Keep console open
//         Console.WriteLine("Press any key to exit...");
//         Console.ReadKey(); 
//     }
// }

#endregion

#region systemsNeeds

using System;
using System.Runtime.Intrinsics.Arm;
using System.Security.Cryptography.X509Certificates;
using System.Text.RegularExpressions;
using Microsoft.AspNetCore.Components.Forms;
using System.Collections.Generic;
using System.Linq;

#endregion

namespace HelloWord
{
    class Program
    {
        static void Main(string[] args)
        {
            #region Main App Code

            // int number = 9;
            // string name = "Kasma";
            // string nuna = name + number.ToString();
            // number = 10;

            // int kasmaAge = 36, shirinAge = 32;
            
            // Console.WriteLine("kamas's Age:"+kasmaAge);
            // Console.WriteLine("shirin's Age:"+shirinAge);

            // kasmaAge ++;
            // Console.WriteLine("kamas's Age After one year:"+kasmaAge);
            
            // shirinAge = shirinAge + 1;
            // Console.WriteLine("shirin's Age After one year:"+shirinAge);

            // bool isKasmaOlder = kasmaAge > shirinAge;
            // Console.WriteLine("Is kasma older?"+ isKasmaOlder);

            // int decades = kasmaAge/10;
            // Console.WriteLine("Kasma has passed "+decades+" decades");

            // Console.WriteLine($"HelloWord {number} {name} {nuna}");
            #endregion

            #region Conditinal Code
            
            // int thisYear = 1400;

            // Console.WriteLine("enter your year:");

            // int year = int.Parse(Console.ReadLine() ?? string.Empty) ;

            // Console.WriteLine("year is:"+ year);

            // //int year = 1399;

            // if (year == thisYear)
            // {
            //     Console.WriteLine(year + " is this year");
            // } 
            // else if ( year < thisYear)
            // {
            //     Console.WriteLine("We are in the past");
            // }
            // else
            // {
            //     Console.WriteLine("We are in the future");
            // }

            
            // string someonesName ;
            // bool shouldContinue = true;

            // while(shouldContinue)
            // {
            //     Console.WriteLine($"Write a name:"); 

            //     someonesName = Console.ReadLine() ?? string.Empty;
                
            //     switch (someonesName)
            //     {
            //         case "peyman":
            //             Console.WriteLine("my  friend");
            //             shouldContinue = false;
            //             break;
            //         case "Abbaas":
            //             Console.WriteLine("my fahter");
            //             shouldContinue = false;
            //             break;
            //         case "kian":
            //             Console.WriteLine("my brother");
            //             shouldContinue = false;
            //             break;
            //         case "maryam":
            //             Console.WriteLine("my brother");
            //             shouldContinue = false;
            //             break;
            //         case "":
            //             Console.WriteLine("You don't write anything. Please write something:");
            //             break;
            //         default:
            //             Console.WriteLine("I don't know you");
            //             shouldContinue = false;
            //             break;
            //     }

            // }

            #endregion

            #region Loop Code
            
            // int hopNumber = 6;

            // for (int i = 0; i <= 100; i++)
            // {
            //     if(i%hopNumber == 0) Console.WriteLine($"hop");
            //     else Console.WriteLine($"{i}");
            // }

            // int numberOfFloor = 10;
            // int numberOfParkSpotINEachFloor = 20;
            
            // for (var i = 1; i <= numberOfFloor; i++)
            // {
            //     Console.WriteLine($"Floor: {i}");
                
            //     for (var j = 1; j <= numberOfParkSpotINEachFloor; j++)
            //     {
            //         Console.WriteLine($"car place number: {i}_{j}");
            //     }
            // }

            // int someNum = 10;

            // while(someNum >= 0 && DateTime.Now.Year == 2025)
            // {
            //     Console.WriteLine(someNum);
            //     Console.WriteLine(new Random().Next(0,100));
                
            //     someNum --;
            // }

            // int numberOfGuess = 0;
            // int randomNum = new Random().Next(0,100);
            // bool guessCondition = true ;

            
            // while(guessCondition)
            // {
            //     // Console.WriteLine($"enter your guess as a number:");
            //     // int guessNum = int.Parse(Console.ReadLine() ?? string.Empty);

                // Console.WriteLine("Enter your guess (0-99):");
                // string input = Console.ReadLine() ?? string.Empty;

                // // Check for empty input
                // if (string.IsNullOrWhiteSpace(input))
                // {
                //     Console.WriteLine("You didn't enter anything. Please enter a number.");
                //     continue;
                // }

                // // Try to parse the number
                // if (!int.TryParse(input, out int guessNum))
                // {
                //     Console.WriteLine("Invalid input. Please enter a valid number.");
                //     continue;
                // }

            //     if (guessNum < randomNum)
            //     {
            //         Console.WriteLine($"your guess number is smaller than the random number");
            //         numberOfGuess ++;
            //         continue;
            //     }
            //     else if (guessNum > randomNum)
            //     {
            //         Console.WriteLine($"your guess number is bigger than the random number");
            //         numberOfGuess ++;
            //         continue;
            //     }else if (guessNum == randomNum)
            //     {
            //         numberOfGuess ++;
            //         Console.WriteLine($"your guess it right After {numberOfGuess} try");
            //         guessCondition = false;
            //         break;
            //     }                 
            // }

            #endregion
            
            #region Rock Papper Sciccors
            
            // // Define the array
            // string[] choices = ["Rock", "Paper", "Scissors"];
            // string userChoice = "";
            // string computerChoice = "";

            // int userScore = 0; 
            // int computerScore = 0;
            // int winScore = 3;

            // while (userScore<winScore && computerScore<winScore)
            // {
                
            //     int randomIndex = new Random().Next(0,choices.Length);
            //     // Console.WriteLine(randomIndex);
            //     computerChoice = choices[randomIndex];
            //     // Console.WriteLine(computerChoice);

            //     // Show options to user
            //     Console.WriteLine("Choose your move:");
            //     for (int i = 0; i < choices.Length; i++)
            //     {
            //         Console.WriteLine($"{i + 1}. {choices[i]}");
            //     }

            //     bool correctInput = true;

            //     while(correctInput)
            //     {
            //         // Get user input
            //         Console.Write("Enter your choice (1-3):");
            //         string input = Console.ReadLine() ?? string.Empty;
            //         // Validate and process input
            //         if (int.TryParse(input, out int choice) && choice >= 1 && choice <= choices.Length)
            //         {
            //             userChoice = choices[choice - 1]; // Convert to 0-based index
            //             Console.WriteLine($"You chose: {userChoice}");
            //             correctInput = false;
            //         }
            //         else
            //         {
            //             Console.WriteLine("Invalid input. Please enter 1, 2, or 3.");
            //         }

            //     }
                
                
            //     Console.WriteLine($"computerChoice: {computerChoice} , userChoice: {userChoice}");
                
            //     switch (computerChoice)
            //     {
            //         case "Rock":
            //             if(userChoice == "Paper")
            //             {
            //                 userScore ++;
            //             }
            //             else if(userChoice == "Scissors")
            //             {
            //                 computerScore ++;
            //             }
            //             break;
            //         case "Paper":
            //             if(userChoice == "Scissors")
            //             {
            //                 userScore ++;
            //             }
            //             else if(userChoice == "Rock")
            //             {
            //                 computerScore ++;
            //             }
            //             break;
            //         case "Scissors":
            //             if(userChoice == "Rock")
            //             {
            //                 userScore ++;
            //             }
            //             else if(userChoice == "Paper")
            //             {
            //                 computerScore ++;
            //             }
            //             break;
            //     }

            //     Console.WriteLine($"computerScore:{computerScore} , userScore: {userScore}");
            // }

            // if(userScore > computerScore)
            //     Console.WriteLine($"the winner is you :))) yeah :))) ");
            // else
            //     Console.WriteLine($"the winner is computer :(( ");

            #endregion
            
            #region Array

            // string[] sample = new string[5];

            // for (int i = 0; i < sample.Length; i++)
            // {
            //     Console.WriteLine($"Enter into sample Array:");
            //     string input = Console.ReadLine() ?? string.Empty;
            //     sample[i] = input;
            // }

            // for (int j = 0; j < sample.Length; j++)
            // {
            //     Console.WriteLine($"The sample array {j} : is {sample[j]}");
            // }

            #endregion

            #region Plindrome Game
            
            // string userWord = "";
            // bool isString = true;
            // bool isPlindrome = true;
            // int score = 0;

            // while(isPlindrome)
            // {
            //     while(isString)
            //     {
            //         Console.WriteLine($"Enter your word:");
            //         userWord = Console.ReadLine() ?? string.Empty;

            //         if (!IsValidString(userWord))
            //         {
            //             Console.WriteLine("Error: Input must not contain numbers");
            //             // return; // Exit or handle the error
            //         }
            //         else
            //         {
            //             isString = false;
            //         }
            //     }

            //     isString = true;

            //     //Continue with your palindrome logic
            //     Console.WriteLine($"Valid input: {userWord}");

            //     char[] lettersUserWord = userWord.ToCharArray();

            //     for (int i = 0; i < lettersUserWord.Length; i++)
            //     {
            //         Console.WriteLine($"letter {i} : {lettersUserWord[i]}");
            //         if(lettersUserWord[i] != lettersUserWord[lettersUserWord.Length-i-1])
            //         {                    
            //             Console.WriteLine($"You lose with score {score}.your word is not Plindrome. The letters number {i+1} from begining and ending are not equal");
            //             isPlindrome = false;
            //             break;
            //         }
            //     }
                
            //     if(isPlindrome == true) 
            //     {
            //         score++;
            //         Console.WriteLine($"Your word is Plindrome and your score is {score}");
            //     }
            // }
            
            #endregion

            #region using car class
            
            // Car car1 = new Car(900,"Benz");
            
            // Console.WriteLine(car1.IntroduceYourself());
            
            // Car car2 = new Car(1995,"Pride");
            // Console.WriteLine(car2.IntroduceYourself());

            #endregion

            #region function

            // int FirstNumber = 0;
            // var ValidFirstNumber = WhileCheckingNumber(5,"Enter your first number:");
            // if(!ValidFirstNumber.IsValid)
            //     Console.WriteLine($"{ValidFirstNumber.Error}");
            // else
            //     FirstNumber = ValidFirstNumber.Number;

            // int SecondNumber = 0;
            // var ValidSecondNumber = WhileCheckingNumber(5,"Enter your second number:");
            // if(!ValidSecondNumber.IsValid)
            //     Console.WriteLine($"{ValidSecondNumber.Error}");   
            // else
            //     SecondNumber = ValidSecondNumber.Number;
            
            // Console.WriteLine($"first number is {FirstNumber} , second number is {SecondNumber}");

            // string result = CompareNumber(FirstNumber,SecondNumber);
            // Console.WriteLine($"{result}");
            
            #endregion 

            #region Properties

            // Employee kasma = new Employee(37);


            // if(kasma.AmIRetired())
            //     Console.WriteLine($"this person is retired");
            // else
            //     Console.WriteLine($"this person can still work");

            #endregion

            #region Inheritance

            // Animal myPet = new Animal("cat");
            // myPet.TalkAboutYourself();
            // // Animal bob = new Cat();
            // var kitty = new Cat();
            // kitty.Name = "bob";
            // kitty.Feed();
            // kitty.TalkAboutYourself();

            #endregion


            #region Animal Game

            var db = new AppDataBase();
            var fighters = db.GetFighters();

            // for (var i = 0; i < fighters.Length; i++)
            // {
            //     fighters[i].Introduce();
            // }
            
            int score = 0;

            int userChoice = 0;

            bool isContinue = true;

            while (isContinue)
            {
                Fighter fighter1 = fighters[new Random().Next(0, fighters.Length)];
                Fighter fighter2 = fighters[new Random().Next(0, fighters.Length)];
                Fighter fighter3 = fighters[new Random().Next(0, fighters.Length)];
                Fighter fighter4 = fighters[new Random().Next(0, fighters.Length)];

                Team team1 = new Team(fighter1, fighter2);
                Team team2 = new Team(fighter3, fighter4);

                int winnerTeam = 0;

                if (team1.TeamPower() > team2.TeamPower())
                    winnerTeam = 1;
                else
                    winnerTeam = 2;



                Console.WriteLine($"Guess which team wins");

                Console.WriteLine($"Team 1 is");
                Console.WriteLine($"{fighter1.Name}");
                Console.WriteLine($"{fighter2.Name}");
                Console.WriteLine($"Team 2 is");
                Console.WriteLine($"{fighter3.Name}");
                Console.WriteLine($"{fighter4.Name}");

                var ValidNumber = WhileCheckingNumber(3, "Enter the number of winner team:");

                if (!ValidNumber.IsValid)
                {
                    Console.WriteLine($"{ValidNumber.Error}");
                    continue;
                }
                else if (ValidNumber.IsValid && ValidNumber.Number != 1 && ValidNumber.Number != 2)
                {
                    Console.WriteLine($"you have to enter 1 or 2");
                    continue;
                }
                else
                {
                    userChoice = ValidNumber.Number;

                    if (userChoice == winnerTeam)
                    {
                        score++;
                        Console.WriteLine($"You guess it right and win this hand. Your score is {score}");
                    }
                    else if (winnerTeam == 0)
                    {
                        Console.WriteLine($"The power of teams are equal");
                    }
                    else
                    {
                        score--;
                        Console.WriteLine($"Your guess is worng and you lose a score. Your score is {score}");
                    }
                }
                    
                
                Console.WriteLine("Do you want to continue? (Y/N)");
                string? userContinued = Console.ReadLine()?.Trim().ToUpper(); // Ensure uppercase input

                if (userContinued == "Y")
                {
                    Console.WriteLine("Ok Let's play more");
                    // Add logic for when the user selects Yes
                }
                else if (userContinued == "N")
                {
                    Console.WriteLine("Ok. You don't want to play anymore.");
                    isContinue = false;
                }
                else
                {
                    Console.WriteLine("Invalid input. Please enter Y or N.");
                }
                
            }

            #endregion

                #region usingLinq

                // // int[] scores = new int[2];

                // // scores[0] = 10;
                // // scores[1] = 20;
                // // scores[2] = 30;

                // List<int> scores = new List<int>(); 

                // scores.Add(10);
                // scores.Add(20);
                // scores.Add(30);
                // scores.Add(40);
                // scores.Add(50);
                // scores.Add(40);
                // scores.Add(30);

                // Console.WriteLine($"the average is : {scores.Average()}");
                // Console.WriteLine($"the last number is : {scores.Last()}");
                // scores.ForEach(score => Console.WriteLine(score));

                // List<int> othernumber = new List<int>();

                // othernumber = scores.Where(a => a>20 && a<50).ToList();

                // // for (var i = 0; i < scores.Count; i++)
                // // {
                // //     Console.WriteLine($"{scores[i]}");
                // // }

                // Console.WriteLine(string.Join(", ", othernumber));

                #endregion

                #region Enum

                // Console.WriteLine($"Select your gender:");
                // Console.WriteLine($"100.Unspecified");
                // Console.WriteLine($"200.Male");
                // Console.WriteLine($"300.Female");

                // var userInput = Console.ReadLine();
                // int userChoice = 0;

                // try
                // {
                //     userChoice = Convert.ToInt32(userInput);
                // }
                // catch (System.Exception)
                // {
                //     Console.WriteLine($"you didn't enter a number");
                //     // throw;
                // }

                // // int userChoice = int.Parse(userInput ?? string.Empty);



                // Gender userGender = (Gender) userChoice;

                // switch (userGender)
                // {
                //     case Gender.Unspecified:
                //         Console.WriteLine($"You did not specified your gender");
                //         break;
                //     case Gender.Male:
                //         Console.WriteLine($"You are male");
                //         break;
                //     case Gender.Female:
                //         Console.WriteLine($"You are female");
                //         break;
                // }


                #endregion

                #region Finishing App
                Console.WriteLine("App coding is finished");
            Console.WriteLine("GoodBye");
            #endregion
        }

        #region neededClasses

        public static  bool IsValidString(string input)
        {
            return !Regex.IsMatch(input, @"\d"); // Returns true if no digits found
        }

        public static string CompareNumber( int x, int y)
        {
            if (x>y) return "First number is greater";
            else if (x<y) return "Second number is greater";
            else return "both of them are equal";
        }

        public static (bool IsValid, int Number, string? Error) ValidateNumber (string input)
        {
            if(string.IsNullOrWhiteSpace(input)) return (false,0,"No input provided");
            if(!int.TryParse(input, out int number)) return (false,0,"Invalid number format");
            return(true,number,null);
        }

        public static (bool IsValid, int Number, string? Error) WhileCheckingNumber(int repeatNumber, string enterMessage)
        {
            bool isUnacceptable = true;
            int repeated = 0;
            int outputNumber = 0;

            while(isUnacceptable && repeated <= repeatNumber)
            {
                Console.WriteLine($"{enterMessage}");
            
                string inputString = Console.ReadLine() ?? string.Empty;
                var validation = ValidateNumber(inputString); 

                if(!validation.IsValid)
                {
                    Console.WriteLine(validation.Error);
                    repeated++;
                    continue;
                }

                isUnacceptable = false;
                outputNumber = validation.Number;
            }

            if(repeated >= repeatNumber && isUnacceptable)
                return(false,0,$"In {repeatNumber} , try you didn't put the correct format"); 
            else
                return(true,outputNumber,null);
        }

        #endregion

    }
}

