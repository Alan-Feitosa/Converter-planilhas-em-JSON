PT-BR
# Processamento de Planilha com Pandas

## Descrição

Este projeto demonstra como utilizar a biblioteca `pandas` para manipulação e processamento de dados em uma planilha Excel. O objetivo é transformar os dados brutos de uma planilha Excel em um arquivo JSON formatado, realizando limpeza e ajustes específicos nos dados.

## Autor

Alan Feitosa

## Objetivo

Este script foi criado para demonstrar conhecimentos na utilização da biblioteca `pandas` para manipulação de dados, bem como para documentar o processo de transformação e limpeza de dados. O código pode servir como um exemplo para outras pessoas que necessitem realizar tarefas semelhantes.

## Dependências

Para executar o script, você precisa ter o `pandas` e `openpyxl` instalados. Se ainda não os tiver, instale-os usando pip:

```bash
pip install pandas openpyxl

EN-US
# Data Manipulation with Pandas

This project demonstrates knowledge of data manipulation using the Pandas library in Python. The main script reads data from an Excel file, processes it, and outputs the results to a JSON file. The script includes functionality for filtering data, rounding numeric values, and formatting output for different languages.

## Project Description

The script performs the following tasks:

1. **Load Excel Data**: Reads data from an Excel file.
2. **Remove Unnamed Columns**: Deletes columns with names containing 'Unnamed'.
3. **Drop Columns with All NaN Values**: Removes columns that have only NaN values.
4. **Filter Data**: Removes rows where the 'name' column is NaN or contains the description 'Descrição dos alimentos'.
5. **Format Numeric Values**: Rounds numeric values to 2 decimal places.
6. **JSON Conversion**: Converts the cleaned and formatted DataFrame to a JSON file with specific formatting.

## How to Use

1. **Install Required Packages**: Ensure you have the necessary Python packages installed:

   ```bash
   pip install pandas openpyxl