; Suma acumulada desde 1 hasta n
; NASM, Linux x86-64 (SysV ABI)

section .data
	prompt      db  "Ingrese un entero n: ",0
	fmt_in      db  "%d",0
	fmt_out     db  "La suma de 1 a %d es: %ld",10,0
	fmt_out_zero db "La suma es: %ld",10,0

section .bss
	n       resd 1
	; sum se mantiene en rax, no hace falta reservar en bss

section .text
	global main
	extern printf
	extern scanf

main:
	push rbp
	mov rbp, rsp

	; Mostrar prompt
	lea rdi, [rel prompt]
	xor rax, rax
	call printf

	; Leer entero n
	lea rdi, [rel fmt_in]
	lea rsi, [rel n]
	xor rax, rax
	call scanf

	; Extender n a 64 bits en rsi
	mov eax, dword [rel n]
	movsxd rsi, eax        ; rsi = n (sign-extended)

	; Si n < 1, imprimir 0
	cmp rsi, 1
	jl .print_zero

	; Inicializar suma y contador
	xor rax, rax          ; rax = suma (64-bit)
	mov rcx, 1            ; contador = 1

.loop:
	cmp rcx, rsi
	jg .after_loop
	add rax, rcx
	inc rcx
	jmp .loop

.after_loop:
	; Imprimir resultado: printf(fmt_out, n, sum)
	lea rdi, [rel fmt_out]
	mov esi, dword [rel n]   ; segundo argumento (int n)
	mov rdx, rax             ; tercer argument (long sum) -> passed in rdx
	xor rax, rax
	call printf
	jmp .done

.print_zero:
	lea rdi, [rel fmt_out_zero]
	mov rsi, 0
	xor rax, rax
	call printf

.done:
	xor edi, edi
	mov eax, 0
	pop rbp
	ret

