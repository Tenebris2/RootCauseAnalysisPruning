# Table for traced instructions to total instructions

| program | traced_instructions | total_instructions | percentage |
| ------- | ------------------- | ------------------ | ---------- |
| test    | 61                  | 392                | 15.5%      |
| readelf | 6359                | 57471              | 11.06%     |
|         |                     |                    |            |
|         |                     |                    |            |
# Table for tracing time
**BB**: Basic Block
**LOC**: Line of Code
**LOC-DEBUG**: Line of Code with Debug symbols


| No  | ID                | program                     | tracing time(h:m) | method    | crash exploration time/files (h:m) | predicate ranking                                     | line ranking | rca time (h:m) | Root cause       |
| --- | ----------------- | --------------------------- | ----------------- | --------- | ---------------------------------- | ----------------------------------------------------- | ------------ | -------------- | ---------------- |
| 1   | Hackerone #186041 |                             |                   |           |                                    |                                                       |              |                |                  |
|     |                   | mruby                       | 0:35              | aurora    | 0:08/2070                          | 97                                                    | 40           |                |                  |
|     |                   |                             | 0:3               | LOC       |                                    | 31                                                    | 26           |                |                  |
|     |                   |                             | 0:3               | LOC-DEBUG |                                    | 31                                                    | 27           |                |                  |
|     |                   |                             | 0:2.8             | BB        |                                    | 28                                                    | 26           |                |                  |
| 2   | CVE-2016-5636     | python                      | 1:02              | aurora    | 0:23/919                           | 290                                                   | 188          | 0:4            |                  |
|     |                   | python                      | 0:27              | LOC       |                                    | 184                                                   | 149          | 0:2            |                  |
|     |                   | python                      | 0:20              | LOC-DEBUG |                                    | 157                                                   | 136          | 0:1.20         |                  |
|     |                   | python                      | 0:12              | BB        |                                    | 194                                                   | 104          | 0:0.3          |                  |
|     |                   | python                      | 0:15              | LOC-DEBUG | 0:20/825                           | 157                                                   |              |                |                  |
|     |                   | python                      | 0:13              | BB        | 0:20/826                           | 177                                                   |              |                |                  |
| 3   | CVE-2019-9077     | readelf                     | 0:1               | LOC-DEBUG | 0:03/853                           | 1                                                     |              |                |                  |
|     |                   | readelf                     | 0:1               | LOC       |                                    | 2                                                     |              |                |                  |
|     |                   | readelf                     | 0:2               | aurora    |                                    | 4                                                     |              |                |                  |
|     |                   | readelf                     | 0:1               | BB        |                                    | 1                                                     |              |                |                  |
| 4   | CVE-2018-10191    | mruby integer overflow      | 0:6               | BB        | 0:25/1607                          | 5/ off root cause by 4 lines                          |              |                |                  |
|     |                   | mruby integer overflow      | 0:12              | LOC       | 0:25/1607                          | 10                                                    |              |                |                  |
| 5   | bug #5.0-2        | lua                         | 0:5               | aurora    | 0:15/1007                          | 63                                                    |              |                |                  |
|     |                   | lua                         | 0:1,40            | LOC       |                                    | 24                                                    |              |                |                  |
|     |                   | lua                         | 0:1,29            | LOC-DEBUG |                                    | 20                                                    |              |                |                  |
|     |                   | lua                         | 0:1               | BB        |                                    | 10                                                    |              |                |                  |
| 6   | Bugzilla-21670    | nm                          | 0:0.34            | aurora    | 0:19.34/297                        | 1                                                     |              |                |                  |
|     |                   | nm                          | 0:0.21            | LOC       | 0:33/291                           | 2                                                     |              |                |                  |
|     |                   | nm                          | 0:0.33            | aurora    |                                    | 1                                                     |              |                |                  |
|     |                   | nm                          | 0:0.20            | LOC-DEBUG |                                    | 4                                                     |              |                |                  |
|     |                   | nm                          | 0:0.15            | BB        |                                    | 4                                                     |              |                |                  |
| 7   | CVE-2017-12858    | libzip                      | 0:2               | aurora    | 0:23/327                           | 6                                                     |              |                | zip_dirent.c:581 |
|     |                   |                             | 0:0.47            | LOC       |                                    | 4                                                     |              |                |                  |
|     |                   |                             | 0:0.44            | LOC-DEBUG |                                    | 3                                                     |              |                |                  |
|     |                   |                             | 0:0.20            | BB        |                                    | 5                                                     |              |                |                  |
| 8   | CVE-2020-19497    | matio                       | 0:0.5             | aurora    | 0:23/97                            | 2                                                     |              |                |                  |
|     |                   |                             | 0:0.38            | LOC       |                                    | 1                                                     |              |                |                  |
|     |                   |                             | 0:0.39            | LOC-DEBUG |                                    | 1                                                     |              |                |                  |
|     |                   |                             | 0:0.36            | BB        |                                    | 1 (off by three lines?)                               |              |                |                  |
|     |                   |                             | 0:0.6             | aurora    | 1:15/119                           | 2                                                     |              |                |                  |
|     |                   |                             | 0:0.4             | LOC       |                                    | 1                                                     |              |                |                  |
|     |                   |                             | 0:0.38            | LOC-DEBUG |                                    | 1                                                     |              |                |                  |
|     |                   |                             | 0:0.36            | BB        |                                    | 1 (off by three lines)                                |              |                |                  |
| 9   | issue-905         | sleuthkit                   | 0:1.58            | aurora    |                                    | 9                                                     |              |                | ext2fs:807       |
|     |                   |                             | 0:0.56            | LOC       |                                    | 5                                                     |              |                |                  |
|     |                   |                             | 0:0.49            | LOC-DEBUG |                                    | 4                                                     |              |                |                  |
|     |                   |                             | 0:0.49            | BB        |                                    | 26 (off by 4 lines) or 4 (pinpoint inside a for loop) |              |                |                  |
| 10  | issue-3947        | mruby unintialized variable | 0:31              | aurora    | 0:23/1107                          | 2                                                     |              | 0:3            |                  |
|     |                   |                             | 0:9               | LOC       |                                    | 1                                                     |              | 0:1            |                  |
|     |                   |                             | 0:10              | LOC-DEBUG |                                    | 3                                                     |              | 0:1.30         |                  |
|     |                   |                             | 0:4               | BB        |                                    | 1                                                     |              | 0:1.15         |                  |
| 11  | CVE-2018-12248    |                             |                   |           |                                    |                                                       |              |                |                  |
|     |                   |                             |                   |           |                                    |                                                       |              |                |                  |

Increase  in instructions if include all jump is 15 - 22%
Increase in speed x2~x4
Better predicate ranking
Aurora - LOC - BB

