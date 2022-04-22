namespace PooJogoRPG.Entities
{
    public class Wizard : Hero {

        public Wizard(string name, int level, string heroType) {  // Construtor com parâmetros
            this.Name = name;
            this.Level = level;
            this.HeroType = heroType;
        }

        public Wizard(){  // Construtor com parâmetros
            
        }
        public override string Attack(){  // Uma maneira de polimorfismo
            return this.Name + " Lançou Magia";
        }

        public string Attack(int Bonus){  // Sobrecarga de método (Polimorfismo)
            return this.Name + $" Lançou Magia com bônus de ataque de {Bonus}.";
        }
    }
}