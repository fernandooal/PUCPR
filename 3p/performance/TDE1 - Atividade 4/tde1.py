class CacheMapeamentoDireto:
    def __init__(self, cache_size, ram_size):
        self.cache_size = cache_size
        self.ram_size = ram_size
        
        self.cache = self.cache = [(None, None, False) for _ in range(self.cache_size)]
        self.ram = {}
        
        self.populate_ram()

    def populate_ram(self):
        for i in range(self.ram_size):
            self.ram[i] = i
        
    def print_cache(self):
        print("Cache:")
        for linha, (tag, valor, valido) in enumerate(self.cache):
            status = f"Tag {tag} -> Valor {valor}" if valido else "Vazia"
            print(f"Linha {linha}: {status}")
        print()
        
    def print_ram(self):
        print("RAM:")
        for address, value in self.ram.items():
            print(f"Endereço {address}: {value}")
        print()
        
    def buscar_endereco(self, address, novo_valor=None):
        print(f"Buscando endereço {address}...")
        
        linha_cache = address % self.cache_size
        tag = address // self.cache_size
        
        # cache hit?
        cache_tag, cache_valor, valido = self.cache[linha_cache]
        if valido and cache_tag == tag:
            print("Cache HIT!")
            if novo_valor is not None:
                print(f"Atualizando valor no endereço {address} para {novo_valor}")
                self.cache[linha_cache] = (tag, novo_valor, True)
                return novo_valor
            return cache_valor
        else:
            print("Cache MISS...")
            
            # se a linha estava ocupada, atualizo a ram
            if valido:
                endereco_ram = cache_tag * self.cache_size + linha_cache
                print(f"Atualizando RAM no endereço {endereco_ram} com valor {cache_valor}")
                self.ram[endereco_ram] = cache_valor
            
            # novo valor
            valor_ram = self.ram[address]
            print(f"Carregando valor {valor_ram} da RAM para a cache (linha {linha_cache})")
            self.cache[linha_cache] = (tag, valor_ram, True)
            
            if novo_valor is not None:
                print(f"Atualizando valor no endereço {address} para {novo_valor}")
                self.cache[linha_cache] = (tag, novo_valor, True)
                return novo_valor
            return valor_ram

print("=== Simulador de Cache com Mapeamento Direto ===")
# 4 linhas de cache, 16 endereços de ram
cm = CacheMapeamentoDireto(4, 16)

print("\nEstado inicial:")
cm.print_ram()
cm.print_cache()

print("\n=== Primeira busca (miss) ===")
cm.buscar_endereco(5)
cm.print_cache()

print("\n=== Segunda busca (miss) ===")
cm.buscar_endereco(0)
cm.print_cache()

print("\n=== Terceira busca (miss) ===")
cm.buscar_endereco(3)
cm.print_cache()

print("\n=== Busca no mesmo bloco (miss) ===")
cm.buscar_endereco(1, 10)
cm.print_cache()

print("\n=== Busca na mesma linha (hit) ===")
cm.buscar_endereco(5)
cm.print_cache()

print("\n=== Busca com atualização ===")
cm.buscar_endereco(5, 100)
cm.print_cache()

print("\n=== Busca que substitui linha da cache ===")
cm.buscar_endereco(1)
cm.print_cache()

print("\n=== Estado Final ===")
cm.print_ram()