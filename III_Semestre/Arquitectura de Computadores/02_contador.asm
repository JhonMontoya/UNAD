; Contador 1..10 en NASM (Linux x86-64, SysV ABI)

section .data
	fmt db "%d",10,0

section .text
	global main
	extern printf

main:
	push rbp
	mov rbp, rsp
	push rbx             ; preservar rbx (calle-saved)

	mov ebx, 1           ; contador = 1 (usar ebx para que printf no lo sobrescriba)

.loop:
	lea rdi, [rel fmt]   ; formato "%d\n"
	mov esi, ebx         ; segundo arg = contador
	xor eax, eax         ; rax=0 (no SSE regs usados para printf)
	call printf

	inc ebx
	cmp ebx, 11          ; mientras contador <= 10
	jne .loop

	xor edi, edi         ; return 0
	mov eax, 0
	pop rbx
	pop rbp
	ret

