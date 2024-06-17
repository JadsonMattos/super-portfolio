# Boas-vindas ao repositório do projeto Super Portfólio

<details>
<summary><strong>🧑‍💻 O que deverá ser desenvolvido</strong></summary><br />

Neste projeto, você vai praticar os seus conhecimentos em Django e Django Rest Framework. Você irá desenvolver uma API para gerenciamento de dados de perfil e projetos em um super portfólio. Vamos lá? 🤩

</details>

<details>
  <summary><strong>📝 Habilidades a serem trabalhadas</strong></summary><br />

Neste projeto, verificamos se você é capaz de:

- Utilizar o _Django REST Framework_ para criar endpoints com entidades aninhadas.
- Utilizar o módulo _Simple JWT_ para implementar autenticação no Django REST Framework.

</details>

# Orientações que você já conhece 😉

<details>

   <summary><strong>‼ Antes de começar a desenvolver </strong></summary><br />

1. Para conseguir instalar a dependência `mysqlclient` você precisa garantir a existência de algumas bibliotecas no seu sistema operacional:

- **Debian/Ubuntu**
```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
```

- **Mac**
```bash
brew install mysql pkg-config
```

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />

O Python oferece um recurso chamado de ambiente virtual, que permite sua máquina rodar sem conflitos diferentes tipos de projetos com diferentes versões de bibliotecas.

1. Criar o ambiente virtual

```bash
python3 -m venv .venv
```

2. Ativar o ambiente virtual

```bash
source .venv/bin/activate
```

3. Instalar as dependências no ambiente virtual

```bash
python3 -m pip install -r dev-requirements.txt
```

Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.

</details>

<details>
  <summary><strong>🏃🏾 Executando o Projeto</strong></summary>
    <br />
  Para a realização deste projeto, utilizaremos um banco de dados chamado `super_portfolio_database`. Já existe um script de criação do banco pronto no arquivo `database/01_create_database.sql` que será copiado para dentro do container. Não altere este script.

  Para rodar o MySQL via Docker execute os seguintes comandos na raiz do projeto:

  ```bash
  docker build -t super-portfolio-db .
  docker run -d -p 3306:3306 --name=super-portfolio-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=super_portfolio_database super-portfolio-db
  ```

  Esses comandos irão fazer o build da imagem e subir o container Docker.

  Lembre-se de que o MySQL utiliza por padrão a porta 3306. Se já houver outro serviço utilizando esta porta, considere desativá-lo ou mudar a porta no comando acima.

</details>

# Requisitos obrigatórios

Você é uma pessoa desenvolvedora fullstack que já desenvolveu vários projetos enquanto estudava um conjunto de tecnologias específicas. Agora, sua atenção será direcionada para entrar para o mercado de trabalho e para isso, apresentar um portfólio com todos os seus projetos é algo importantíssimo. Seu objetivo aqui será desenvolver este portfólio com seu perfil, projetos, links importantes do seu LinkedIn e disponibilizá-lo para visualização por meio do deploy via Railway.

A seguir está o escopo de cada tarefa que te levará a conclusão do seu Super Portfólio! 🤩

## 1 - Implemente a autenticação com simple JWT

> <b>🍀 Dica:</b> Antes de iniciar a implementação da autenticação, certifique-se de que tanto o container Docker com o banco de dados quanto o servidor estão rodando.

<br />

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>

- Implemente a autenticação com **Simple JWT** no projeto para que somente pessoas logadas possam ter acesso a aplicação.
- Use a rota `token/` para a obtenção do Token JWT.
- Use a rota `token/refresh/` para a atualização do Token JWT.
- Use a rota `token/verify/` para a verificação do Token JWT.

</details>

## 2 - Inicie o app `projects` e crie um C.R.U.D para `Profile`

Inicie um app com o nome `projects` e crie um **C.R.U.D.** para o model `Profile`. Para isso, você deve criar as rotas, views e serializers necessários para que seja possível realizar as operações de C.R.U.D. para a model `Profile`.

> <b>🍀 Dica:</b> Os requisitos seguintes exigirão a criação de modelos. Lembre-se que sempre que criar/modificar um modelo, é necessário criar as migrações para espelhar as modificações para os bancos de dados, inclusive o banco de testes contam com estas modificações. O comando para gerar a migration a partir dos modelos criados é:

</b>

```bash
python3 manage.py makemigrations
```

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>
  <br />
  <details>
    <summary>
      <b>✍️ Model Profile</b>
    </summary>

