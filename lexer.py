# lexer_rust.py
# Lexer para subconjunto de Rust usando PLY

import ply.lex as lex

# Lista de tokens
tokens = (
    # Palabras reservadas
    'LET', 'MUT', 'FN', 'IF', 'ELSE', 'WHILE', 'RETURN',
    'TRUE', 'FALSE',
    
    # Tipos
    'I32', 'BOOL',
    
    # Identificadores y literales
    'IDENTIFIER', 'NUMBER',
    
    # Operadores
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN',
    'EQ', 'NEQ', 'LT', 'GT',
    
    # Delimitadores
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON', 'COMMA',
)

# Expresiones regulares simples para tokens
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_ASSIGN    = r'='
t_EQ        = r'=='
t_NEQ       = r'!='
t_LT        = r'<'
t_GT        = r'>'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_SEMICOLON = r';'
t_COMMA     = r','

# Palabras reservadas (diccionario para mapeo)
reserved = {
    'let': 'LET',
    'mut': 'MUT',
    'fn': 'FN',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'return': 'RETURN',
    'true': 'TRUE',
    'false': 'FALSE',
    'i32': 'I32',
    'bool': 'BOOL',
}

# Identificador: letra seguida de letras/números/guiones bajos
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Verifica si es palabra reservada
    return t

# Números enteros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios y tabs
t_ignore = ' \t'

# Ignorar comentarios de línea (// ...)
def t_COMMENT(t):
    r'//.*'
    pass  # Ignorar el comentario

# Manejo de nuevas líneas (para contar líneas)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Error léxico en línea {t.lexer.lineno}: Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Función de prueba
def test_lexer(data):
    lexer.input(data)
    print(f"{'Token':<15} {'Valor':<15} {'Línea'}")
    print("-" * 40)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(f"{tok.type:<15} {str(tok.value):<15} {tok.lineno}")

# Ejemplo de uso
if __name__ == '__main__':
    codigo_prueba = '''
    fn main() {
        let mut x: i32 = 10;
        let y = 5;
        
        if x > y {
            x = x + 1;
        } else {
            return false;
        }
        
        while x < 100 {
            x = x * 2;
        }
    }
    '''
    
    test_lexer(codigo_prueba)
