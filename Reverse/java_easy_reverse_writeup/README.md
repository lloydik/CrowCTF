# Java easy reverse (1000)

```
Программа вывела вот это

e7 f3 27 1a 2f 8d 6f c3 e7 31 f2 16 55 9b 54 44 12 3e 77 f7 ca fb ce 89 6 bf 

посмотрите файлик, вдруг поймёте его
```
<hr>
В таске дан jar файл. Открываем его в jd-gui.

![](images/jd1.png)

Из кода программы видно, что создаётся объект класса Random, у которого seed генерируется рандомно. Он не особо большой, так что можно перебрать это число. Для этого напишем такой скрипт:

```java
import java.util.Random;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    Random rand_seed = new Random();
    char[] flag = {0xe7, 0xf3, 0x27, 0x1a, 0x2f, 0x8d, 0x6f, 0xc3, 0xe7, 0x31, 0xf2, 0x16, 0x55, 0x9b, 0x54, 0x44, 0x12, 0x3e, 0x77, 0xf7, 0xca, 0xfb, 0xce, 0x89, 0x6, 0xbf}; // Строка из условия
    for(int seed = 0; seed < 4000000; ++seed)
    {
        Random rand = new Random(seed);
        //Дальше брутим сид. Если совпали первые 3 символа ключа, то мы нашли (скорее всего) seed
        if(rand.nextInt(256) == 162) // 162 = 0xe7^'E'
        {
            if(rand.nextInt(256) == 139) // 139 = 0xf3^'x'
            {
                if(rand.nextInt(256) == 87) // 87 = 0x27^'p'
                {
                    StringBuffer res = new StringBuffer();
                    for (int i = 3; i < flag.length; i++)
                      res.append(Integer.toHexString(flag[i] ^ rand.nextInt(256)) + " "); // Собираем и 
                    System.out.println(res); // Выводим флаг
                }
            }
        }
    }
  }
}
```

**FLAG: ExpEvi{J4v4_f1r5t_r3v3r53}**
