using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc.ModelBinding;

namespace HelloWord
{
    public class Car
    {
        private int CreatedAt;
        private string? ModelName;

        public Car(int createdAt, string modelName)
        {
            this.CreatedAt = createdAt;
            this.ModelName = modelName;
        }

        public string IntroduceYourself()
        {
            if(CreatedAt < 2000 && CreatedAt > 1000 )
                return "I'm old and my model is " + ModelName + "I'm manufactured at " + CreatedAt ;
            else if(CreatedAt < 1000)
                return "I'm ancient";
            else
            {
                return "I'm new and my model is " + ModelName + "I'm manufactured at " + CreatedAt;
            }
        }
    }

    
}