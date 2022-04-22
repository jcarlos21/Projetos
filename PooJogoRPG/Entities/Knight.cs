namespace PooJogoRPG.Entities
{
    public class Knight : Hero {
        
        public Knight(string name, int level, string heroType, int hp, int mp) {  // Construtor com parâmetros
            this.Name = name;
            this.Level = level;
            this.HeroType = heroType;
            this.HP = hp;
            this.MP = mp;
        }

        public Knight() {

        }
    }
}