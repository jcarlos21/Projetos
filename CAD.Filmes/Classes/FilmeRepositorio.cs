using System;
using System.Collections.Generic;
using CAD.Filmes.Interfaces;

namespace CAD.Filmes {

    public class FilmeRepositorio : IRepositorio<Filmes> {

        private List<Filmes> listaFilmes = new List<Filmes>();
        public void Atualiza(int id, Filmes objeto)
		{
			listaFilmes[id] = objeto;
		}

		public void Exclui(int id)
		{
			listaFilmes[id].Excluir();
		}

		public void Insere(Filmes objeto)
		{
			listaFilmes.Add(objeto);
		}

		public List<Filmes> Lista()
		{
			return listaFilmes;
		}

		public int ProximoId()
		{
			return listaFilmes.Count;
		}

		public Filmes RetornaPorId(int id)
		{
			return listaFilmes[id];
		}
    }
}