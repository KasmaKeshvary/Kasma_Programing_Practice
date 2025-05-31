using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc.ModelBinding;

namespace HelloWord
{
    public class Animal
    {
        public string Name {get;set;}

        public Animal(string name)
        {
            this.Name = name;
        }

        public virtual void TalkAboutYourself()
        {
            Console.WriteLine($"I am a {Name}");
            
        }
        
    }
}