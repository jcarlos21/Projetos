using System;

namespace DIO.BankTransf {
    class Program {
        static List<Conta> listContas = new List<Conta>();  // Criação de uma lista do tipo Conta
        static void Main(string[] args) {
            string opcaoUsuario = ObterOpcaoUsuario();

            while (opcaoUsuario.ToUpper() != "X") {
				switch (opcaoUsuario) {
					case "1":
						ListarContas();
						break;
					case "2":
						InserirConta();
						break;
					case "3":
						Transferir();
						break;
					case "4":
						Sacar();
						break;
					case "5":
						Depositar();
						break;
                    case "C":
						Console.Clear();
						break;

					default:
						throw new ArgumentOutOfRangeException();
				}

                opcaoUsuario = ObterOpcaoUsuario();                
            }

            Console.WriteLine("Obrigado por utilizar nossos serviços.");
			Console.ReadLine();
        }

        private static void Transferir() {
			Console.Write("Digite o número da conta de origem: ");
			int indiceContaOrigem = int.Parse(Console.ReadLine());

            Console.Write("Digite o número da conta de destino: ");
			int indiceContaDestino = int.Parse(Console.ReadLine());

			Console.Write("Digite o valor a ser transferido: ");
			double valorTransferencia = double.Parse(Console.ReadLine());

            listContas[indiceContaOrigem].Transferir(valorTransferencia, listContas[indiceContaDestino]);  // Acessando as contas na lista
		}

        private static void Sacar()	{

			Console.Write("Digite o número da conta: ");
			int indiceConta = int.Parse(Console.ReadLine());

			Console.Write("Digite o valor a ser sacado: ");
			double valorSaque = double.Parse(Console.ReadLine());

            listContas[indiceConta].Sacar(valorSaque);
		}

        private static void Depositar()	{
			Console.Write("Digite o número da conta: ");
			int indiceConta = int.Parse(Console.ReadLine());

			Console.Write("Digite o valor a ser depositado: ");
			double valorDeposito = double.Parse(Console.ReadLine());

            listContas[indiceConta].Depositar(valorDeposito);
		}
        
        private static void InserirConta() {
            
            Console.WriteLine("Inserir nova conta");

			Console.Write("Digite 1 para Conta Fisica ou 2 para Juridica: ");
			int entradaTipoConta = int.Parse(Console.ReadLine());

			Console.Write("Digite o Nome do Cliente: ");
			string entradaNome = Console.ReadLine();

			Console.Write("Digite o saldo inicial: ");
			double entradaSaldo = double.Parse(Console.ReadLine());

			Console.Write("Digite o crédito: ");
			double entradaCredito = double.Parse(Console.ReadLine());

			Conta novaConta = new Conta(tipoConta: (TipoConta)entradaTipoConta, saldo: entradaSaldo,
										credito: entradaCredito, nome: entradaNome);

			listContas.Add(novaConta);  // Adicionando a conta que criamos na lista criada.        
        }

        private static void ListarContas() {
			Console.WriteLine("Listar contas");

			if (listContas.Count == 0) {
				Console.WriteLine("Nenhuma conta cadastrada.");
				return;  // O return sozinho sai do método
			}

			for (int i = 0; i < listContas.Count; i++) {
				Conta conta = listContas[i];
				Console.Write("#{0} - ", i);
				Console.WriteLine(conta);  // Essa linha irá acionar o método ToString (o que foi sobreescrito)
			}
		}

        private static string ObterOpcaoUsuario() {
            Console.WriteLine();
            Console.WriteLine("Bank a seu dispor!!!");
            Console.WriteLine("Por favor, informe uma das opções a seguir:");

            Console.WriteLine("1 - Listar contas:");
            Console.WriteLine("2 - Inserir nova conta:");
            Console.WriteLine("3 - Transferir");
			Console.WriteLine("4 - Sacar");
			Console.WriteLine("5 - Depositar");
            Console.WriteLine("C - Limpar Tela");
			Console.WriteLine("X - Sair");
			Console.WriteLine();

			string opcaoUsuario = Console.ReadLine().ToUpper();
			Console.WriteLine();
			return opcaoUsuario;
        }
    }
}
