namespace PooJogoRPG.Entities {
    public class hero {
        public string Name;
        public int Level;
        public string HeroType;

        // Método construtor com parâmetros
        public hero(string name, int level, string heroType) {
            this.Name = name;
            this.Level = level;
            this.HeroType = heroType;
        }

        // Método construtor sem parâmetros (construtor vazio)
        public hero() {            
        }

        public override string ToString(){  // Sobrescrita do método ToString()
            return this.Name + " " + this.Level + " " + this.HeroType;
        }

        public string Attack(){
            return this.Name + " Atacou com a sua espada.";
        }
    }
}