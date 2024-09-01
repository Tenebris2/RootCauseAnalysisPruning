**### Speed Up

| No      | Vulnerability     | LOC    | LOC-DEBUG | BB     |
| ------- | ----------------- | ------ | --------- | ------ |
| 1       | Hackerone #186041 | 11x    | 11x       | 11x    |
| 2       | CVE-2016-5636     | 2.3x   | 3.1x      | 5.1x   |
| 3       | CVE-2019-9077     | 1.6x   | 1.6x      | 2.5x   |
| 4       | CVE-2018-10191    | 4x     | 4x        | 6.67x  |
| 5       | bug #5.0-2        | 3.6x   | 3.6x      | 5.5x   |
| 6       | Bugzilla-21670    | 1.57x  | 1.65x     | 2.2x   |
| 7       | CVE-2017-12858    | 2.55x  | 2.72x     | 6x     |
| 8       | CVE-2020-19497    | 1.31x  | 1.28x     | 1.38x  |
| 9       | issue-905         | 1.7x   | 1.93x     | 1.93x  |
| 10      | issue-3047        | 3.4x   | 3.1x      | 7.75x  |
| 11      | CVE-2018-12248    | 4.3x   | 4.3x      | 10x    |
| 12      | CVE-2018-13785    | 1.7x   | 1.7x      | 1.89x  |
| 13      | CVE-2021-20205    | 1.2x   | 1.2x      | 1.33x  |
| 14      | CVE-2018-14498    | 1.33x  | 1.33x     | 2x     |
| 15      | bug #54558        | 2x     | 2x        | 2.36x  |
| 16      | CVE-2017-16808    | 2x     | 2.24x     | 3x     |
| 17      | CVE-2017-5969     | 2.37x  | 2.49x     | 3.39x  |
| 18      | CVE-2021-45340    | 1.4x   | 1.458     | 1.48   |
| Average |                   | 2.388x | 2.4x      | 3.833x |
### Predicates
_At CVE-2018-10191, all were off root cause as the fuzzing time was not enough!_
**O - x** : Off of root cause by {x}
**O - F**: Point root cause inside a for loop

Instruction Selection
Selective Instructions
**Selective Predicate-based Root Cause Analysis**
**On instruction selection for predicate-based root cause analysis**


Level of detail
- Aurora: every single instructions
- LOC: Line of Code (1 Inst / LOC)
- Basic Block: 1 inst / basic block (branch)

Time: Tracing(Intel Pin) - Predicate Analysis (PA) (Predicate -> Instruction) - Ranking (-> Execution Rank)

| No  | Vulnerability     | Aurora (Instructions) | LOC       | LOC(with Source) | Basic Block |
| --- | ----------------- | --------------------- | --------- | ---------------- | ----------- |
| 1   | Hackerone #186041 | 97                    | 31        | 31               | 28          |
| 2   | CVE-2016-5636     | 290                   | 184       | 157              | 194         |
| 3   | CVE-2019-9077     | 4                     | 2         | 4                | 1           |
| 4   | CVE-2018-10191    | 1(O - 36)             | 1(O - 36) | 13(O - 35)       | 5(O - 43)   |
| 5   | bug #5.0-2        | 20                    | 7         | 7                | 5           |
| 6   | Bugzilla-21670    | 1                     | 2         | 4                | 4           |
| 7   | CVE-2017-12858    | 6                     | 4         | 3                | 5           |
| 8   | CVE-2020-19497    | 2                     | 1         | 1                | 1 (O - 3)   |
| 9   | issue-905         | 9                     | 5         | 4                | 4 (O - F)   |
| 10  | issue-3047        | 2                     | 1         | 3                | 1           |
| 11  | CVE-2018-12248    | 1                     | 2 (O - 1) | 1                | 4 (O - 1)   |
| 12  | CVE-2018-13785    | 4                     | 2         | 3                | 2           |
| 13  | CVE-2021-20205    | 2                     | 1         | 1                | 1 (O - 7)   |
| 14  | CVE-2018-14498    | 1                     | 1         | 1                | 1 (O - 2)   |
| 15  | bug #54558        | 3                     | 2         | 2                | 1 (O - 1)   |
| 16  | CVE-2017-16808    | 1                     | 5         | 1                | 5           |
| 17  | CVE-2017-5969     | 35                    | 13        | 12               | 12          |
| 18  | CVE-2021-45340    | 29                    | 16        | 49               | 20          |
### SLOC 
**X**: Off of root cause

| No  | Vulnerability     | Aurora | LOC | LOC-DEBUG | BB  |
| --- | ----------------- | ------ | --- | --------- | --- |
| 1   | Hackerone #186041 | 40     | 26  | 27        | 26  |
| 2   | CVE-2016-5636     | 188    | 149 | 136       | 104 |
| 3   | CVE-2019-9077     | 2      | 2   | 4         | 1   |
| 4   | CVE-2018-10191    | 1X     | 1X  | 11X       | 4X  |
| 5   | bug #5.0-2        | 9      | 7   | 7         | 5   |
| 6   | Bugzilla-21670    | 1      | 2   | 4         | 4   |
| 7   | CVE-2017-12858    | 4      | 4   | 3         | 4   |
| 8   | CVE-2020-19497    | 2      | 1   | 1         | 1X  |
| 9   | issue-905         | 5      | 5   | 4         | 4X  |
| 10  | issue-3047        | 2      | 1   | 3         | 1   |
| 11  | CVE-2018-12248    | 1      | 2X  | 1         | 4X  |
| 12  | CVE-2018-13785    | 3      | 2   | 3         | 2   |
| 13  | CVE-2021-20205    | 2      | 1   | 1         | 1X  |
| 14  | CVE-2018-14498    | 1      | 1   | 1         | 1X  |
| 15  | bug #54558        | 2      | 2   | 2         | 1X  |
| 16  | CVE-2017-16808    | 1      | 5   | 1         | 5   |
| 17  | CVE-2017-5969     | 15     | 10  | 9         | 11  |
| 18  | CVE-2021-45340    | 14     | 16  | 48        | 17  |
