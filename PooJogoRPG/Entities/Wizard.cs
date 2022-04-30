namespace PooJogoRPG.Entities
{
    public class Wizard : Hero {

        public Wizard(string name, int level, string heroType, int hp, int mp) {  // Construtor com parâmetros
            this.Name = name;
            this.Level = level;
            this.HeroType = heroType;
            this.HP = hp;
            this.MP = mp;
        }

        public Wizard(){  // Construtor sem parâmetros
            
        }
        public override string Attack(){  // Uma maneira de polimorfismo
            return this.Name + " Lançou Magia";
        }

        public string Attack(int Bonus){  // Sobrecarga de método (Polimorfismo)
            if (Bonus > 6) {
                return this.Name + $" Lançou Magia Super Efetiva com bônus de {Bonus}.";
            }
            else{
                return this.Name + $" Lançou Magia com força fraca e bônus de {Bonus}.";
            }
        }
    }
}