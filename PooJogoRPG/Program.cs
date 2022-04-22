using System;
using PooJogoRPG.Entities;

namespace PooJogoRPG {
    internal class Program {
        static void Main(string[] args) {

            Knight arus = new Knight ("Arus", 23, "Knight", 749, 72);
            Knight oponnent = new Knight ("Maleficus", 99, "Devil", 749, 72);
            Wizard jennica = new Wizard ("Jennica", 23, "White Wizard", 601, 482);

            Console.WriteLine(arus.ToString());

            System.Console.WriteLine(arus.Attack());
            System.Console.WriteLine(oponnent.Attack());
            System.Console.WriteLine(jennica.Attack(25));
        }
    }
}