- Crie a classe `Profile`.
- A classe `Profile` deve herdar os `models` do Django.
- A classe `Profile` deve ter as propriedades: `name`, `github`, `linkedin`, e `bio`.
- A propriedade `name` deve ser um campo de caracteres com um tamanho máximo de **100 caracteres**.
- As propriedades `github`, `linkedin` devem ser campos de **URL**.
- A propriedade `bio` deve ser um campo de texto sem tamanho máximo definido.
- As propriedades devem ser:
  - `name`: Campo de caracteres, com tamanho máximo de **100 caracteres**.
  - `github`: Campo de **URL**.
  - `linkedin`: Campo de **URL**.
  - `bio`: Campo de texto, sem tamanho máximo definido.
- As propriedades `name`, `github`, `linkedin`, e `bio` não devem aceitar informações vazias ou maiores que 500 caracteres.
- O método `__str__` da classe `Profile` deve retornar a propriedade `name` do perfil criado.

  </details>

<details>
  <summary>
    <b>✍️ Rotas </b>
  </summary>

As operações do C.R.U.D. devem ser acessadas apor meio da rota: `profiles/`, a partir da URL base `http://localhost:8000/`. Em que:

- A rota `profiles` deve aceitar requisições do tipo `GET` e retornar uma lista com todos os perfis cadastrados.
- A rota `profiles/` deve aceitar requisições do tipo `POST` e criar um novo perfil com as informações passadas.
- A rota `profiles/<id_do_perfil>` deve aceitar requisições do tipo `GET` e retornar o perfil com o `id` especificado.
- A rota `profiles/<id_do_perfil>/` deve aceitar requisições do tipo `PATCH` e atualizar o perfil com o `id` especificado.
- A rota `profiles/<id_do_perfil>/` deve aceitar requisições do tipo `DELETE` e deletar o perfil com o `id` especificado.

</details>

</details>

## 3 - Crie um C.R.U.D para `Project`

Crie um **C.R.U.D.** para o model `Project`. Para isso, você deve criar as rotas, views e serializers necessários para que seja possível realizar as operações de C.R.U.D. para a model `Project`.

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>
  <br />
  <details>
    <summary>
      <b>✍️ Model Project</b>
    </summary>

- Crie a classe `Project`.
- A classe `Project` deve herdar os `models` do Django.
- A classe `Project` deve ter as propriedades: `name`, `description`, `github_url`, `keyword`, `key_skill` e `profile`.
- As propriedades `name`, `keywords` e `key_skill` devem ser campos de caracteres com um tamanho máximo de **50 caracteres**.
- A propriedade `description` deve ser um campo de texto com um tamanho máximo de **500 caracteres**.
- A propriedade `github_url` deve ser um campo de **URL**.
- A propriedade `profile` deve ser um campo de relacionamento com a classe `Profile`.
- As propriedades devem ser:
  - `name`: Campo de caracteres, com tamanho máximo de **50 caracteres**.
  - `description`: Campo de texto, , com tamanho máximo de **500 caracteres**.
  - `github_url`: Campo de **URL**.
  - `keyword`:  Campo de caracteres, com tamanho máximo de **50 caracteres**.
  - `key_skill`:  Campo de caracteres, com tamanho máximo de **50 caracteres**.
  - `profile`: Campo de chave estrangeira(_foreign key_) com a classe `Profile`.
- As propriedades `name`, `description`, `github_url`, `keywords` e `key_skills` não devem aceitar informações vazias ou maiores que 500 caracteres.
- O relacionamento presente em `profile` deve ser do tipo `1:N`, em que um perfil pode ter vários projetos.
- O método `__str__` da classe `Project` deve retornar a propriedade `name` do projeto criado.

