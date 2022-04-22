namespace PooJogoRPG.Entities {
    public abstract class Hero {  // 'abstract' indica que a classe Hero (classe mâe) só pode ser herdada e não instanciada. Trata-se de uma classe
    // específica.
        public string Name;
        public int Level;
        public string HeroType;
        public int HP;
        public int MP;

        // Método construtor com parâmetros
        public Hero(string name, int level, string heroType, int hp, int mp) {  // Classe criada para qualquer herói (conceito de abstração)
            this.Name = name;
            this.Level = level;
            this.HeroType = heroType;
            this.HP = hp;
            this.MP = mp;
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