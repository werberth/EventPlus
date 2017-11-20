# EventPlus
### Plataforma de anuncio de enventos desenvolvida para submissão no processo de seleção de estagio da MidiaCode

![EventPlus](https://image.ibb.co/hiwMoR/screen.png)


## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.6
3. Ative o virtualenv.
4. Instale as dependências

```console
git clone git@github.com:werberth/EventPlus.git eventplus
cd eventplus
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

5. Após intalar as dependencias, renomeie o arquivo ```exemple.env``` para ```.env```
e preencha o valor na variável ```SECRET_KEY```. (Entre no site [MiniWebtool](https://www.miniwebtool.com/django-secret-key-generator/), gere uma secrete key, copie e cole como valor da variavel.)

6. Caso queria utilizar o sqlite3, exclua a variável DATABASE_URL (```DATABASE_URL='postgres://username:password/db_name'```) do arquivo.

7. Caso queira utilizar o PostgreSQL substitua o valor ```username```, ```password``` e ```db_name``` na string da variável, pelo nome de usuario, senha  e nome do banco respectivamente.

8. Rode as migrações:
``` console
python manage.py migrate
```

9. Compile as traduções:
```console
python manage.py compilemessages
```

10. Feito, isso é só rodar os tests:

``` console
python manage.py test
```
