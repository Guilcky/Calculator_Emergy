# 🌱 EmergyFlow — Sistema de Cálculo de Emergia

Sistema desenvolvido em Python para modelagem, simulação e análise de fluxos de emergia em sistemas complexos, inspirado no software SCALE apresentado no artigo:

> *SCALE: Software for CALculating Emergy based on Life Cycle Inventories* — Marvuglia et al. (2013)

O projeto aplica conceitos de Engenharia de Software, sustentabilidade e álgebra emergética para realizar cálculos ambientais utilizando bases de dados de Inventário do Ciclo de Vida (LCI).

---

# 📌 Objetivo do Projeto

O EmergyFlow foi desenvolvido como parte de uma APS (Atividade Prática Supervisionada), com foco em:

- Desenvolvimento de sistemas complexos
- Aplicação de boas práticas de Engenharia de Software
- Modelagem de redes ambientais
- Simulação de fluxos de emergia
- Visualização gráfica de dados ambientais
- Geração automatizada de relatórios

---

# 🚀 Funcionalidades

## ✔ Gerenciamento de Dados LCI

- Importação de arquivos CSV
- Estruturação de fluxos ambientais
- Manipulação de matrizes de Inventário do Ciclo de Vida
- Integração com redes de processos

---

## ✔ Simulador Emergético

- Cálculo da emergia total
- Cálculo da emergia por processo
- Redes de processos interconectados
- Aplicação da álgebra emergética
- Fluxos energéticos entre sistemas

---

## ✔ Dashboard Interativo

- Interface moderna em Dark Mode
- Visualização em tempo real
- Cards analíticos
- Indicadores emergéticos
- Evolução histórica da emergia

---

## ✔ Visualização Gráfica

- Gráfico de evolução da emergia
- Distribuição dos processos
- Visualização da rede emergética
- Fluxos entre processos

---

## ✔ Relatórios em PDF

- Exportação automática em PDF
- Sumário emergético
- Informações analíticas
- Gráficos integrados
- Rede de fluxos
- Salvamento automático na Área de Trabalho

---

# 🖥 Interface do Sistema

O sistema possui um dashboard moderno inspirado em aplicações profissionais de análise de dados.

### Recursos visuais:

- Sidebar interativa
- Cards analíticos
- Gráficos dinâmicos
- Tema escuro profissional
- Visual responsivo

---

# 🛠 Tecnologias Utilizadas

## Linguagem

- Python 3

## Bibliotecas

- Pandas
- NumPy
- NetworkX
- Matplotlib
- CustomTkinter
- ReportLab

---

# 📁 Estrutura do Projeto

```bash
emergy_system/
│
├── core/
│   ├── config.py
│   ├── lci_manager.py
│   ├── emergy_calculator.py
│   └── network_model.py
│
├── gui/
│   ├── app.py
│   ├── dashboard.py
│   └── styles.py
│
├── reports/
│   └── report_generator.py
│
├── tests/
│   └── test_emergy.py
│
├── data/
│   └── exemplo_lci.csv
│
├── main.py
│
└── requirements.txt
```

---

# ⚙ Como Executar o Projeto

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/emergyflow.git
```

---

## 2️⃣ Acesse a pasta

```bash
cd emergyflow
```

---

## 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Execute o sistema

```bash
python main.py
```

---

# 📄 Formato do CSV

O sistema utiliza arquivos `.csv` contendo:

```csv
source,target,value
Solar,Agricultura,150
Agricultura,Indústria,200
Indústria,Consumo,300
```

| Coluna | Descrição |
|---|---|
| source | Processo de origem |
| target | Processo de destino |
| value | Valor do fluxo emergético |

---

# 📊 Exemplo de Fluxo Emergético

```text
Solar → Agricultura → Indústria → Consumo
```

Cada conexão representa um fluxo de emergia entre processos do sistema.

---

# 🧠 Conceitos Aplicados

O projeto utiliza conceitos de:

- Engenharia de Software
- Redes Complexas
- Sistemas Ambientais
- Inventário do Ciclo de Vida (LCI)
- Álgebra Emergética
- Modelagem de Sistemas
- Sustentabilidade Computacional

---

# 🧪 Testes Automatizados

O sistema possui testes unitários utilizando:

```python
unittest
```

Executar testes:

```bash
python -m unittest
```

---

---


# 📚 Referência Acadêmica

MARVUGLIA, A.; BENETTO, E.; REGE, S.; JURY, C.  
**SCALE: Software for CALculating Emergy based on Life Cycle Inventories**.  
Ecological Modelling, 2013.

---

# 📜 Licença

Este projeto possui finalidade acadêmica e educacional.
