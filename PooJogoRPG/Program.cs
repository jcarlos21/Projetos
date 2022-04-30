using System;
using PooJogoRPG.Entities;

namespace PooJogoRPG {
    internal class Program {
        static void Main(string[] args) {

            Knight arus = new Knight ("Arus", 23, "Knight", 749, 72);
            Knight oponnent = new Knight ("Maleficus", 99, "Devil", 749, 72);
            Wizard jennica = new Wizard ("Jennica", 23, "White Wizard", 601, 482);

            Console.WriteLine(arus.ToString());

            Console.WriteLine(arus.Attack());
            Console.WriteLine(oponnent.Attack());
            Console.WriteLine(jennica.Attack(25));

        }
    }
}