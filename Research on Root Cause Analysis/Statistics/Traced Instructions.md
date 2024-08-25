	# Table for traced instructions to total instructions

| program                      | method    | traced_instructions | total_instructions | percentage |
| ---------------------------- | --------- | ------------------- | ------------------ | ---------- |
| test                         |           | 61                  | 392                | 15.5%      |
| readelf                      |           | 6359                | 57471              | 11.06%     |
| mruby integer overflow       | LOC       | 8584                | 40000              | 21%        |
|                              | LOC-DEBUG | 7120                | 41181              | 17%        |
|                              | BB        | 2868                | 41325              |            |
| lua                          | LOC       | 2710                | 12690              |            |
|                              | LOC-DEBUG | 2180                | 12408              |            |
|                              | BB        | 919                 | 12837              |            |
| nm                           | LOC       | 1487                | 5450               |            |
|                              | LOC-DEBUG | 1185                | 5450               |            |
|                              | BB        | 653                 | 5386               |            |
| libzip                       | LOC       | 993                 | 3883               |            |
|                              | LOC-DEBUG | 974                 | 3950               |            |
|                              | BB        | 451                 | 4373               |            |
| matio                        | LOC       | 125                 | 455                |            |
|                              | LOC-DEBUG | 88                  | 455                |            |
|                              | BB        | 58                  | 455                |            |
| sleuthkit                    | LOC       |                     |                    |            |
|                              | LOC-DEBUG |                     |                    |            |
|                              | BB        |                     |                    |            |
| mruby unintialized variable  | LOC       |                     |                    |            |
|                              | LOC-DEBUG |                     |                    |            |
|                              | BB        |                     |                    |            |
| mruby heap buffer overflow   | LOC       | 6810                | 32455              |            |
|                              | LOC-DEBUG | 5210                | 31283              |            |
|                              | BB        | 2535                | 38139              |            |
| screen                       | LOC       |                     |                    |            |
|                              | LOC-DEBUG |                     |                    |            |
|                              | BB        |                     |                    |            |
| libpng                       | LOC       | 1413                | 5873               |            |
|                              | LOC-DEBUG | 1302                | 6218               |            |
|                              | BB        | 349                 | 3228               |            |
| libjpeg                      | LOC       | 291                 | 708                |            |
|                              | LOC-DEBUG | 230                 | 832                |            |
|                              | BB        | 136                 | 1067               |            |
| libjpeg heap buffer overflow | LOC       | 165                 | 622                |            |
|                              | LOC-DEBUG | 135                 | 584                |            |
|                              | BB        | 139                 | 1020               |            |
|                              |           |                     |                    |            |
|                              |           |                     |                    |            |
|                              |           |                     |                    |            |
# Table for tracing time
**BB**: Basic Block
**LOC**: Line of Code
**LOC-DEBUG**: Line of Code with Debug symbols


