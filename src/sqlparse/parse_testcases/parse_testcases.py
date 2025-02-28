#!/bin/env python3

import sqlparse
import pathlib

def run(input, output):
    with open(input, "rb") as f:
        content = f.read()
    queries = content.split(b"\n<end_of_query/>\n")[:-1]

    output = open(output, "w")

    for query in queries:
        query_str = query.decode('utf-8')
        output.write(query_str)
        output.write("\n<end_of_query/>\n")

        for (token_type, token_content) in sqlparse.lexer.tokenize(query_str):
            output.write(repr(token_type))
            output.write("\n")
            output.write(token_content)
            output.write("\n<end_of_token/>\n")

        output.write("\n<end_of_tokens/>\n")

    print(input, ": processed", len(queries), "queries")

    output.close()

if __name__ == '__main__':
    pathlib.Path('/mount/testdata/dialect_sqlparse').mkdir(parents=True, exist_ok=True) 

    run("/mount/src/sqlparse/extract_testcases/extracted-sqlparse-testcases.txt", "/mount/testdata/dialect_sqlparse/parsed-sqlparse-testcases.txt")
    run("/mount/src/sqlfluff/extract_testcases/extracted-sqlfluff-all-testcases.txt", "/mount/testdata/dialect_sqlparse/parsed-sqlfluff-all-testcases.txt")