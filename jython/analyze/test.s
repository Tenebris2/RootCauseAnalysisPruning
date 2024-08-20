	.file	"test.c"
	.intel_syntax noprefix
# GNU C17 (Ubuntu 11.4.0-1ubuntu1~22.04) version 11.4.0 (x86_64-linux-gnu)
#	compiled by GNU C version 11.4.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version isl-0.24-GMP

# GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
# options passed: -masm=intel -mtune=generic -march=x86-64 -g -fasynchronous-unwind-tables -fstack-protector-strong -fstack-clash-protection -fcf-protection
	.text
.Ltext0:
	.file 0 "/home/tenebris/Documents/Root Cause Analysis/analyze" "test.c"
	.section	.rodata
.LC0:
	.string	"Enter 5 integers:"
.LC1:
	.string	"Number %d: "
.LC2:
	.string	"%d"
.LC3:
	.string	"You entered: "
.LC4:
	.string	"Sum of the numbers: %d\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.file 1 "test.c"
	.loc 1 8 12
	.cfi_startproc
	endbr64	
	push	rbp	#
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp	#,
	.cfi_def_cfa_register 6
	sub	rsp, 48	#,
# test.c:8: int main() {
	.loc 1 8 12
	mov	rax, QWORD PTR fs:40	# tmp101, MEM[(<address-space-1> long unsigned int *)40B]
	mov	QWORD PTR -8[rbp], rax	# D.2387, tmp101
	xor	eax, eax	# tmp101
# test.c:13:     printf("Enter 5 integers:\n");
	.loc 1 13 5
	lea	rax, .LC0[rip]	# tmp86,
	mov	rdi, rax	#, tmp86
	call	puts@PLT	#
# test.c:14:     for (i = 0; i < 5; i++) {
	.loc 1 14 12
	mov	DWORD PTR -40[rbp], 0	# i,
# test.c:14:     for (i = 0; i < 5; i++) {
	.loc 1 14 5
	jmp	.L2	#
.L3:
# test.c:15:         printf("Number %d: ", i + 1);
	.loc 1 15 9 discriminator 3
	mov	eax, DWORD PTR -40[rbp]	# tmp87, i
	add	eax, 1	# _1,
	mov	esi, eax	#, _1
	lea	rax, .LC1[rip]	# tmp88,
	mov	rdi, rax	#, tmp88
	mov	eax, 0	#,
	call	printf@PLT	#
# test.c:16:         scanf("%d", &numbers[i]);
	.loc 1 16 9 discriminator 3
	lea	rdx, -32[rbp]	# tmp89,
	mov	eax, DWORD PTR -40[rbp]	# tmp91, i
	cdqe
	sal	rax, 2	# tmp92,
	add	rax, rdx	# _2, tmp89
	mov	rsi, rax	#, _2
	lea	rax, .LC2[rip]	# tmp93,
	mov	rdi, rax	#, tmp93
	mov	eax, 0	#,
	call	__isoc99_scanf@PLT	#
# test.c:14:     for (i = 0; i < 5; i++) {
	.loc 1 14 25 discriminator 3
	add	DWORD PTR -40[rbp], 1	# i,
.L2:
# test.c:14:     for (i = 0; i < 5; i++) {
	.loc 1 14 19 discriminator 1
	cmp	DWORD PTR -40[rbp], 4	# i,
	jle	.L3	#,
# test.c:20:     int sum = sumArray(numbers, 5);
	.loc 1 20 15
	lea	rax, -32[rbp]	# tmp94,
	mov	esi, 5	#,
	mov	rdi, rax	#, tmp94
	call	sumArray	#
	mov	DWORD PTR -36[rbp], eax	# sum, tmp95
# test.c:23:     printf("You entered: ");
	.loc 1 23 5
	lea	rax, .LC3[rip]	# tmp96,
	mov	rdi, rax	#, tmp96
	mov	eax, 0	#,
	call	printf@PLT	#
# test.c:24:     printArray(numbers, 5);
	.loc 1 24 5
	lea	rax, -32[rbp]	# tmp97,
	mov	esi, 5	#,
	mov	rdi, rax	#, tmp97
	call	printArray	#
