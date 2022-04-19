using System;
using PooJogoRPG.Entities;

namespace PooJogoRPG {
    internal class Program {
        static void Main(string[] args) {

            hero Arus = new hero ("Arus", 23, "Knight");

            Console.WriteLine(Arus.ToString());
            System.Console.WriteLine(Arus);  // Vai imprimir a mesma coisa que a linha anterior.


            
        }
    }
}