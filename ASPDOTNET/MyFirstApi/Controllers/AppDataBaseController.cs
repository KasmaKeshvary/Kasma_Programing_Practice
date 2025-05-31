using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc.ModelBinding;
using System.IO;

namespace HelloWord
{
    public class AppDataBase
    {
        public Fighter[] GetFighters()
        {
            var lines = File.ReadAllLines("DataBase.txt");

            Fighter[] fighters = new Fighter[lines.Length];

            for (var i = 0; i < lines.Length; i++)
            {
                string line = lines[i];
                Fighter fighter = ParseLine(line);
                fighters[i] = fighter;
            }

            return fighters;
        }

        private Fighter ParseLine(string input)
        {
            var values = input.Split(" ");

            string FighterName = values[0];
            int FighterPower = Convert.ToInt32(values[1]);

            return new Fighter(FighterName,FighterPower);
        } 
    }
}