# test.c:25:     printf("Sum of the numbers: %d\n", sum);
	.loc 1 25 5
	mov	eax, DWORD PTR -36[rbp]	# tmp98, sum
	mov	esi, eax	#, tmp98
	lea	rax, .LC4[rip]	# tmp99,
	mov	rdi, rax	#, tmp99
	mov	eax, 0	#,
	call	printf@PLT	#
# test.c:27:     return 0;
	.loc 1 27 12
	mov	eax, 0	# _13,
# test.c:28: }
	.loc 1 28 1
	mov	rdx, QWORD PTR -8[rbp]	# tmp102, D.2387
	sub	rdx, QWORD PTR fs:40	# tmp102, MEM[(<address-space-1> long unsigned int *)40B]
	je	.L5	#,
	call	__stack_chk_fail@PLT	#
.L5:
	leave	
	.cfi_def_cfa 7, 8
	ret	
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.section	.rodata
.LC5:
	.string	"%d "
	.text
	.globl	printArray
	.type	printArray, @function
printArray:
.LFB1:
	.loc 1 31 38
	.cfi_startproc
	endbr64	
	push	rbp	#
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp	#,
	.cfi_def_cfa_register 6
	sub	rsp, 32	#,
	mov	QWORD PTR -24[rbp], rdi	# arr, arr
	mov	DWORD PTR -28[rbp], esi	# size, size
.LBB2:
# test.c:32:     for (int i = 0; i < size; i++) {
	.loc 1 32 14
	mov	DWORD PTR -4[rbp], 0	# i,
# test.c:32:     for (int i = 0; i < size; i++) {
	.loc 1 32 5
	jmp	.L7	#
.L8:
# test.c:33:         printf("%d ", arr[i]);
	.loc 1 33 26 discriminator 3
	mov	eax, DWORD PTR -4[rbp]	# tmp86, i
	cdqe
	lea	rdx, 0[0+rax*4]	# _2,
	mov	rax, QWORD PTR -24[rbp]	# tmp87, arr
	add	rax, rdx	# _3, _2
# test.c:33:         printf("%d ", arr[i]);
	.loc 1 33 9 discriminator 3
	mov	eax, DWORD PTR [rax]	# _4, *_3
	mov	esi, eax	#, _4
	lea	rax, .LC5[rip]	# tmp88,
	mov	rdi, rax	#, tmp88
	mov	eax, 0	#,
	call	printf@PLT	#
# test.c:32:     for (int i = 0; i < size; i++) {
	.loc 1 32 32 discriminator 3
	add	DWORD PTR -4[rbp], 1	# i,
.L7:
# test.c:32:     for (int i = 0; i < size; i++) {
	.loc 1 32 23 discriminator 1
	mov	eax, DWORD PTR -4[rbp]	# tmp89, i
	cmp	eax, DWORD PTR -28[rbp]	# tmp89, size
	jl	.L8	#,
.LBE2:
# test.c:35:     printf("\n");
	.loc 1 35 5
	mov	edi, 10	#,
	call	putchar@PLT	#
# test.c:36: }
	.loc 1 36 1
	nop	
	leave	
	.cfi_def_cfa 7, 8
	ret	
	.cfi_endproc
.LFE1:
	.size	printArray, .-printArray
	.globl	sumArray
	.type	sumArray, @function
sumArray:
.LFB2:
	.loc 1 39 35
	.cfi_startproc
	endbr64	
	push	rbp	#
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp	#,
	.cfi_def_cfa_register 6
	mov	QWORD PTR -24[rbp], rdi	# arr, arr
	mov	DWORD PTR -28[rbp], esi	# size, size
# test.c:40:     int sum = 0;
	.loc 1 40 9
	mov	DWORD PTR -8[rbp], 0	# sum,
.LBB3:
# test.c:41:     for (int i = 0; i < size; i++) {
	.loc 1 41 14
	mov	DWORD PTR -4[rbp], 0	# i,
# test.c:41:     for (int i = 0; i < size; i++) {
	.loc 1 41 5
	jmp	.L10	#
