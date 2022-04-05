namespace DIO.BankTransf  // A palavra 'conta' foi retirada de namespace DIO.BankTransf.Conta para ficar tudo no mesmo namespace
{
    public class Conta
    {
        // Propriedades (ou atributos) são privadas (encapsuladas)______________
        private TipoConta TipoConta { get; set; }
        private double Saldo { get; set; }
        private double Credito { get; set; }
        private string Nome { get; set; }

        // Método Construtor (método chamado no momento de criação do objeto)__
        public Conta (TipoConta tipoConta, double saldo, double credito, string nome)
        {
            this.TipoConta = tipoConta;  // 'this' indica que se refere a esta instância
            this.Saldo = saldo;
            this.Credito = credito;
            this.Nome = nome;
        }

        // Ações ou métodos da Conta___________________________________________
        public bool Sacar (double valorSaque) {
            // Validação de saldo suficiente (Ex: 1000-1501 = -501, se Credito == -500)
            if (this.Saldo - valorSaque < (this.Credito * (-1))) {
                Console.WriteLine("Saldo insuficente!");
                return false;
            }
            this.Saldo -= valorSaque;
            // this.Saldo = this.Saldo - valorSaque;
            Console.WriteLine("Saldo atual da conta de {0} é {1}", this.Nome, this.Saldo);
            return true;
        }

        public void Depositar (double valorDeposito) {
            this.Saldo += valorDeposito;
            Console.WriteLine("Saldo atual da conta de {0} é {1}", this.Nome, this.Saldo);
        }

        public void Transferir (double valorTransferencia, Conta contaDestino) {
            if(this.Sacar(valorTransferencia)) {
                contaDestino.Depositar(valorTransferencia);
            }
        }

        public override string ToString() {  // Sobrecarga (sobreescreve) de método (Polimorfismo)
            string retorno = "";
            retorno += "TipoConta " + this.TipoConta + " | ";
            retorno += "Nome " + this.Nome + " | ";
            retorno += "Saldo " + this.Saldo + " | ";
            retorno += "Crédito " + this.Credito;
            return retorno;
            // Geralmente o método é usado para criar logs da aplicação (saber o que está ocorrendo).
        }

        
    }
}