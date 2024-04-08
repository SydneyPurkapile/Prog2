using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FavClub
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter your favorite sport: ");
            string sport = Console.ReadLine();
            Console.WriteLine("Your favorite sport is " + sport);

            Console.ReadKey();
        }
    }
}
