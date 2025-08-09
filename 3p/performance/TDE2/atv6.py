class MemoriaVirtualFIFO:
    def __init__(self, tamanho_mem_fisica, tamanho_mem_virtual, tamanho_pagina):
        self.tamanho_mem_fisica = tamanho_mem_fisica  # Em número de quadros
        self.tamanho_mem_virtual = tamanho_mem_virtual  # Em número de páginas
        self.tamanho_pagina = tamanho_pagina  # Tamanho de cada página em bytes
        
        # Memória física (quadros)
        self.mem_fisica = [None] * tamanho_mem_fisica
        # Fila para controle FIFO
        self.fila_quadros = []
        # Tabela de páginas: mapeia página -> quadro (ou None se não está na memória)
        self.tabela_paginas = {i: None for i in range(tamanho_mem_virtual)}
        # Memória secundária (simulada)
        self.mem_secundaria = {i: f"Conteúdo da página {i}" for i in range(tamanho_mem_virtual)}
    
    def acessar_memoria(self, endereco_virtual, operacao='leitura', dado=None):
        pagina = endereco_virtual // self.tamanho_pagina
        
        print(f"\nAcessando endereço virtual {endereco_virtual} (Página {pagina})")
        
        # Verifica se a página está na memória física
        if self.tabela_paginas[pagina] is not None:
            quadro = self.tabela_paginas[pagina]
            print(f"Page HIT! Página {pagina} está no quadro {quadro}")
            
            if operacao == 'escrita':
                print(f"Escrevendo '{dado}' no endereço {endereco_virtual}")
                self.mem_fisica[quadro] = f"Conteúdo modificado da página {pagina} (dado: {dado})"
            
            return self.mem_fisica[quadro]
        else:
            print(f"Page MISS! Página {pagina} não está na memória física")
            
            # Encontrar um quadro livre ou substituir
            quadro = self._encontrar_quadro()
            
            # Se o quadro estava ocupado, precisamos salvar a página antiga (se foi modificada)
            if self.mem_fisica[quadro] is not None:
                pagina_antiga = next(p for p, q in self.tabela_paginas.items() if q == quadro)
                print(f"Substituindo página {pagina_antiga} no quadro {quadro} (FIFO)")
                self.tabela_paginas[pagina_antiga] = None
            
            # Carregar a nova página
            print(f"Carregando página {pagina} da memória secundária para o quadro {quadro}")
            self.mem_fisica[quadro] = self.mem_secundaria[pagina]
            self.tabela_paginas[pagina] = quadro
            
            # Atualizar a fila FIFO
            if quadro in self.fila_quadros:
                self.fila_quadros.remove(quadro)
            self.fila_quadros.append(quadro)
            
            if operacao == 'escrita':
                print(f"Escrevendo '{dado}' no endereço {endereco_virtual}")
                self.mem_fisica[quadro] = f"Conteúdo modificado da página {pagina} (dado: {dado})"
            
            return self.mem_fisica[quadro]
    
    def _encontrar_quadro(self):
        # Primeiro tenta encontrar um quadro livre
        for i, conteudo in enumerate(self.mem_fisica):
            if conteudo is None:
                return i
        
        # Se não tem livre, usa FIFO para substituição
        quadro_substituir = self.fila_quadros.pop(0)
        return quadro_substituir
    
    def imprimir_estado(self):
        print("\nMemória Física (Quadros):")
        for quadro, conteudo in enumerate(self.mem_fisica):
            pagina = next((p for p, q in self.tabela_paginas.items() if q == quadro), None)
            status = f"Página {pagina}: {conteudo}" if conteudo is not None else "Livre"
            print(f"Quadro {quadro}: {status}")
        
        print("\nFila FIFO (ordem de substituição):", self.fila_quadros)


# Simulação
print("=== Simulador de Memória Virtual com Substituição FIFO ===")
# 3 quadros na memória física, 10 páginas virtuais, tamanho de página = 100 bytes
mv = MemoriaVirtualFIFO(3, 10, 100)

print("\nEstado inicial:")
mv.imprimir_estado()

print("\n=== Primeiro acesso (page fault) ===")
mv.acessar_memoria(150)  # Página 1
mv.imprimir_estado()

print("\n=== Segundo acesso (page fault) ===")
mv.acessar_memoria(20)   # Página 0
mv.imprimir_estado()

print("\n=== Terceiro acesso (page fault) ===")
mv.acessar_memoria(320)  # Página 3
mv.imprimir_estado()

print("\n=== Acesso a página existente (page hit) ===")
mv.acessar_memoria(170)  # Página 1
mv.imprimir_estado()

print("\n=== Acesso causando substituição FIFO ===")
mv.acessar_memoria(450)  # Página 4 (substitui a página 1)
mv.imprimir_estado()

print("\n=== Acesso com escrita ===")
mv.acessar_memoria(25, 'escrita', "1")  # Página 0
mv.imprimir_estado()

print("\n=== Outra substituição FIFO ===")
mv.acessar_memoria(550)  # Página 5 (substitui a página 0)
mv.imprimir_estado()