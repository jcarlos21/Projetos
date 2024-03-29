﻿using System;

namespace CAD.Filmes {
    class Program {
        static FilmeRepositorio repositorio = new FilmeRepositorio();
        static void Main(string[] args) {
            
            string opcaoUsuario = ObterOpcaoUsuario();

            while (opcaoUsuario.ToUpper() != "X") {
                switch (opcaoUsuario) {
                    case "1":
                        ListarFilmes();
                        break;
                    case "2":
                        InserirFilme();
                        break;
                    case "3":
                        AtualizarFilme();
                        break;
                    case "4":
                        ExcluirFilme();
                        break;
                    case "5":
                        VisualizarFilme();
                        break;
                    case "C":
                        Console.Clear();
                        break;

                    default:
                        throw new ArgumentOutOfRangeException();
                }

                opcaoUsuario = ObterOpcaoUsuario();
            }

            static void ExcluirFilme() {
                Console.Write("Digite o id do filme: ");
                int indiceFilme = int.Parse(Console.ReadLine());

                repositorio.Exclui(indiceFilme);
            }

            static void VisualizarFilme() {
                Console.Write("Digite o id do filme: ");
                int indiceFilme = int.Parse(Console.ReadLine());

                var filme = repositorio.RetornaPorId(indiceFilme);

                Console.WriteLine(filme);
		    }

            static void AtualizarFilme() {
                Console.Write("Digite o id do filme: ");
                int indiceFilme = int.Parse(Console.ReadLine());

                foreach (int i in Enum.GetValues(typeof(Genero))) {
                    Console.WriteLine("{0}-{1}", i, Enum.GetName(typeof(Genero), i));
                }
                Console.Write("Digite o gênero entre as opções acima: ");
                int entradaGenero = int.Parse(Console.ReadLine());

                Console.Write("Digite o Título do filme: ");
                string entradaTitulo = Console.ReadLine();

                Console.Write("Digite o Ano de Início do filme: ");
                int entradaAno = int.Parse(Console.ReadLine());

                Console.Write("Digite a Descrição do filme: ");
                string entradaDescricao = Console.ReadLine();

                Filmes atualizaFilme = new Filmes(id: indiceFilme,
                                            genero: (Genero)entradaGenero,
                                            titulo: entradaTitulo,
                                            ano: entradaAno,
                                            descricao: entradaDescricao);

                repositorio.Atualiza(indiceFilme, atualizaFilme);
		    }

            static void ListarFilmes() {
                Console.WriteLine("Listar filmes");

                var lista = repositorio.Lista();

                if (lista.Count == 0) {
                    Console.WriteLine("Nenhum filme cadastrado.");
                    return;
                }

                foreach (var filme in lista) {
                    var excluido = filme.retornaExcluido();

                    Console.WriteLine("#ID {0}: - {1} {2}", filme.retornaId(), filme.retornaTitulo(), (excluido ? "*Excluído*" : ""));
                }
            }

            static void InserirFilme() {
                Console.WriteLine("Inserir novo filme");

                foreach (int i in Enum.GetValues(typeof(Genero)))
                {
                    Console.WriteLine("{0}-{1}", i, Enum.GetName(typeof(Genero), i));
                }
                Console.Write("Digite o gênero entre as opções acima: ");
                int entradaGenero = int.Parse(Console.ReadLine());

                Console.Write("Digite o Título do Filme: ");
                string entradaTitulo = Console.ReadLine();

                Console.Write("Digite o Ano do Filme: ");
                int entradaAno = int.Parse(Console.ReadLine());

                Console.Write("Digite a Descrição do Filme: ");
                string entradaDescricao = Console.ReadLine();

                Filmes novoFilme = new Filmes(id: repositorio.ProximoId(),
                                            genero: (Genero)entradaGenero,
                                            titulo: entradaTitulo,
                                            ano: entradaAno,
                                            descricao: entradaDescricao);

                repositorio.Insere(novoFilme);
		    }

            static string ObterOpcaoUsuario() {
                Console.WriteLine();
                Console.WriteLine("CAD filmes a seu dispor!!!\n");
                Console.WriteLine("Informe a opção desejada:");

                Console.WriteLine("1- Listar filmes");
                Console.WriteLine("2- Inserir novo filme");
                Console.WriteLine("3- Atualizar filme");
                Console.WriteLine("4- Excluir filme");
                Console.WriteLine("5- Visualizar filme");
                Console.WriteLine("C- Limpar Tela");
                Console.WriteLine("X- Sair");
                Console.WriteLine();

                string opcaoUsuario = Console.ReadLine().ToUpper();
                Console.WriteLine();
                return opcaoUsuario;
            }
        }
    }
}
