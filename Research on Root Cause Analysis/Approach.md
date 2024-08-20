Better predicate ranking due to this?
![[Pasted image 20240810193112.png]]

## Fixing Discrepancy
As was stated in the paper in mruby missing check type confusion, I found that the line with predicate describing the location of developers fix is ranked 15th, as such the analyst has to inspect 14 lines of code that are related to the bug but do not point to the developer fix. And in the terms of predicates, the 33rd predicate explains the root cause. This results from the fact that one source code line may translate to multiple assembly instructions. Thus, multiple predicate may refer to values used in the same source code line.
Using our method of mapping final lines of instructions to their respective source code line, we can reduce this discrepancy and have better ranking in terms of predicates

_Vietnamese edition_
Khi  đang đọc lại qua bài báo aurora, em phát hiện trong đoạn Case Studies của mruby rằng developer phải xét dòng lệnh thứ 15 để phát hiện lỗi, nhưng về mặt vị từ thì đến vị từ thứ 33 mới tìm ra root cause. Điều này do một dòng mã nguồn có thể dịch sang nhiều lệnh.
Vậy nên em nghĩ với phương pháp đại diện từng dòng mã nguồn với câu lệnh cuối cùng của nó có thể khắc phục điều này và giúp cải tiến ranking không ạ.

# Reason for covering all jumps in decompiler mode
Our decompiler mode is to replicate what dwarf does to map source code to their respective instructions which we cannot 100% replicate with just decompiler mode as there are no way of distinguishing different instances of code or data that might have same basic entry or contexts and location. => We need to replicate discriminators by over all covering all jump cases possible.
Dwarf Discriminators are for when a single line of source code has multiple path of executions for example
``` C
x = (i == 1 ? one() : two());
```
A "discriminator" is an arbitrary value used to distinguish multiple constructs (traditionally basic blocks) that occur on the same (file, line, column) location.
In summary, a DWARF discrimininator is a mechanism in which DWARF debugging format allows more precise tracking of code execution, especially in scenarios where multiple machine instructions or code blocks correspond to a single source line.

# Why not just cover all jumps instead?
CVE-2018-10191, root cause at line 1200 in vm.c
![[mruby_source_code_integer_overflow.png]]
![[mruby_integer_overflow_dump_dwarf.png]]
![[mruby_integer_overflow_decompiled.png]]What happens if the root cause is in a line of code that does not cover a basic block? The root cause won't be able to be detected!
![[mruby_integer_overflow_rca_results.png]]
Closest to the root cause is vm.c:1204

_vietnamese edition_
Em thưa thầy, em phát hiện rằng trong CVE-2018-10191 root cause nằm trong một khoảng các câu lệnh liên tục làm cho việc sử dụng trace theo phương pháp basic block bị lệch root cause khoảng 4 dòng lệnh ở vm.c: 1204 trong khi root cause nằm ở dòng lệnh 1200 của vm.c do root cause ở vm.c:1200 nằm trong một basic block lớn gồm nhiều câu lệnh khác.

CVE-2018-10191
![[mruby_source_code_integer_overflow.png]]
Dump của chương trình mruby
![[mruby_integer_overflow_dump_dwarf.png]]

Ánh xạ câu lệnh lên dòng code đã được dịch ngược
![[mruby_integer_overflow_decompiled.png]]
Kết quả root cause analysis sử dụng trace theo basic block
![[mruby_integer_overflow_rca_results.png]]
Kết quả root cause analysis sử dụng trace theo ánh xạ câu lệnh ra dòng lệnh biên dịch ngược
![[Pasted image 20240818134632.png]]
matio

![[Pasted image 20240820195815.png]]
Sleuthkit
![[Pasted image 20240820173106.png]]
![[Pasted image 20240820205542.png]]