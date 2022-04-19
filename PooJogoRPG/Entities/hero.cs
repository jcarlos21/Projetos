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

        // Método construtor sem parâmetros
        public hero() {            
        }
    }
}