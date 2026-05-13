# 🌱 EmergyFlow — Sistema de Cálculo de Emergia

Sistema desenvolvido em Python para modelagem, simulação e análise de fluxos de emergia em sistemas complexos utilizando Inventários do Ciclo de Vida (LCI) e conceitos da álgebra emergética.

O projeto foi inspirado no software **SCALE (Software for CALculating Emergy based on Life Cycle Inventories)**, apresentado por Marvuglia et al. (2013), sendo desenvolvido como Atividade Prática Supervisionada (APS) da disciplina de Engenharia de Software.

---

# 🚀 Funcionalidades

## ✔ Importação de Dados LCI

* Importação de arquivos CSV
* Leitura automática de fluxos emergéticos
* Suporte a análise mensal
* Estruturação de matrizes ambientais

---

## ✔ Simulador Emergético

* Cálculo de emergia total
* Cálculo de emergia por processo
* Redes de processos interconectados
* Aplicação da álgebra emergética
* Fluxos energéticos entre sistemas

---

## ✔ Dashboard Interativo

* Interface moderna utilizando CustomTkinter
* Visualização gráfica da evolução emergética
* Comparação mensal dinâmica
* Indicadores analíticos em tempo real
* Layout responsivo e moderno

---

## ✔ Visualização de Redes

* Modelagem através de grafos direcionados
* Exibição visual de conexões entre processos
* Fluxos energéticos com pesos emergéticos

---

## ✔ Relatórios em PDF

* Exportação automática em PDF
* Salvamento automático na Área de Trabalho
* Tabelas analíticas
* Gráficos comparativos
* Fluxos emergéticos
* Resumo completo da análise

---

# 🖥️ Interface do Sistema

O sistema possui uma interface moderna inspirada em dashboards analíticos profissionais, contendo:

* Sidebar de navegação
* Cards estatísticos
* Gráficos mensais
* Distribuição dos processos
* Área analítica integrada
* Geração de relatórios

---

# 🛠 Tecnologias Utilizadas

| Tecnologia    | Função                |
| ------------- | --------------------- |
| Python        | Linguagem principal   |
| Pandas        | Manipulação de dados  |
| NumPy         | Operações matemáticas |
| NetworkX      | Modelagem de redes    |
| Matplotlib    | Geração de gráficos   |
| CustomTkinter | Interface gráfica     |
| ReportLab     | Geração de PDF        |

---

# 📁 Estrutura do Projeto

```bash
emergyflow/
│
├── core/
│   ├── config.py
│   ├── lci_manager.py
│   ├── emergy_calculator.py
│   └── network_model.py
│
├── gui/
│   ├── app.py
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
├── requirements.txt
└── README.md
```

---

# 📊 Exemplo de Arquivo CSV

```csv
month,source,target,value
Jan,Energia Solar,Agricultura,50
Jan,Água,Agricultura,30
Jan,Agricultura,Indústria,70

Fev,Energia Solar,Agricultura,180
Fev,Água,Agricultura,120
Fev,Agricultura,Indústria,240

Mar,Energia Solar,Agricultura,120
Mar,Água,Agricultura,80
Mar,Agricultura,Indústria,160
```

---

# ▶ Como Executar

## 1️⃣ Clone o Repositório

```bash
git clone https://github.com/Guilcky/Calculator_Emergy.git
```

---

## 2️⃣ Acesse a Pasta

```bash
cd Calculator_Emergy
```

---

## 3️⃣ Instale as Dependências

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Execute o Sistema

```bash
python main.py
```

---

# 📈 Funcionalidades Analíticas

O sistema permite:

* análise mensal de emergia;
* comparação temporal;
* cálculo de fluxos;
* visualização gráfica;
* exportação de relatórios;
* monitoramento de processos emergéticos.

---

# 🧪 Testes

O projeto inclui testes unitários para validação dos cálculos emergéticos.

Para executar:

```bash
python -m unittest discover tests
```

---

# 📚 Referências

MARVUGLIA, Antonino et al.
*SCALE: Software for CALculating Emergy based on Life Cycle Inventories.*
Ecological Modelling, v. 248, p. 80–91, 2013.

ARBAULT, Damien et al.
*Emergy evaluation using the calculation software SCALE.*
Science of the Total Environment, v. 472, p. 608–619, 2014.

VALYI, Raphaël; ORTEGA, Enrique.
*Emergy Simulator: An Open Source Simulation Platform Dedicated to Systems Ecology and Emergy Studies.*
UNICAMP, 2004.

---
---

# 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos.