| No  | ID                | program                      | tracing time(h:m) | method    | crash exploration time/files (h:m) | #Predicates                                           | #SLOC | rca time (h:m) | hit count        |
| --- | ----------------- | ---------------------------- | ----------------- | --------- | ---------------------------------- | ----------------------------------------------------- | ----- | -------------- | ---------------- |
| 1   | Hackerone #186041 |                              |                   |           |                                    |                                                       |       |                |                  |
|     |                   | mruby                        | 0:35              | aurora    | 0:08/2070                          | 97                                                    | 40    |                |                  |
|     |                   |                              | 0:3               | LOC       |                                    | 31                                                    | 26    |                |                  |
|     |                   |                              | 0:3               | LOC-DEBUG |                                    | 31                                                    | 27    |                |                  |
|     |                   |                              | 0:2.8             | BB        |                                    | 28                                                    | 26    |                |                  |
| 2   | CVE-2016-5636     | python                       | 1:02              | aurora    | 0:23/919                           | 290                                                   | 188   | 0:4            |                  |
|     |                   | python                       | 0:27              | LOC       |                                    | 184                                                   | 149   | 0:2            |                  |
|     |                   | python                       | 0:20              | LOC-DEBUG |                                    | 157                                                   | 136   | 0:1.20         |                  |
|     |                   | python                       | 0:12              | BB        |                                    | 194                                                   | 104   | 0:0.3          |                  |
| 3   | CVE-2019-9077     | readelf                      | 0:5               | aurora    | 0:41/2559                          | 4                                                     | 2     | 0:2            |                  |
|     |                   | readelf                      | 0:3               | LOC       |                                    | 2                                                     | 2     | 0.46           |                  |
|     |                   | readelf                      | 0:3               | LOC-DEBUG |                                    | 4                                                     | 1     | 0.28           |                  |
|     |                   | readelf                      | 0:2               | BB        |                                    | 1                                                     | 1     | 0.22           |                  |
| 4   | CVE-2018-10191    | mruby integer overflow       | 0:6               | BB        | 0:25/1607                          | 5/ off root cause by 4 lines                          | 3     |                |                  |
|     |                   |                              | 0:12              | LOC       | 0:25/1607                          | 10                                                    | 8     |                |                  |
|     |                   |                              | 0:20              | aurora    | 0:3/749                            | 1 / off root cause by 36 lines                        | 1     | 0:1            |                  |
|     |                   |                              | 0:5               | LOC       |                                    |                                                       | 1     |                |                  |
|     |                   |                              | 0:5               | LOC-DEBUG |                                    | 13/Off root cause by 35 lines                         | 11    |                |                  |
|     |                   |                              | 0:3               | BB        |                                    | 5/Off root case by 43                                 | 4     |                |                  |
| 5   | bug #5.0-2        | lua                          | 0:5               | aurora    | 0:15/1007                          | 63                                                    |       |                |                  |
|     |                   | lua                          | 0:1,40            | LOC       |                                    | 24                                                    |       |                |                  |
|     |                   | lua                          | 0:1,29            | LOC-DEBUG |                                    | 20                                                    |       |                |                  |
|     |                   | lua                          | 0:1               | BB        |                                    | 10                                                    |       |                |                  |
|     |                   |                              | 0:11              | aurora    | 0:40/2244                          | 20                                                    | 9     | 0:3            |                  |
|     |                   |                              | 0:3               | LOC       |                                    | 7                                                     | 7     | 0:0.40         |                  |
|     |                   |                              | 0:3               | LOC-DEBUG |                                    | 7                                                     | 7     | 0:0.30         |                  |
|     |                   |                              | 0:2               | BB        |                                    | 5                                                     | 5     | 0:0.14         |                  |
| 6   | Bugzilla-21670    | nm                           | 0:0.34            | aurora    | 0:19.34/297                        | 1                                                     | 1     |                |                  |
|     |                   | nm                           | 0:0.21            | LOC       | 0:33/291                           | 2                                                     | 2     |                |                  |
|     |                   | nm                           | 0:0.33            | aurora    |                                    | 1                                                     | 1     |                |                  |
|     |                   | nm                           | 0:0.20            | LOC-DEBUG |                                    | 4                                                     | 4     |                |                  |
|     |                   | nm                           | 0:0.15            | BB        |                                    | 4                                                     | 4     |                |                  |
| 7   | CVE-2017-12858    | libzip                       | 0:2               | aurora    | 0:23/327                           | 6                                                     | 4     |                | zip_dirent.c:581 |
|     |                   |                              | 0:0.47            | LOC       |                                    | 4                                                     | 4     |                |                  |
|     |                   |                              | 0:0.44            | LOC-DEBUG |                                    | 3                                                     | 3     |                |                  |
|     |                   |                              | 0:0.20            | BB        |                                    | 5                                                     | 4     |                |                  |
| 8   | CVE-2020-19497    | matio                        | 0:0.5             | aurora    | 0:23/97                            | 2                                                     | 2     |                |                  |
|     |                   |                              | 0:0.38            | LOC       |                                    | 1                                                     | 1     |                |                  |
|     |                   |                              | 0:0.39            | LOC-DEBUG |                                    | 1                                                     | 1     |                |                  |
|     |                   |                              | 0:0.36            | BB        |                                    | 1 (off by three lines?)                               | 1     |                |                  |
|     |                   |                              | 0:0.6             | aurora    | 1:15/119                           | 2                                                     | 2     |                |                  |
|     |                   |                              | 0:0.4             | LOC       |                                    | 1                                                     | 1     |                |                  |
|     |                   |                              | 0:0.38            | LOC-DEBUG |                                    | 1                                                     | 1     |                |                  |
|     |                   |                              | 0:0.36            | BB        |                                    | 1 (off by three lines)                                | 1     |                |                  |
| 9   | issue-905         | sleuthkit                    | 0:1.58            | aurora    |                                    | 9                                                     | 5     |                | ext2fs:807       |
|     |                   |                              | 0:0.56            | LOC       |                                    | 5                                                     | 5     |                |                  |
|     |                   |                              | 0:0.49            | LOC-DEBUG |                                    | 4                                                     | 4     |                |                  |
|     |                   |                              | 0:0.49            | BB        |                                    | 26 (off by 4 lines) or 4 (pinpoint inside a for loop) | 29    |                |                  |
| 10  | issue-3947        | mruby unintialized variable  | 0:31              | aurora    | 0:23/1107                          | 2                                                     | 2     | 0:3            |                  |
|     |                   |                              | 0:9               | LOC       |                                    | 1                                                     | 1     | 0:1            |                  |
|     |                   |                              | 0:10              | LOC-DEBUG |                                    | 3                                                     | 3     | 0:1.30         |                  |
|     |                   |                              | 0:4               | BB        |                                    | 1                                                     | 1     | 0:1.15         |                  |
| 11  | CVE-2018-12248    | mruby heap buffer overflow   | 0:13              | aurora    | 0:1/536                            | 1                                                     | 1     |                |                  |
|     |                   |                              | 0:3               | LOC       |                                    | 2 (off by 1 line)                                     | 2     |                |                  |
|     |                   |                              | 0:3               | LOC-DEBUG |                                    | 1                                                     | 1     |                |                  |
|     |                   |                              | 0:1.30            | BB        |                                    | 4 (off by 1)                                          | 3     |                |                  |
| 12  | CVE-2018-13785    | libpng                       | 0:0.17            | aurora    | 0:33/241                           | 4                                                     | 3     |                |                  |
|     |                   |                              | 0:0.10            | LOC       |                                    | 2                                                     | 2     |                |                  |
|     |                   |                              | 0:0.10            | LOC-DEBUG |                                    | 3                                                     | 3     |                |                  |
|     |                   |                              | 0.9               | BB        |                                    | 2                                                     | 2     |                |                  |
| 13  |                   | libjpeg divide by zero       | 0:0.12            | aurora    | 0:25/268                           | 2                                                     | 2     |                |                  |
|     |                   |                              | 0:0.10            | LOC       |                                    | 1                                                     | 1     |                |                  |
|     |                   |                              | 0:0.10            | LOC-DEBUG |                                    | 1                                                     | 1     |                |                  |
|     |                   |                              | 0:0.9             | BB        |                                    | 1 (off by 7 lines) predicate at rdgic.c:454           | 1     |                |                  |
| 14  |                   | libjpeg heap buffer overflow | 0:0.4             | aurora    |                                    | 1                                                     | 1     |                |                  |
|     |                   |                              | 0:0.3             | LOC       |                                    | 1                                                     | 1     |                |                  |
|     |                   |                              | 0:0.3             | LOC-DEBUG |                                    | 1                                                     | 1     |                |                  |
|     |                   |                              |                   | BB        |                                    | 1 (off by 2 lines) predicate at rdbmp.c:207           | 1     |                |                  |
| 15  |                   | mruby use after free         |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
| 16  |                   | tcpdump                      |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
| 17  |                   | bash                         |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
| 18  |                   | patch                        |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
| 19  |                   | nasm                         |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
| 20  |                   | libtiff heap buffer overflow |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
| 21  |                   | libsixel                     |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
|     |                   |                              |                   |           |                                    |                                                       |       |                |                  |
| 22  |                   | nm integer overflow          |                   |           |                                    |                                                       |       |                |                  |

Increase  in instructions if include all jump is 15 - 22%
Increase in speed x2~x4
Better predicate ranking
Aurora - LOC - BB

