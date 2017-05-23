
Basic logging of system memory usage on a <b>Microsoft Windows machine</b>    

## To run: 
```
git clone https://github.com/snolan1/windows_log_system_memory.git
cd windows_log_system_memory
python windows_log_system_memory_use.py
```
   
No external dependencies other than python (2 or 3)    

<b>Tested on: Windows Server 2012 R2, Windows 7, Windows 10</b>    


#### Example output

```
****[23 May 2017 - 10:51:22]****
starting

****[23 May 2017 - 10:51:22]****
Total Physical Memory:     16,327 MB
Available Physical Memory: 4,404 MB
Virtual Memory: Max Size:  32,652 MB
Virtual Memory: Available: 20,045 MB
Virtual Memory: In Use:    12,607 MB

****[23 May 2017 - 10:51:40]****
Total Physical Memory:     16,327 MB
Available Physical Memory: 4,330 MB
Virtual Memory: Max Size:
32,652 MB
Virtual Memory: Available:
19,974 MB
Virtual Memory: In Use:
12,678 MB

...
...
...
```
