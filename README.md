# path_sqlmaper
Replacing paths with a wildcard "*" so the sqlmap can inject it.

## EXAMPLE
```
❯ cat urls.txt
http://afine.com/id/2
http://afine.com/id/1
http://afine.com/another/path/here/

❯ cat urls.txt | path_sqlmaper
http://afine.com/*/2
http://afine.com/id/*
http://afine.com/*/1
http://afine.com/id/*
http://afine.com/*/path/here/
http://afine.com/another/*/here/
http://afine.com/another/path/*/
http://afine.com/another/path/here/*
```

## INSTALL
```
python3 -m pip install path-sqlmaper
echo 'alias path_sqlmaper=path_sqlmaper.py' >> "$HOME/.zshrc"
source "$HOME/.zshrc"
```

## USAGE
```
cat urls.txt | path-sqlmaper
```
