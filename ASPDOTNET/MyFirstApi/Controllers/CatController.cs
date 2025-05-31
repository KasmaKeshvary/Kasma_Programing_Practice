using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc.ModelBinding;

namespace HelloWord
{
    public sealed class Cat : Animal
    {
        private int energy = 0;
        private int mood = 0;
        public Cat() : base ("kasma")
        {
            
        }

        public void Feed()
        {
            energy++;
            mood++;
        }

        public override void TalkAboutYourself()
        {
            base.TalkAboutYourself();

            Console.WriteLine($"my energy value is {energy}");
            Console.WriteLine($"my mood value is {mood}");

        }
    }
}