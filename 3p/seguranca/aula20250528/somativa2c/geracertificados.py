import certLib as CERT

def exercicio1():
    print('Exercicio de certificados autoassinados')

    # GERA CERTIFICADO AUTOASSINADO DO SERVIDOR
    # openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout server.key -out server.crt -subj "/C=BR/ST=Parana/L=Curitiba/O=BCC/CN=server.bcc.com"
    chavePri, _ = CERT.geraChavePrivada(2048, 'server.key')
    chavePub, _ = CERT.geraChavePublica(chavePri)
    dn = {'cn':'server.bcc.com', 'o':'BCC', 'c':'BR', 's':'Parana', 'l':'Curitiba'} 
    CERT.geraAutoAssinado(chavePri, chavePub, dn, 'server.crt', ca=False) 

    # GERA CERTIFICADO AUTOASSINADO DO CLIENTE 1
    # openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout client.key -out client.crt -subj "/C=BR/ST=Parana/L=Curitiba/O=BCC/CN=Cliente ID1"
    chavePri, _ = CERT.geraChavePrivada(2048, 'client.key')
    chavePub, _ = CERT.geraChavePublica(chavePri)
    dn = {'cn':'CLIENTE ID1', 'o':'BCC', 'c':'BR', 's':'Parana', 'l':'Curitiba'} 
    CERT.geraAutoAssinado(chavePri, chavePub, dn, 'client.crt', ca=False)

    # GERA CERTIFICADO AUTOASSINADO DO CLIENTE 2
    # openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout client2.key -out client2.crt -subj "/C=BR/ST=Parana/L=Curitiba/O=BCC/CN=Cliente ID2"
    chavePri, _ = CERT.geraChavePrivada(2048, 'client2.key')
    chavePub, _ = CERT.geraChavePublica(chavePri)
    dn = {'cn':'CLIENTE ID2', 'o':'BCC', 'c':'BR', 's':'Parana', 'l':'Curitiba'} 
    CERT.geraAutoAssinado(chavePri, chavePub, dn, 'client2.crt', ca=False)

def exercicio2():

    print('Exercicio com uma CA PRIVADA')
    
    # GERA CERTIFICADO AUTOASSINADO DA CA
    # openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout bcc_CA.key -out bcc_CA.crt -subj "/C=US/O=Politecnica/CN=BCC Politecnica"
    chavePri, _ = CERT.geraChavePrivada(2048, 'bcc_CA.key')
    chavePub, _ = CERT.geraChavePublica(chavePri)
    dn = {'cn':'BCC Politecnica', 'o':'Politecnica', 'c':'BR', 's':'Parana', 'l':'Curitiba'} 
    CERT.geraAutoAssinado(chavePri, chavePub, dn, 'bcc_CA.crt', ca=True) 

    # GERA O CSR PARA O CLIENTE 1
    # openssl req -newkey rsa:2048 -days 365 -nodes -keyout client.key -out client.csr -subj "/C=BR/ST=Parana/L=Curitiba/O=BCC/CN=Cliente ID1"
    chavePri, _ = CERT.geraChavePrivada(2048, 'client.key')
    dn = {'cn':'Cliente ID1', 'o':'BCC', 'c':'BR', 's':'Parana', 'l':'Curitiba'} 
    CERT.geraCSR(chavePri, dn, 'client.csr')

    # GERA O CSR PARA O CLIENTE 2
    # openssl req -newkey rsa:2048 -days 365 -nodes -keyout client2.key -out client2.csr -subj "/C=BR/ST=Parana/L=Curitiba/O=BCC/CN=Cliente ID2"
    chavePri, _ = CERT.geraChavePrivada(2048, 'client2.key')
    dn = {'cn':'Cliente ID2', 'o':'BCC', 'c':'BR', 's':'Parana', 'l':'Curitiba'} 
    CERT.geraCSR(chavePri, dn, 'client2.csr')

    # GERA O CSR PARA O SERVIDOR
    # openssl req -newkey rsa:2048 -days 365 -nodes -keyout server.key -out server.csr -subj "/C=BR/ST=Parana/L=Curitiba/O=BCC/CN=server.bcc.com"
    chavePri, _ = CERT.geraChavePrivada(2048, 'server.key')
    dn = {'cn':'server.bcc.com', 'o':'BCC', 'c':'BR', 's':'Parana', 'l':'Curitiba'} 
    CERT.geraCSR(chavePri, dn, 'server.csr')

    # ASSINA O CERTIFICADO DO CLIENTE 1
    # openssl x509 -days 365 -req -in client.csr -CA bcc_CA.crt -CAkey bcc_CA.key -CAcreateserial -out client.crt
    csr = CERT.carregaCSR('client.csr')
    priCA = CERT.carregaChavePrivada('bcc_CA.key')
    certCA = CERT.carregaCertificado('bcc_CA.crt')
    CERT.assinaCSR(csr, certCA, priCA, 'client.crt')

    # ASSINA O CERTIFICADO DO CLIENTE 2
    #openssl x509 -days 365 -req -in client2.csr -CA bcc_CA.crt -CAkey bcc_CA.key -CAcreateserial -out client2.crt
    csr = CERT.carregaCSR('client2.csr')
    priCA = CERT.carregaChavePrivada('bcc_CA.key')
    certCA = CERT.carregaCertificado('bcc_CA.crt')
    CERT.assinaCSR(csr, certCA, priCA, 'client2.crt')

    # ASSINA O CERTIFICADO DO SERVIDOR
    #openssl x509 -days 365 -req -in server.csr -CA bcc_CA.crt -CAkey bcc_CA.key -CAcreateserial -out server.crt
    csr = CERT.carregaCSR('server.csr')
    priCA = CERT.carregaChavePrivada('bcc_CA.key')
    certCA = CERT.carregaCertificado('bcc_CA.crt')
    CERT.assinaCSR(csr, certCA, priCA, 'server.crt')