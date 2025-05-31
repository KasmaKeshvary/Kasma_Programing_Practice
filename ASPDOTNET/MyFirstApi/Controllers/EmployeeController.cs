using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc.ModelBinding;

namespace HelloWord
{
    public class Employee 
    {
        private int age;
        public int Age {
            get
            {
                return this.age;
            }
            private set
            {
                this.age = value;
                if(this.age > 65)
                    IsRetired = true;
            }
        }
        private bool IsRetired;

        public Employee(int input_age)
        {
            this.Age = input_age;
        }

        public bool AmIRetired()
        {
            return IsRetired;
        }
    }
}