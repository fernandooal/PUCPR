# a) Gere uma chave privada
openssl genrsa -out chaveprivada.pem 2048

# b) Gere um CSR
openssl req -new -key chaveprivada.pem -out csr.pem   

# a) e b) poderiam ser executados com o mesmo comando:
# openssl req -newkey rsa:2048 -nodes -keyout chaveprivada.pem -out csr.pem

# c) Mostre o conteúdo do CSR
openssl req -in csr.pem -text -verify -noout

# d) Verifique a validade do CSR
openssl req -in csr.pem -noout -verify -key chaveprivada.pem

# e) Crie um certificado auto assinado a partir do CSR
openssl x509 -in csr.pem -out cert.pem -req -signkey chaveprivada.pem -days 365

# f) Mostre o conteúdo do certificado auto assinado.
openssl x509 -noout -in cert.pem -text
