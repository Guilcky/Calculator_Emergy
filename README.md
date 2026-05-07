# 🌱 Sistema de Cálculo de Emergia

Sistema desenvolvido em Python para modelagem, simulação e análise de fluxos de emergia em sistemas complexos, utilizando conceitos de álgebra emergética e Inventário do Ciclo de Vida (LCI).

O projeto possui uma arquitetura modular e escalável, permitindo importar bases de dados ambientais, representar redes de processos interconectados, calcular emergia total e visualizar os resultados através de uma interface gráfica moderna.

---

# 🚀 Funcionalidades

## ✔ Gerenciamento de Dados LCI
- Importação de bases CSV
- Manipulação de matrizes ambientais
- Estruturação de dados de fluxo

## ✔ Simulador Emergético
- Cálculo de emergia total
- Redes de processos interconectados
- Aplicação da álgebra emergética
- Fluxos energéticos entre sistemas

## ✔ Interface Gráfica
- Interface moderna com CustomTkinter
- Dashboard interativo
- Visualização de redes
- Geração de relatórios

## ✔ Relatórios
- Exportação em PDF
- Sumário de emergia
- Informações analíticas

---

# 🛠 Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- NetworkX
- Matplotlib
- CustomTkinter
- ReportLab

---

# 📁 Estrutura do Projeto

```bash
emergia_system/
│
├── core/
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
├── data/
│   └── exemplo_lci.csv
│
├── main.py
└── requirements.txt
