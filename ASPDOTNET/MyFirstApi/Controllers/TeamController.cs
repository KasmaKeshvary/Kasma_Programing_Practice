using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc.ModelBinding;

namespace HelloWord
{
    public class Team
    {
        private Fighter FirstFighter;
        private Fighter SecondFighter;
        public Team(Fighter fighter1, Fighter fighter2)
        {
            this.FirstFighter = fighter1;
            this.SecondFighter = fighter2;
        }

        public int TeamPower()
        {
            return FirstFighter.Power + SecondFighter.Power;
        }
    }
}