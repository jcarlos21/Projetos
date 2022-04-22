namespace PooJogoRPG.Entities
{
    public class BlackWizard : Hero {
        public BlackWizard(string name, int level, string heroType, int hp, int mp) {
            this.Name = name;
            this.Level = level;
            this.HeroType = heroType;
            this.HP = hp;
            this.MP = mp;
        }

        public BlackWizard() {
            
        }
    }
}