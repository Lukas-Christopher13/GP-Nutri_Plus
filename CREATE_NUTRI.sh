#!/bin/bash

# Variáveis
DATABASE="/home/lukas/desenvolvimento/Nutri_plus/GP-Nutri_Plus/instance/project.db"

EMAIL="test@gmail.com"
FULL_NAME="nutricionista test"
BIRT_DATE="00/00/0000"
CNPJ="12345678901"
SENHA="teste123"


PASSWORD_HASH=$(python - <<END
from werkzeug.security import generate_password_hash

senha = "$SENHA"

hash_senha = generate_password_hash(senha)

print(hash_senha)

END
)

QUERY="INSERT INTO nutricionista (email, full_name, birt_date, cnpj, password_hash) VALUES ('$EMAIL', '$FULL_NAME', '$BIRT_DATE', '$CNPJ', '$PASSWORD_HASH');"

# Executar o comando SQL no banco de dados SQLite
sqlite3 $DATABASE "$QUERY"

echo "Usuário '$FULL_NAME' criado com sucesso no banco de dados '$DATABASE'."