> <b>🍀 Dicas:</b> Existe um tipo de campo específico pra URLs no Django. Para saber mais, acesse a [documentação](https://docs.djangoproject.com/en/3.2/ref/models/fields/#urlfield). 😉
  </details>

<details>
  <summary>
    <b>✍️ Rotas </b>
  </summary>

As operações do C.R.U.D. devem ser acessadas apor meio da rota: `projects/`, a partir da URL base `http://localhost:8000/`. Em que:

- As rotas `projects/` e `projects/<id_do_projeto>/` devem ser acessíveis apenas por pessoas usuárias autenticadas.
- A rota `projects/` deve aceitar requisições do tipo `GET` e retornar uma lista com todos os projetos cadastrados.
- A rota `projects/` deve aceitar requisições do tipo `POST` e criar um novo projeto com as informações passadas.
- A rota `projects/<id_do_projeto>/` deve aceitar requisições do tipo `GET` e retornar o projeto com o `id` especificado.
- A rota `projects/<id_do_projeto>/` deve aceitar requisições do tipo `PATCH` e atualizar o projeto com o `id` especificado.
- A rota `projects/<id_do_projeto>/` deve aceitar requisições do tipo `DELETE` e deletar o projeto com o `id` especificado.

</details>

</details>

## 4 - Customize as ViewSets para `Profile`

Customize a ViewSet de `Profile` para que as rotas do tipo `GET` possam ser acessadas sem a necessidade de autenticação, renderizando diretamente um template com todas as informações pertinentes ao invés de haver retorno da API.

> <b>🍀 Dica:</b> Há como definir uma função dentro de uma ViewSet que dá diferentes permissões de acesso para diferentes métodos HTTP conforme o tipo de requisição. No caso deste requisito, por exemplo, o método GET é permitido para qualquer pessoa, enquanto os outros métodos (POST, PATCH e DELETE) requerem autenticação. Desta forma, a função que faz a diferenciação de permissões de acesso deve ser definida dentro da ViewSet pode ser definida da seguinte forma:

</b>

```python
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]
```

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>

- Crie uma classe chamada `ProfileViewSet` em `projects/views.py`.
- Essa classe deve herdar de `ModelViewSet`.
- A classe `ProfileViewSet` deve ter uma função que exige autenticação a depender do método utilizado na requisição.
- As rotas do tipo `GET` podem ser acessadas sem a necessidade de autenticação, renderizando diretamente um template com todas as informações pertinentes.
- As rotas do tipo `POST`, `PATCH` e `DELETE` só podem ser acessadas por pessoas usuárias autenticadas.
- Utilize o método `retrieve` para exibir os detalhes de um perfil (_profile_), renderizando um template HTML com esses detalhes e informações relacionadas. Esse método deve verificar se a requisição é um `GET` e, se não for, chamar a implementação padrão de recuperação de detalhes usando `super().retrieve()`.
- Após recuperar o perfil, renderize um template HTML com o perfil. O template deve ser criado no caminho `projects/templates/profile_detail.html`.

> <b>🍀 Dica:</b> A função `retrieve` é chamada quando o Viewset recebe, entre outras possibilidades, a requisição `GET`. Customizando ela, conseguimos direcionar cada verbo HTTP para uma renderiza'ncção de dados diferente . Desta forma, você pode utilizar a função abaixo como base para desenvolver o que é solicitado:

</b>

```python
class ProfileViewSet(viewsets.ModelViewSet):
    # defina a queryset
    # defina a classe do serializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if request.method == 'GET':
          # busque o id do perfil
          # crie uma variável para guardar esse perfil

            return render(
              # passe os parâmetros necessários para o template:
              # a requisição, o caminho do template e um dict com dados para o template
            )
        return super().retrieve(request, *args, **kwargs)
```

</details>

## 5 - Crie um C.R.U.D inline para `Certificate` e `CertifyingInstitution`

Crie um **C.R.U.D.** inline para o model `Certificate` e `CertifyingInstitution`, para que em uma única requisição seja possível ver/criar as instituições certificadoras e seus respectivos certificados em uma única requisição. Para isso, você deve criar as rotas, views e serializers necessários para que seja possível realizar as operações de C.R.U.D. para as models `Certificate` e `CertifyingInstitution`.

> <b>🍀 Dica:</b> Para criar um C.R.U.D. inline, você deve herdar do `serializers.ModelSerializer` no serializer que conterá a outra entidade, para definir um atributo que contenha uma instância do serializer a ser contido. Neste momento você pode usar o argumento `(many=True)` para indicar que o campo de relacionamento representa vários objetos relacionados, ou seja, serializando várias certificações para uma instituição certificadora. Além disso, você deve sobrescrever a função `create` do serializer.

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>
  <br />
  <details>
    <summary>
      <b>✍️ Model CertifyingInstitution</b>
    </summary>

- Crie a classe `CertifyingInstitution`.
- A classe `CertifyingInstitution` deve herdar os `models` do Django.
- A classe `CertifyingInstitution` deve ter as propriedades: `name` e `url`.
- A propriedade `name` deve ser um campo de caracteres com um tamanho máximo de **100 caracteres**.
- A propriedade `url` deve ser um campo de **URL**.
- As propriedades `name` e `url` não devem aceitar informações vazias ou maiores que 500 caracteres.
- O método `__str__` da classe `CertifyingInstitution` deve retornar a propriedade `name` da instituição certificadora criada.

</details>

  <details>
    <summary>
      <b>✍️ Model Certificate</b>
    </summary>

- Crie a classe `Certificate`.
- A classe `Certificate` deve herdar os `models` do Django.
- A classe `Certificate` deve ter as propriedades: `name`, `certifying_institution`, `timestamp` e `profiles`.
- A propriedade `name` deve ser um campo de caracteres com um tamanho máximo de **100 caracteres**.
- A propriedade `certifying_institution` deve ser um campo de relacionamento de chave estrangeira com a classe `CertifyingInstitution`.
- A propriedade `timestamp` deve ser um campo de data e hora preenchido automaticamente no momento de sua criação.
- A propriedade `profiles` deve ser um campo de relacionamento do tipo `ManyToMany` com a classe `Profile` com o atributo `related_name` definido como `certificates`.
- As propriedades `name`, `certifying_institution`, `timestamp`, e `profiles` não devem aceitar informações vazias ou maiores que 500 caracteres.
- O método `__str__` da classe `Certificate` deve retornar a propriedade `name` do certificado criado.
  </details>

<details>
  <summary>
    <b>✍️ Rotas </b>
  </summary>

As operações do C.R.U.D. devem ser acessadas apor meio das rotas: `certificates/`, e `certifying-institutions/` a partir da URL base `http://localhost:8000/`. Em que:

- As rotas `certificates/` e `certificates/<id_do_certificado>/` devem ser acessíveis apenas por pessoas usuárias autenticadas.
- A rota `certificates/` deve aceitar requisições do tipo `GET` e retornar uma lista com todos os certificados cadastrados.
- A rota `certificates/` deve aceitar requisições do tipo `POST` e criar um novo certificado com as informações passadas.
- A rota `certificates/<id_do_certificado>/` deve aceitar requisições do tipo `GET` e retornar o certificado com o `id` especificado.
- A rota `certificates/<id_do_certificado>/` deve aceitar requisições do tipo `PATCH` e atualizar o certificado com o `id` especificado.
- A rota `certificates/<id_do_certificado>/` deve aceitar requisições do tipo `DELETE` e deletar o certificado com o `id` especificado.

- As rotas `certifying-institutions/` e `certifying-institutions/<id_da_instituição-certificadora>/` devem ser acessíveis apenas por pessoas usuárias autenticadas.
- A rota `certifying-institutions/` deve aceitar requisições do tipo `GET` e retornar uma lista com todas as instituições certificadoras cadastradas.
- A rota `certifying-institutions/` deve aceitar requisições do tipo `POST` e criar uma nova instituição certificadora com as informações passadas. Essa instituição deve conter pelo menos um certificado para ser criada.
- A rota `certifying-institutions/<id_da_instituição-certificadora>/` deve aceitar requisições do tipo `GET` e retornar a instituição certificadora com o `id` especificado.
- A rota `certifying-institutions/<id_da_instituição-certificadora>/` deve aceitar requisições do tipo `PATCH` e atualizar a instituição certificadora com o `id` especificado. **Não é necessário** que as atualizações possam ser inline também.
- A rota `certifying-institutions/<id_da_instituição-certificadora>/` deve aceitar requisições do tipo `DELETE` e deletar a instituição certificadora com o `id` especificado.

</details>

</details>

## 6 - Exibir uma página de perfil completa

O template de `Profile` deve ser atualizado para que seja possível visualizar todas as informações de um perfil, incluindo seus certificados e instituições certificadoras.

> <b>🍀 Dica:</b> Para que seja possível exibir também os certificados, você precisará alterar a função `retrieve`, nas views.

<details>
  <summary>
    <b>✍️ Detalhes do requisito</b>
  </summary>

- Ao acessar um perfil, deve ser possível visualizar os certificados e instituições certificadoras de um perfil.

</details>

# Requisito não avaliativo

## 7. Faça o deploy de seu projeto Django

Para que seu projeto esteja acessível e pronto para ser visualizado por pessoas de recrutamento, fazer deploy dele pode ser um grande diferencial. Lembre-se que sempre que precisar, você pode consultar o material sobre **deploy com Django** do curso. 😉
