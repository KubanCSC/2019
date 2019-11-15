Title:

What happened in MFT stays in MFT

Description:

We got hacker's usb flash. We tried to find some intresting accesses, but we didn't find anything suspicious. Can you help us? 

Solution:

Файл которы й нас интересует acc.txt, но в нем нет ничего интересного
```
google 0912i4FASSf992
proton (S*DGdjlksld08324
proton *(SDu8godsdll
facebook fsd98ugasdASLF
```

Можно предположить что хакер просто стер из файла данные. Учитывая что размер файла очень маленький, то его данные полностью хранятся в его MFT-записи.
Соответственно если в файле что то было написано, а потом удалено, то стертые данные просто остались в slackspace $DATA атрибута MFT-записи.

![](https://github.com/KubanCSC/2019/blob/master/writeups/4N6/100test.png)

Flag: flag{SDS*GUDs9&&aasd#}
