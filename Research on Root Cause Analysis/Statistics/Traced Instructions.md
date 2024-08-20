# Table for traced instructions to total instructions

| program | traced_instructions | total_instructions | percentage |
| ------- | ------------------- | ------------------ | ---------- |
| test    | 61                  | 392                | 15.5%      |
| readelf | 6359                | 57471              | 11.06%     |
|         |                     |                    |            |
# Table for tracing time


| No  | ID                | program                | tracing time(h:m) | method    | crash exploration time/files (h:m) | predicate ranking            | rca time (h:m) |
| --- | ----------------- | ---------------------- | ----------------- | --------- | ---------------------------------- | ---------------------------- | -------------- |
| 1   | Hackerone #186041 | mruby                  | 01:04             | aurora    | N/A                                | 33                           |                |
|     |                   | mruby                  | 0:40              | aurora    | 0:08/2070                          |                              |                |
|     |                   | mruby                  | 0:15              | LOC       | 0:14/2600                          |                              |                |
|     |                   | mruby                  | 0:9.6             | LOC       | 0:08/1848                          | 29                           |                |
|     |                   | mruby                  | 0:10.45           | LOC       | 0:08/1848                          | 29                           |                |
|     |                   | mruby                  | 0:12              | LOC       | 0:10/2200                          | 28                           |                |
|     |                   | mruby                  | 0:25              | LOC-DEBUG | 0:24/3900                          | 23                           |                |
| 2   | CVE-2016-5636     | python                 | 1:01              | aurora    | 0:20/826                           | 269                          |                |
|     |                   | python                 | 0:29              | LOC       | 0:40/1002                          | 51                           |                |
|     |                   | python                 | 0:25              | LOC       | 0:20/826                           | 192                          |                |
|     |                   | python                 | 0:25              | LOC       | 0:20/826                           | 203                          |                |
|     |                   | python                 | 0:15              | LOC-DEBUG | 0:20/825                           | 157                          |                |
|     |                   | python                 | 0:13              | BB        | 0:20/826                           | 177                          |                |
| 3   | CVE-2019-9077     | readelf                | 0:1               | LOC-DEBUG | 0:03/853                           | 1                            |                |
|     |                   | readelf                | 0:1               | LOC       |                                    | 2                            |                |
|     |                   | readelf                | 0:2               | aurora    |                                    | 4                            |                |
|     |                   | readelf                | 0:1               | BB        |                                    | 1                            |                |
| 4   | CVE-2018-10191    | mruby integer overflow | 0:6               | BB        | 0:25/1607                          | 5/ off root cause by 4 lines |                |
|     |                   | mruby integer overflow | 0:12              | LOC       | 0:25/1607                          | 10                           |                |
| 5   | bug #5.0-2        | lua                    | 0:5               | aurora    | 0:15/1007                          | 63                           |                |
|     |                   | lua                    | 0:1,40            | LOC       |                                    | 24                           |                |
|     |                   | lua                    | 0:1,29            | LOC-DEBUG |                                    | 20                           |                |
|     |                   | lua                    | 0:1               | BB        |                                    | 10                           |                |
| 6   | Bugzilla-21670    | nm                     | 0:0.34            | aurora    | 0:19.34/297                        | 1                            |                |
|     |                   | nm                     | 0:0.21            | LOC       | 0:33/291                           | 2                            |                |
|     |                   | nm                     | 0:0.33            | aurora    |                                    | 1                            |                |
|     |                   | nm                     | 0:0.20            | LOC-DEBUG |                                    | 4                            |                |
|     |                   | nm                     | 0:0.15            | BB        |                                    | 4                            |                |
| 7   | CVE-2017-12858    | libzip                 | 0:2               | aurora    | 0:23/327                           | 6                            |                |
|     |                   |                        | 0:0.47            | LOC       |                                    | 4                            |                |
|     |                   |                        | 0:0.44            | LOC-DEBUG |                                    | 3                            |                |
|     |                   |                        | 0:0.20            | BB        |                                    | 5                            |                |
| 8   | CVE-2020-19497    | matio                  | 0:0.5             | aurora    | 0:23/97                            | 2                            |                |
|     |                   |                        | 0:0.38            | LOC       |                                    | 1                            |                |
|     |                   |                        | 0:0.39            | LOC-DEBUG |                                    | 1                            |                |
|     |                   |                        | 0:0.36            | BB        |                                    | 1 (off by three lines?)      |                |
|     |                   |                        | 0:0.6             | aurora    | 1:15/119                           | 2                            |                |
|     |                   |                        | 0:0.4             | LOC       |                                    | 1                            |                |
|     |                   |                        | 0:0.38            | LOC-DEBUG |                                    | 1                            |                |
|     |                   |                        | 0:0.36            | BB        |                                    | 1 (off by three lines)       |                |
| 9   | issue-905         | sleuthkit              | 0:1.58            | aurora    |                                    | 9                            |                |
|     |                   |                        | 0:0.56            | LOC       |                                    | 5                            |                |
|     |                   |                        | 0:0.49            | LOC-DEBUG |                                    | 4                            |                |
|     |                   |                        | 0:0.49            | BB        |                                    | 26 (off by 4 lines)          |                |

Increase  in instructions if include all jump is 15 - 22%
Increase in speed x2~x4
Better predicate ranking