.L11:
# test.c:42:         sum += arr[i];
	.loc 1 42 19 discriminator 3
	mov	eax, DWORD PTR -4[rbp]	# tmp88, i
	cdqe
	lea	rdx, 0[0+rax*4]	# _2,
	mov	rax, QWORD PTR -24[rbp]	# tmp89, arr
	add	rax, rdx	# _3, _2
	mov	eax, DWORD PTR [rax]	# _4, *_3
# test.c:42:         sum += arr[i];
	.loc 1 42 13 discriminator 3
	add	DWORD PTR -8[rbp], eax	# sum, _4
# test.c:41:     for (int i = 0; i < size; i++) {
	.loc 1 41 32 discriminator 3
	add	DWORD PTR -4[rbp], 1	# i,
.L10:
# test.c:41:     for (int i = 0; i < size; i++) {
	.loc 1 41 23 discriminator 1
	mov	eax, DWORD PTR -4[rbp]	# tmp90, i
	cmp	eax, DWORD PTR -28[rbp]	# tmp90, size
	jl	.L11	#,
.LBE3:
# test.c:44:     return sum;
	.loc 1 44 12
	mov	eax, DWORD PTR -8[rbp]	# _10, sum
# test.c:45: }
	.loc 1 45 1
	pop	rbp	#
	.cfi_def_cfa 7, 8
	ret	
	.cfi_endproc
.LFE2:
	.size	sumArray, .-sumArray
.Letext0:
	.file 2 "/usr/include/stdio.h"
	.section	.debug_info,"",@progbits
.Ldebug_info0:
	.long	0x1c9
	.value	0x5
	.byte	0x1
	.byte	0x8
	.long	.Ldebug_abbrev0
	.uleb128 0x9
	.long	.LASF14
	.byte	0x1d
	.long	.LASF0
	.long	.LASF1
	.quad	.Ltext0
	.quad	.Letext0-.Ltext0
	.long	.Ldebug_line0
	.uleb128 0x1
	.byte	0x8
	.byte	0x7
	.long	.LASF2
	.uleb128 0x1
	.byte	0x4
	.byte	0x7
	.long	.LASF3
	.uleb128 0x1
	.byte	0x1
	.byte	0x8
	.long	.LASF4
	.uleb128 0x1
	.byte	0x2
	.byte	0x7
	.long	.LASF5
	.uleb128 0x1
	.byte	0x1
	.byte	0x6
	.long	.LASF6
	.uleb128 0x1
	.byte	0x2
	.byte	0x5
	.long	.LASF7
	.uleb128 0xa
	.byte	0x4
	.byte	0x5
	.string	"int"
	.uleb128 0x1
	.byte	0x8
	.byte	0x5
	.long	.LASF8
	.uleb128 0x1
	.byte	0x1
	.byte	0x6
	.long	.LASF9
	.uleb128 0xb
	.long	0x66
	.uleb128 0xc
	.long	.LASF15
	.byte	0x2
	.value	0x1b5
	.byte	0xc
	.long	.LASF16
	.long	0x58
	.long	0x8e
	.uleb128 0x3
	.long	0x8e
	.uleb128 0x4
	.byte	0
	.uleb128 0x5
	.long	0x6d
	.uleb128 0xd
	.long	.LASF17
	.byte	0x2
	.value	0x164
	.byte	0xc
	.long	0x58
	.long	0xab
	.uleb128 0x3
	.long	0x8e
	.uleb128 0x4
	.byte	0
	.uleb128 0xe
	.long	.LASF18
	.byte	0x1
	.byte	0x27
	.byte	0x5
	.long	0x58
	.quad	.LFB2
	.quad	.LFE2-.LFB2
	.uleb128 0x1
	.byte	0x9c
	.long	0x116
	.uleb128 0x6
	.string	"arr"
	.byte	0x27
	.byte	0x12
	.long	0x116
	.uleb128 0x2
	.byte	0x91
	.sleb128 -40
	.uleb128 0x7
	.long	.LASF10
	.byte	0x27
	.byte	0x1d
	.long	0x58
	.uleb128 0x2
	.byte	0x91
	.sleb128 -44
	.uleb128 0x2
	.string	"sum"
	.byte	0x28
	.byte	0x9
	.long	0x58
	.uleb128 0x2
	.byte	0x91
	.sleb128 -24
	.uleb128 0x8
	.quad	.LBB3
	.quad	.LBE3-.LBB3
	.uleb128 0x2
	.string	"i"
	.byte	0x29
	.byte	0xe
	.long	0x58
	.uleb128 0x2
	.byte	0x91
	.sleb128 -20
	.byte	0
	.byte	0
	.uleb128 0x5
	.long	0x58
	.uleb128 0xf
	.long	.LASF11
	.byte	0x1
	.byte	0x1f
	.byte	0x6
	.quad	.LFB1
	.quad	.LFE1-.LFB1
	.uleb128 0x1
	.byte	0x9c
	.long	0x174
	.uleb128 0x6
	.string	"arr"
	.byte	0x1f
	.byte	0x15
	.long	0x116
	.uleb128 0x2
	.byte	0x91
	.sleb128 -40
	.uleb128 0x7
	.long	.LASF10
	.byte	0x1f
	.byte	0x20
	.long	0x58
	.uleb128 0x2
	.byte	0x91
	.sleb128 -44
	.uleb128 0x8
	.quad	.LBB2
	.quad	.LBE2-.LBB2
	.uleb128 0x2
	.string	"i"
	.byte	0x20
	.byte	0xe
	.long	0x58
	.uleb128 0x2
	.byte	0x91
	.sleb128 -20
	.byte	0
	.byte	0
	.uleb128 0x10
	.long	.LASF12
	.byte	0x1
	.byte	0x8
	.byte	0x5
	.long	0x58
	.quad	.LFB0
	.quad	.LFE0-.LFB0
	.uleb128 0x1
	.byte	0x9c
	.long	0x1c0
	.uleb128 0x11
	.long	.LASF13
	.byte	0x1
	.byte	0x9
	.byte	0x9
	.long	0x1c0
	.uleb128 0x2
	.byte	0x91
	.sleb128 -48
	.uleb128 0x2
	.string	"i"
	.byte	0xa
	.byte	0x9
	.long	0x58
	.uleb128 0x2
	.byte	0x91
	.sleb128 -56
	.uleb128 0x2
	.string	"sum"
	.byte	0x14
	.byte	0x9
	.long	0x58
	.uleb128 0x2
	.byte	0x91
	.sleb128 -52
	.byte	0
	.uleb128 0x12
	.long	0x58
	.uleb128 0x13
	.long	0x2e
	.byte	0x4
	.byte	0
	.byte	0
	.section	.debug_abbrev,"",@progbits
