﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RealCalcWithFunctions
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter num1: ");
            int n1 = int.Parse(Console.ReadLine());
            Console.Write("Enter num2: ");
            int n2 = int.Parse(Console.ReadLine());
            Console.Write("Choose an options: add, sub, mul, or div: ");
            string op = Console.ReadLine();
            int result = 0;
            if (op == "add") result = n1 + n2;
            else if (op == "sub") result = n1 - n2;
            else if (op == "mul") result = n1 * n2;
            else if (op == "div") result = n1 / n2;
            Console.WriteLine("Result: " + result);
            wait();
        }
        public static void wait()
        {
            Console.ReadLine();
        }
        public static int add(int x, int y)
        {
            return x + y;
        }
        public static int sub(int x, int y)
        {
            return x - y;
        }
        public static int mul(int x, int y)
        {
            return x * y;
        }
        public static int div(int x, int y)
        {
            return x / y;
        }
    }
}
