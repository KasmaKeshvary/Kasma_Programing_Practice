using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc.ModelBinding;

namespace HelloWord
{
    public class Fighter
    {
        public string Name;
        public int Power;

        public Fighter(string name, int power)
        {
            this.Name = name;
            this.Power = power;
        }

        public void Introduce()
        {
            Console.WriteLine($"I am {Name}");
        }
    }
}