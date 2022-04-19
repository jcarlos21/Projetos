using System;
using PooJogoRPG.Entities;

namespace PooJogoRPG {
    internal class Program {
        static void Main(string[] args) {

            hero arus = new hero ("Arus", 23, "Knight");
            hero oponnent = new hero ("Maleficus", 99, "Devil");

            Console.WriteLine(arus.ToString());
            System.Console.WriteLine(arus);  // Vai imprimir a mesma coisa que a linha anterior.

            System.Console.WriteLine(oponnent);


            
        }
    }
}