bits 16
org 0x100
; Programa COM (16-bit) que solicita nombre completo y carrera
; Usa interrupciones INT 21h (funciones 09h y 0Ah) para I/O
; Ensamblar con: nasm -f bin -o 05_cadena.com 05_cadena.asm

border      db '========================================',13,10,'$'
title       db '     *** Registro de Estudiante ***',13,10,'$'
promptName  db 'Ingrese nombre completo: $'
promptCareer db 'Ingrese la carrera: $'
labelName   db 'Nombre  : $'
labelCareer db 'Carrera : $'
crlf        db 13,10,'$'
errTooLong  db 'Entrada demasiado larga',13,10,'$'

; Buffers para lectura con la estructura de INT 21h AH=0Ah
; primer byte = max length, segundo byte = actual count al regresar, luego bytes de texto
nameBuf     db 50,0   ; max 50 chars, count=0
            times 50 db 0
careerBuf   db 50,0
            times 50 db 0

; Buffers para mostrar (copiamos y añadimos terminador '$')
nameDisp    times 55 db 0
careerDisp  times 55 db 0

start:
    ; Mostrar encabezado decorativo
    mov dx, border
    call print_str
    mov dx, title
    call print_str
    mov dx, border
    call print_str

    ; Leer nombre
    mov dx, promptName
    call print_str
    mov dx, nameBuf
    mov ah, 0x0A
    int 0x21
    ; verificar longitud (si mayor al max no sucede, buffer contiene up to max)

    ; Leer carrera
    mov dx, promptCareer
    call print_str
    mov dx, careerBuf
    mov ah, 0x0A
    int 0x21

    ; Preparar y mostrar resultado con formato
    mov dx, border
    call print_str
    ; Mostrar etiqueta Nombre
    mov dx, labelName
    call print_str
    ; Copiar nombre desde nameBuf+2 a nameDisp y terminar con '$' y CRLF
    lea si, [nameBuf+2]
    lea di, [nameDisp]
    mov bl, [nameBuf+1]   ; longitud
    call copy_and_terminate
    mov dx, nameDisp
    call print_str

    ; Mostrar etiqueta Carrera
    mov dx, labelCareer
    call print_str
    lea si, [careerBuf+2]
    lea di, [careerDisp]
    mov bl, [careerBuf+1]
    call copy_and_terminate
    mov dx, careerDisp
    call print_str

    mov dx, border
    call print_str

    ; Terminar programa
    mov ax, 0x4C00
    int 0x21

; -----------------
; print_str: espera DX -> offset del string terminado en '$', usa INT21 AH=09
; Preserva AX
print_str:
    push ax
    mov ah, 0x09
    int 0x21
    pop ax
    ret

; copy_and_terminate: copia BL bytes desde SI a DI, luego añade 13,10,'$'
; usa BL como longitud; destruye SI, DI, BX
copy_and_terminate:
    push cx
    push si
    push di
    xor cx, cx
    mov cl, bl
    cmp cx, 0
    je .write_crlf
.copy_loop:
    mov al, [si]
    mov [di], al
    inc si
    inc di
    dec cx
    jnz .copy_loop
.write_crlf:
    mov byte [di], 13
    inc di
    mov byte [di], 10
    inc di
    mov byte [di], '$'
    ; restore and return
    pop di
    pop si
    pop cx
    ret

; NASM requires a final newline at end of file
