class cache_simplificada:
    def __init__(self, cache_size, ram_size):
        self.cache_size = cache_size
        self.ram_size = ram_size
        
        self.cache = {}
        self.ram = {}
        
        self.populate_ram()
        
    def populate_ram(self):
        for i in range(self.ram_size):
            self.ram[i] = i
    
    def print_cache(self):
        print(f"Cache: {self.cache}")
        
    def print_ram(self):
        print(f"RAM: {self.ram}")
        
    def buscar_endereco(self, address, valor):
        print(f"Buscando endereço {address}...")
        
        nbr = int(address/self.cache_size)
        
        #cache vazia
        if(len(self.cache) == 0):
            print("Cache vazia")
            self.buscar_from_ram(nbr)
            self.atualizar_valor(address, valor)
            return
        
        nbc = int(next(iter(self.cache))/self.cache_size)
        
        if(nbr==nbc):#cache hit
            print("Cache HIT!")
            self.atualizar_valor(address, valor)
        else: #cache miss
            print("Cache MISS..")
            
            #1. atualizar RAM a partir da cache
            self.atualizar_ram(nbc)
            
            #2. limpar cache
            self.cache.clear()
            
            #3. buscar novo bloco para a cache
            self.buscar_from_ram(nbr)
            
            self.atualizar_valor(address, valor)
        
        return
        
    def atualizar_valor(self, address, valor):
        self.cache[address] = valor
        return
    
    def atualizar_ram(self, bloco):
        print("Atualizando RAM com dados da Cache..")
        
        for i in range(self.cache_size):
            self.ram[bloco*self.cache_size+i] = self.cache[bloco*self.cache_size+i]
        
        return
            
    def buscar_from_ram(self, bloco):
        print(f"Buscando bloco {bloco} na RAM...")
        
        for i in range(self.cache_size):
            self.cache[bloco*self.cache_size+i] = self.ram[bloco*self.cache_size+i]
        
        return
        
        
cs = cache_simplificada(3, 9)
cs.print_cache()
cs.print_ram()
print("-------------------------")
cs.buscar_endereco(3, 100)
cs.print_cache()
cs.print_ram()
print("-------------------------")
cs.buscar_endereco(4, 100)
cs.print_cache()
cs.print_ram()
print("-------------------------")
cs.buscar_endereco(0, 100)
cs.print_cache()
cs.print_ram()