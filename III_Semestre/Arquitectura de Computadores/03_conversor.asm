; Conversor decimal (0-9) a binario (4 bits)
; NASM, Linux x86-64 (SysV ABI)

section .data
    prompt      db  "Ingrese un numero (0-9): ",0
    fmt_in      db  "%d",0
    fmt_out     db  "%s",10,0
    err_out     db  "Numero fuera de rango",10,0

section .bss
    num     resd 1
    buf     resb 5    ; 4 bits + terminador

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

    ; Leer entero
    lea rdi, [rel fmt_in]
    lea rsi, [rel num]
    xor rax, rax
    call scanf

    ; Validar 0 <= num <= 9
    mov eax, dword [rel num]
    cmp eax, 0
    jl .invalid
    cmp eax, 9
    jg .invalid

    ; Preparar buffer (4 caracteres)
    lea rdi, [rel buf]
    mov rsi, rdi        ; usar rsi como puntero (caller-saved)
    add rsi, 3          ; rsi -> última posición (index 3)

    mov ecx, 4          ; contar 4 bits
.conv_loop:
    mov edx, eax
    and edx, 1          ; edx = bit menos significativo
    add dl, '0'         ; convertir a ASCII
    mov [rsi], dl
    shr eax, 1
    dec rsi
    dec ecx
    jnz .conv_loop

    ; Null terminator
    lea rax, [rel buf]
    mov byte [rax+4], 0

    ; Imprimir resultado
    lea rdi, [rel fmt_out]
    lea rsi, [rel buf]
    xor rax, rax
    call printf

    jmp .done

.invalid:
    lea rdi, [rel err_out]
    xor rax, rax
    call printf

.done:
    xor edi, edi
    mov eax, 0
    pop rbp
    ret
