class CacheAssociativo:
    def __init__(self, cache_size, ram_size, politica):
        self.cache_size = cache_size
        self.ram_size = ram_size
        self.politica = politica.lower()
        
        self.cache = [(None, None, False) for _ in range(cache_size)]
        
        self.ram = {}
        self.populate_ram()
        
        self.controle_politica = {}
        self.contador = 0  # lru/fifo
        
    def populate_ram(self):
        for i in range(self.ram_size):
            self.ram[i] = i
    
    def print_cache(self):
        print("Cache:")
        for linha, (endereco, valor, valido) in enumerate(self.cache):
            status = f"Endereço {endereco} -> Valor {valor}" if valido else "Vazia"
            print(f"Linha {linha}: {status}")
        print()
    
    def print_ram(self):
        print("RAM:")
        for address, value in self.ram.items():
            print(f"Endereço {address}: {value}")
        print()
    
    def buscar_endereco(self, address, novo_valor=None):
        print(f"Buscando endereço {address}...")
        
        # cache hit?
        for i, (endereco, valor, valido) in enumerate(self.cache):
            if valido and endereco == address:
                print("Cache HIT!")
                
                # atualiza politica
                if self.politica == 'lru':
                    self.controle_politica[address] = self.contador
                    self.contador += 1
                elif self.politica == 'lfu':
                    self.controle_politica[address] += 1
                
                # novo valor?
                if novo_valor is not None:
                    print(f"Atualizando valor no endereço {address} para {novo_valor}")
                    self.cache[i] = (address, novo_valor, True)
                    self.ram[address] = novo_valor
                    return novo_valor
                return valor
        
        print("Cache MISS...")
        valor_ram = self.ram[address]
        
        linha = self.encontrar_linha_para_substituir()
        
        # atualiza ram se linha estava ocupada
        endereco_antigo, valor_antigo, valido = self.cache[linha]
        if valido:
            print(f"Atualizando RAM no endereço {endereco_antigo} com valor {valor_antigo}")
            self.ram[endereco_antigo] = valor_antigo
            del self.controle_politica[endereco_antigo]
        
        print(f"Carregando valor {valor_ram} da RAM para a cache (linha {linha})")
        self.cache[linha] = (address, valor_ram, True)
        
        # atualiza politica
        if self.politica == 'lru':
            self.controle_politica[address] = self.contador
            self.contador += 1
        elif self.politica == 'lfu':
            self.controle_politica[address] = 1
        elif self.politica == 'fifo':
            self.controle_politica[address] = self.contador
            self.contador += 1
        
        # novo valor?
        if novo_valor is not None:
            print(f"Atualizando valor no endereço {address} para {novo_valor}")
            self.cache[linha] = (address, novo_valor, True)
            self.ram[address] = novo_valor
            return novo_valor
        
        return valor_ram
    
    def encontrar_linha_para_substituir(self):
        # procura linha vazia
        for i, (endereco, valor, valido) in enumerate(self.cache):
            if not valido:
                return i
        
        # substitui se nao tiver vazia
        if self.politica == 'lru':
            endereco_subst = min(self.controle_politica.items(), key=lambda x: x[1])[0]
        elif self.politica == 'lfu':
            endereco_subst = min(self.controle_politica.items(), key=lambda x: x[1])[0]
        elif self.politica == 'fifo':
            endereco_subst = min(self.controle_politica.items(), key=lambda x: x[1])[0]
        
        for i, (endereco, valor, valido) in enumerate(self.cache):
            if endereco == endereco_subst:
                return i
        return 0


print("=== Simulador de Cache com Mapeamento Associativo ===")

while True:
    politica = input("Escolha a política de substituição (LRU, LFU ou FIFO): ").strip().lower()
    if politica in ['lru', 'lfu', 'fifo']:
        break
    print("Política inválida! Escolha entre LRU, LFU ou FIFO")

cache = CacheAssociativo(4, 16, politica)

print(f"\nPolítica selecionada: {politica.upper()}")
print("\nEstado inicial:")
cache.print_ram()
cache.print_cache()

print("\n=== Primeira busca (miss) ===")
cache.buscar_endereco(5)
cache.print_cache()

print("\n=== Segunda busca (miss) ===")
cache.buscar_endereco(0)
cache.print_cache()

print("\n=== Terceira busca (miss) ===")
cache.buscar_endereco(3)
cache.print_cache()

print("\n=== Busca com atualização (miss) ===")
cache.buscar_endereco(1, 10)
cache.print_cache()

print("\n=== Busca (hit) ===")
cache.buscar_endereco(5)
cache.print_cache()

print("\n=== Busca com atualização (hit) ===")
cache.buscar_endereco(5, 100)
cache.print_cache()

print("\n=== Busca que causa substituição ===")
cache.buscar_endereco(9)
cache.print_cache()

print("\n=== Segunda busca que causa substituição ===")
cache.buscar_endereco(7)
cache.print_cache()

print("\n=== Terceira busca que causa substituição ===")
cache.buscar_endereco(6)
cache.print_cache()

print("\n=== Quarta busca que causa substituição ===")
cache.buscar_endereco(10)
cache.print_cache()

print("\n=== Quinta busca que causa substituição ===")
cache.buscar_endereco(12)
cache.print_cache()

print("\n=== Estado Final ===")
cache.print_ram()