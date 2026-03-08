; Calculadora de la suma de 2 numeros
; Realizado por: Jhonathan Damian Guerrero Montoya


section .data
	prompt1     db  "Ingrese el primer numero: ",0
	prompt2     db  "Ingrese el segundo numero: ",0
	promptOp     db  "Ingrese la operacion (+ - * /): ",0
	fmt_in      db  "%d",0
	fmt_in_double db "%lf",0
	fmt_op      db  " %c",0
	fmt_out     db  "El resultado es: %f",10,0
	err_op      db  "Operacion invalida",10,0

section .bss
	num1    resq 1    ; double
	num2    resq 1    ; double
	op      resb 1

section .text
	global main
	extern printf
	extern scanf

main:
	push    rbp
	mov     rbp, rsp

	; Prompt y lectura del primer numero (double)
	lea     rdi, [rel prompt1]
	xor     rax, rax
	call    printf

	lea     rdi, [rel fmt_in_double]
	lea     rsi, [rel num1]
	xor     rax, rax
	call    scanf

	; Prompt y lectura del segundo numero (double)
	lea     rdi, [rel prompt2]
	xor     rax, rax
	call    printf

	lea     rdi, [rel fmt_in_double]
	lea     rsi, [rel num2]
	xor     rax, rax
	call    scanf

	; Prompt y lectura del operador (char) - usa " %c" para saltar espacios
	lea     rdi, [rel promptOp]
	xor     rax, rax
	call    printf

	lea     rdi, [rel fmt_op]
	lea     rsi, [rel op]
	xor     rax, rax
	call    scanf

	; Cargar operandos en registros SSE (double)
	movsd   xmm0, qword [rel num1]
	movsd   xmm1, qword [rel num2]

	; Obtener operador
	movzx   eax, byte [rel op]
	cmp     al, '+'
	je      .op_add
	cmp     al, '-'
	je      .op_sub
	cmp     al, '*'
	je      .op_mul
	cmp     al, '/'
	je      .op_div

	; Operador invalido
	lea     rdi, [rel err_op]
	xor     rax, rax
	call    printf
	jmp     .done

.op_add:
	addsd   xmm0, xmm1
	jmp     .print

.op_sub:
	subsd   xmm0, xmm1
	jmp     .print

.op_mul:
	mulsd   xmm0, xmm1
	jmp     .print

.op_div:
	divsd   xmm0, xmm1
	jmp     .print

.print:
	lea     rdi, [rel fmt_out]
	; resultado en xmm0
	mov     al, 1      ; numero de registers SSE usados (para llamadas variadicas)
	call    printf

.done:
	xor     eax, eax
	pop     rbp
	ret