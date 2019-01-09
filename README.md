# Generate logins like a sir

Note that for now we support only `name`, `surname` and `patronymic` parameters

### Simple inline generator

```bash
python3 launcher.py 'prefix.{name}.{surname}' --name евгений --surname иванов петров smith
```
```
prefix.evgeniy.smith
prefix.evgeney.smith
prefix.evgeniy.petrov
prefix.evgeney.ivanov
prefix.evgeniy.ivanov
prefix.evgeney.evanov
prefix.evgeniy.evanov
prefix.evgeney.petrov
```

### Names in file

```bash
python3 launcher.py 'prefix.{name}.{surname}' --name-file names.txt --surname иванов петров smith
```

### Inline generator with indexation

```bash
python3 launcher.py 'prefix.{name[0]}.{surname}' --name евгений --surname иванов петров smith
```
```
prefix.e.ivanov
prefix.e.smith
prefix.e.evanov
prefix.e.petrov
```
