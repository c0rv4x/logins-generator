# Generate logins like a sir

Note that for now we support only `name`, `surname` and `patronymic` parameters

### Simple inline generator

```bash
python3 launcher.py --name евгений --surname иванов петров smith -- 'prefix.{name}.{surname}'
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
python3 launcher.py --name-file names.txt --surname иванов петров smith -- 'prefix.{name}.{surname}' 
```

### Inline generator with indexation

```bash
python3 launcher.py --name евгений --surname иванов петров smith -- 'prefix.{name[0]}.{surname}'
```
```
prefix.e.ivanov
prefix.e.smith
prefix.e.evanov
prefix.e.petrov
```

### Supply already formatted file with names, surnames and patronymics

```bash
> cat /tmp/1
< Иван::Петров@Николаевич
< Серьго::Бумеров@Павлович
```
```bash
python3 launcher.py --fullname-file /tmp/1 --fullname-format 'name::surname@patronymic' -- '{name[0]}{surname}'
```
```
ebumerov
spetrov
sbumerov
ipetrov
sboumerov
epetrov
eboumerov
ibumerov
iboumerov
```