#!/bin/bash -e

rm -f /mount/src/sqlparse/extract_testcases/extracted-sqlparse-testcases.txt

cd /

git clone https://github.com/andialbrecht/sqlparse.git
cd sqlparse
git reset --hard 38c065b86ac43f76ffd319747e57096ed78bfa63
git apply /mount/src/sqlparse/extract_testcases/sqlparse.patch

pytest