.Ldebug_abbrev0:
	.uleb128 0x1
	.uleb128 0x24
	.byte	0
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0x3e
	.uleb128 0xb
	.uleb128 0x3
	.uleb128 0xe
	.byte	0
	.byte	0
	.uleb128 0x2
	.uleb128 0x34
	.byte	0
	.uleb128 0x3
	.uleb128 0x8
	.uleb128 0x3a
	.uleb128 0x21
	.sleb128 1
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x2
	.uleb128 0x18
	.byte	0
	.byte	0
	.uleb128 0x3
	.uleb128 0x5
	.byte	0
	.uleb128 0x49
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x4
	.uleb128 0x18
	.byte	0
	.byte	0
	.byte	0
	.uleb128 0x5
	.uleb128 0xf
	.byte	0
	.uleb128 0xb
	.uleb128 0x21
	.sleb128 8
	.uleb128 0x49
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x6
	.uleb128 0x5
	.byte	0
	.uleb128 0x3
	.uleb128 0x8
	.uleb128 0x3a
	.uleb128 0x21
	.sleb128 1
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x2
	.uleb128 0x18
	.byte	0
	.byte	0
	.uleb128 0x7
	.uleb128 0x5
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0x21
	.sleb128 1
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x2
	.uleb128 0x18
	.byte	0
	.byte	0
	.uleb128 0x8
	.uleb128 0xb
	.byte	0x1
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x12
	.uleb128 0x7
	.byte	0
	.byte	0
	.uleb128 0x9
	.uleb128 0x11
	.byte	0x1
	.uleb128 0x25
	.uleb128 0xe
	.uleb128 0x13
	.uleb128 0xb
	.uleb128 0x3
	.uleb128 0x1f
	.uleb128 0x1b
	.uleb128 0x1f
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x12
	.uleb128 0x7
	.uleb128 0x10
	.uleb128 0x17
	.byte	0
	.byte	0
	.uleb128 0xa
	.uleb128 0x24
	.byte	0
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0x3e
	.uleb128 0xb
	.uleb128 0x3
	.uleb128 0x8
	.byte	0
	.byte	0
	.uleb128 0xb
	.uleb128 0x26
	.byte	0
	.uleb128 0x49
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0xc
	.uleb128 0x2e
	.byte	0x1
	.uleb128 0x3f
	.uleb128 0x19
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0x5
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x6e
	.uleb128 0xe
	.uleb128 0x27
	.uleb128 0x19
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x3c
	.uleb128 0x19
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0xd
	.uleb128 0x2e
	.byte	0x1
	.uleb128 0x3f
	.uleb128 0x19
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0x5
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x27
	.uleb128 0x19
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x3c
	.uleb128 0x19
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0xe
	.uleb128 0x2e
	.byte	0x1
	.uleb128 0x3f
	.uleb128 0x19
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x27
	.uleb128 0x19
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x12
	.uleb128 0x7
	.uleb128 0x40
	.uleb128 0x18
	.uleb128 0x7a
	.uleb128 0x19
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0xf
	.uleb128 0x2e
	.byte	0x1
	.uleb128 0x3f
	.uleb128 0x19
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x27
	.uleb128 0x19
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x12
	.uleb128 0x7
	.uleb128 0x40
	.uleb128 0x18
	.uleb128 0x7c
	.uleb128 0x19
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x10
	.uleb128 0x2e
	.byte	0x1
	.uleb128 0x3f
	.uleb128 0x19
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x12
	.uleb128 0x7
	.uleb128 0x40
	.uleb128 0x18
	.uleb128 0x7c
	.uleb128 0x19
	.uleb128 0x1
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x11
	.uleb128 0x34
	.byte	0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x39
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x2
	.uleb128 0x18
	.byte	0
	.byte	0
	.uleb128 0x12
	.uleb128 0x1
	.byte	0x1
	.uleb128 0x49
	.uleb128 0x13
	.byte	0
	.byte	0
	.uleb128 0x13
	.uleb128 0x21
	.byte	0
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x2f
	.uleb128 0xb
	.byte	0
	.byte	0
	.byte	0
	.section	.debug_aranges,"",@progbits
	.long	0x2c
	.value	0x2
	.long	.Ldebug_info0
	.byte	0x8
	.byte	0
	.value	0
	.value	0
	.quad	.Ltext0
	.quad	.Letext0-.Ltext0
	.quad	0
	.quad	0
	.section	.debug_line,"",@progbits
