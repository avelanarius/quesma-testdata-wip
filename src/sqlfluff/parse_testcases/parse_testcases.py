#!/bin/env python3

from sqlfluff.core.parser import Lexer
import pathlib

def run(dialect, input, output):
    with open(input, "rb") as f:
        content = f.read()
    queries = content.split(b"\n<end_of_query/>\n")[:-1]

    output = open(output, "w")
    lexer = Lexer(dialect=dialect)

    error_count = 0

    for query in queries:
        query_str = query.decode('utf-8')

        segments, errors = lexer.lex(query_str)
        segments = list(segments)

        if errors:
            error_count += 1
            continue

        output.write(query_str)
        output.write("\n<end_of_query/>\n")

        for segment in segments:
            output.write(type(segment).__name__)
            output.write("\n")
            output.write(segment._raw)
            output.write("\n<end_of_token/>\n")

        output.write("\n<end_of_tokens/>\n")

    print(input, ": processed", len(queries), "queries;", error_count, "lex errors")

    output.close()

if __name__ == '__main__':
    pathlib.Path('/mount/testdata/dialects_sqlfluff').mkdir(parents=True, exist_ok=True) 

    run("ansi", "/mount/src/sqlfluff/extract_testcases/extracted-sqlfluff-ansi-testcases.txt", "/mount/testdata/dialects_sqlfluff/parsed-sqlfluff-ansi-testcases.txt")
    run("ansi", "/mount/src/sqlparse/extract_testcases/extracted-sqlparse-testcases.txt", "/mount/testdata/dialects_sqlfluff/parsed-sqlparse-testcases.txt")
