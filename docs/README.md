![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/django-4.2+-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
<img src="https://komarev.com/ghpvc/?username=deh0&label=%20Views&color=0e75b6&style=flat" alt="deh0">

## Plataforma SaaS Multi-Tenant Demo

Plataforma completa de e-commerce com ERP integrado, desenvolvida para pequenas e médias empresas que precisam de um site com gateway de pagamento, logística de entrega e emissão de notas fiscais em um só lugar, junto com o sistema de gestão completo.

## Sobre o projeto

Solução multi-tenant monorepo construída com Django, que permite utilizar uma versão para armazenar múltiplas empresas ao mesmo tempo e no mesmo projeto, com o mesmo banco de dados, mas que compartilham schemas diferentes. Isso permite que cada empresa tenha o seu próprio esquema e suas próprias configurações, garantindo total segurança e independência entre as empresas. O projeto é organizado como monorepo com dois subprojetos Django: o e-commerce e o ERP, que se comunicam através de uma API Core central.

## Stack

* Back-end: Django (Python), Django REST Framework e django_tenants.
* Front-end: React, HTML, CSS e JavaScript.
* Banco de dados: PostgreSQL com separação por schemas.
* Autenticação: Sessão Django + JWT.
* Conteinerização: Docker + Docker Compose.
* Infraestrutura: Digital Ocean.
* APIs Externas: Mercado Pago, Focus NF-e e Correios.

## Funcionalidade principais

* E-commerce completo com carrinho, checkout e rastreio de pedidos.
* ERP com gestão em vendas, estoque, produção, financeiro e clientes.
* Emissão automática de NF-e.
* Sistema de notificações e e-mails transacionais.
* Painel de métricas e dashboard por tenant. 

## Status 

Este repositório é a versão demo pública. O projeto em produção está em desenvolvimento ativo.