.Ldebug_line0:
	.section	.debug_str,"MS",@progbits,1
.LASF15:
	.string	"scanf"
.LASF3:
	.string	"unsigned int"
.LASF18:
	.string	"sumArray"
.LASF13:
	.string	"numbers"
.LASF2:
	.string	"long unsigned int"
.LASF9:
	.string	"char"
.LASF16:
	.string	"__isoc99_scanf"
.LASF4:
	.string	"unsigned char"
.LASF12:
	.string	"main"
.LASF8:
	.string	"long int"
.LASF11:
	.string	"printArray"
.LASF5:
	.string	"short unsigned int"
.LASF17:
	.string	"printf"
.LASF10:
	.string	"size"
.LASF7:
	.string	"short int"
.LASF14:
	.string	"GNU C17 11.4.0 -masm=intel -mtune=generic -march=x86-64 -g -fasynchronous-unwind-tables -fstack-protector-strong -fstack-clash-protection -fcf-protection"
.LASF6:
	.string	"signed char"
	.section	.debug_line_str,"MS",@progbits,1
.LASF0:
	.string	"test.c"
.LASF1:
	.string	"/home/tenebris/Documents/Root Cause Analysis/analyze"
	.ident	"GCC: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	1f - 0f
	.long	4f - 1f
	.long	5
0:
	.string	"GNU"
1:
	.align 8
	.long	0xc0000002
	.long	3f - 2f
2:
	.long	0x3
3:
	.align 8
4:
