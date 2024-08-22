![[Pasted image 20240821105714.png | Dump and source code of fls]]

![[Pasted image 20240821105620.png | RCA ranking results of fls when doing basic block tracing]]

## Root Cause
issue 905 of sleuthkit pinpoints the root cause ext2fs.c, a double free error
![[Pasted image 20240821110055.png | Developer patch fixes by using correct counter to increment pointer]]

### Issue with Basic Block Tracing
![[Pasted image 20240821110540.png]]
Branch instructions at 803 and 782
-> Inputs rarely go to 803, BB tracing can only really trace at 782 -> Only traces at the for loop -> Cannot exactly pin point the root cause