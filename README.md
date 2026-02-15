# Lexer para Subconjunto de Rust

Este proyecto implementa un **Analizador Léxico (Lexer)** desarrollado en Python para un subconjunto específico del lenguaje **Rust**, utilizando la librería **PLY (Python Lex-Yacc)**.

---

## 1. Metacompilador Seleccionado: PLY
**PLY** es una implementación en Python de las herramientas clásicas Lex (análisis léxico) y Yacc (análisis sintáctico). 

* **¿Por qué PLY?** Es simple, no requiere fases de compilación separadas y permite escribir toda la lógica en Python puro.
* **Instalación:**
    ```bash
    pip install ply
    ```

---

## 2. Lenguaje L Definido
El lexer reconoce un subconjunto de Rust que incluye los siguientes elementos:

* **Declaraciones:** `let`, `mut`
* **Funciones:** `fn`
* **Control:** `if`, `else`, `while`, `return`
* **Tipos:** `i32`, `bool`
* **Literales:** Números enteros, `true`, `false`
* **Operadores:** `+`, `-`, `*`, `/`, `=`, `==`, `!=`, `<`, `>`
* **Delimitadores:** `(`, `)`, `{`, `}`, `;`, `,`

---

## 3. Implementación del Lexer
El lexer descompone el código fuente en los siguientes tokens principales:

| Token | Expresión Regular | Descripción |
| :--- | :--- | :--- |
| **IDENTIFIER** | `[a-zA-Z_][a-zA-Z_0-9]*` | Nombres de variables y funciones. |
| **NUMBER** | `\d+` | Números enteros. |
| **OPERATORS** | `\+`, `-`, `\*`, `/`, `==`, `!=`, `<`, `>` | Operaciones matemáticas y lógicas. |
| **KEYWORDS** | `let`, `fn`, `if`, `while`, etc. | Palabras reservadas del lenguaje. |

### Ejecución
Para procesar un archivo o cadena de texto, ejecuta:
```bash
python lexer.py
```
---
## 4. Estructura del Proyecto
```
Lexer_Rust/
├── lexer_rust.py      # Código fuente del lexer (PLY)
├── README.md          # Documentación del proyecto
```
---
## 5. Como Usar
1. Instalar PLY: pip install ply
2. Ejecutar: python lexer_rust.py
3. Pruebas: Puedes modificar la variable codigo_prueba dentro del script lexer.py para probar diferentes estructuras de código Rust.

