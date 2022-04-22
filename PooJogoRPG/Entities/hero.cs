namespace PooJogoRPG.Entities {
    public class Hero {
        public string Name;
        public int Level;
        public string HeroType;

        // Método construtor com parâmetros
        public Hero(string name, int level, string heroType) {  // Classe criada para qualquer herói (conceito de abstração)
            this.Name = name;
            this.Level = level;
            this.HeroType = heroType;
        }

        // Método construtor sem parâmetros (construtor vazio)
        public Hero() {            
        }

        public override string ToString(){  // Sobrescrita do método ToString()
            return this.Name + " " + this.Level + " " + this.HeroType;
        }

        public virtual string Attack(){  // Virtual indica: "Eu permito que qualquer um dos meus filhos sobrescreva meu método Attack()." 
            return this.Name + " Atacou com a sua espada.";
        }
    }
}