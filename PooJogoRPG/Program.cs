using System;
using PooJogoRPG.Entities;

namespace PooJogoRPG {
    internal class Program {
        static void Main(string[] args) {

            Hero arus = new Hero ("Arus", 23, "Knight");
            Hero oponnent = new Hero ("Maleficus", 99, "Devil");
            Wizard jennica = new Wizard ("Jennica", 23, "White Wizard");

            Console.WriteLine(arus.ToString());

            System.Console.WriteLine(arus.Attack());
            System.Console.WriteLine(oponnent.Attack());
            System.Console.WriteLine(jennica.Attack(25));
        }
    }
}