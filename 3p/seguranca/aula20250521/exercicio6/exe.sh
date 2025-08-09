# a) Gera um certificado auto assinado CA ROOT:
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout caprivada.pem -out cacert.pem -extensions v3_ca \
 -subj "/C=BR/ST=Parana/L=Curitiba/O=PUCPR/OU=Informatica/CN=www.pucpr.org"

# b) Gera um CSR para um servidor Web
openssl req -newkey rsa:2048 -nodes -keyout swebprivada.pem -out swebcsr.pem \
 -subj "/C=BR/ST=Parana/L=Curitiba/O=PUCPR/OU=Politecnica/CN=politecnica.pucpr.org"

# c) Assina o CSR com o certificado CA ROOT
openssl x509 -days 360 -req -in swebcsr.pem -CA cacert.pem -CAkey caprivada.pem -CAcreateserial -out swebcert.pem

# d) Verifica se o certificado do servidor Web foi assinado pela CA ROOT
openssl verify -verbose -CAfile cacert.pem swebcert.pem

# e) Imprime as seguintes informações do certificado:  Issuer, Subject e Validade
openssl x509 -noout -in swebcert.pem -issuer
openssl x509 -noout -in swebcert.pem -subject
openssl x509 -noout -in swebcert.pem -dates

# em uma linha só:
# openssl x509 -noout -in cert.pem -issuer -subject -dates

# f) Extrai a chave pública do certificado do servidor Web
openssl x509 -pubkey -noout -in swebcert.pem > swebpublica.pem

# g) Criptografa o segredo "Seu Nome" usando a chave pública do servidor Web
openssl pkeyutl -in teste.txt -out cripto.rsa -encrypt -pubin -inkey swebpublica.pem

# h) Descriptografa o segredo usando a chave privada do servidor Web
openssl pkeyutl -in cripto.rsa -out decripto.rec -decrypt -inkey swebprivada.pem