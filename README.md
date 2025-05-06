# 🛒 API de Vendas

API desenvolvida com Django e Django Rest Framework para controle de vendas, clientes, produtos e lojas. O projeto inclui documentação com Swagger, banco de dados PostgreSQL e ambiente isolado com Docker.

---

## 🔧 Tecnologias Utilizadas

- **Python 3.9**
- **Django 4+**
- **Django REST Framework**
- **PostgreSQL**
- **Docker e Docker Compose**
- **drf-yasg (Swagger Docs)**

---

## 🚀 Funcionalidades

- CRUD de **clientes**, **produtos**, **unidades de medida** e **lojas**
- Registro de **vendas com múltiplos itens**
- Geração de **gráficos e dashboards** interativos
- Documentação automática da API via **Swagger**
- Configuração completa via **Docker**

## 📁 Estrutura de Pastas
  api_django/
├── api_django/        # Projeto Django principal
│   ├── core/          # App principal da API (clientes, produtos, vendas...)
│   └── settings.py    # Configurações do Django
├── Dockerfile         # Configuração da imagem Docker
├── docker-compose.yml # Orquestração dos serviços
└── requirements.txt   # Dependências do projeto

## 📄 Endpoints Principais
| Verbo | Endpoint            | Descrição              |
| ----- | ------------------- | ---------------------- |
| GET   | /api/clientes/      | Lista de clientes      |
| POST  | /api/vendas/        | Criação de venda       |
| GET   | /swagger/           | Documentação Swagger   |
| GET   | /api/relatorios/... | Dashboards interativos |

## ✨ Autor
Desenvolvido por Italo Oliveira



