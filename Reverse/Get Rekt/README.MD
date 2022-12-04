# Get Rekt (1000)

```
Ох, кажется я вчера перебрал... Помню как сажусь за комп... Дальше всё в тумане. Проснулся, голова раскалывается, на экране строчка: 111019363f1a3022183905082c0d12321604. Похоже я что-то зашифровал. Прикладываю вам программу, осторожно, кажется это писал какой-то неадекват.
```
Программа находится [здесь](https://disk.yandex.ru/d/77Fr2lvSo8B74w)
<hr>
В таске дан py файл. Открываем его в pycharm и видим это:

![](images/cursed1.png)

pycharm ругается на большое количество говнокода. Нажав Alt + Enter и применив рекомендации pycharm'a получим более читаемый код. Доработаем руками и получим читаемый код:

```python
from binascii import hexlify

flag = "##################"
key = "ThisIsKey"
cipher = ""
i = 0
j = 0

while len(flag) - len(key) > len(key):
    key += key

while len(flag) - len(key) > 0:
    key += key[i]
    i += 1

while len(cipher) - len(key) < 0:
    cipher += chr((~ord(flag[j]) | ~ord(key[j])) & (ord(flag[j]) | ord(key[j])))
    j += 1

print(hexlify(cipher.encode()).decode())
```

Разберём его по блокам:
- Объявление переменных. Флаг длины 18, ключ 9.
```python
from binascii import hexlify

flag = "##################"
key = "ThisIsKey"
cipher = ""
i = 0
j = 0
```
- Добивание ключа до длины флага, путём повторения. Т.е. ключ для флага длины 18 будет таким: ThisIsKeyThisIsKey
```python
while len(flag) - len(key) > len(key):
    key += key
```
- Добивание ключа до длины флага, путём повторения. Т.е. ключ для флага длины 18 будет таким: ThisIsKeyThisIsKey
```python
while len(flag) - len(key) > len(key):
    key += key
while len(flag) - len(key) > 0:
    key += key[i]
    i += 1
```
- Блок шифрования:
```python
while len(cipher) - len(key) < 0:
    cipher += chr((~ord(flag[j]) | ~ord(key[j])) & (ord(flag[j]) | ord(key[j])))
    j += 1
```
Если посмотреть внимательно, то вот этот кусок кода выглядит как знакомая битовая операция:
```python
(~ord(flag[j]) | ~ord(key[j])) & (ord(flag[j]) | ord(key[j]))
```
Если взять flag[j] за A, а key[j] за B и записать это выражение более привычно, то становится всё понятно:
```
(¬A ∨ ¬B) ∧ (A ∨ B) = A ⊕ B
```
Т.к. этот скрипт реализует шифрование XOR, то можно попробовать подать вывод программы на вход (т.к. XOR - симметричный шифр). Запустим такой код и получим флаг:

```python
from binascii import hexlify

flag = "\x11\x10\x19\x36\x3f\x1a\x30\x22\x18\x39\x05\x08\x2c\x0d\x12\x32\x16\x04"
key = "ThisIsKey"
cipher = ""
i = 0
j = 0

while len(flag) - len(key) > len(key):
    key += key

while len(flag) - len(key) > 0:
    key += key[i]
    i += 1

while len(cipher) - len(key) < 0:
    cipher += chr((~ord(flag[j]) | ~ord(key[j])) & (ord(flag[j]) | ord(key[j])))
    j += 1

print(cipher)
```

**FLAG: ExpEvi{Gamma_Days}**
