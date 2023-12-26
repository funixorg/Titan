from opcodes import *
from dtype import *
from codewriter import *
from executable import *


m_prog = Executable()


m_prog.new_constant(
    "magic",
    0xF1A
)

m_prog.new_variable(
    "offset",
    None,
    Types.INT32
)

m_prog.new_function(
    "addedzamuncabol",
    [("a", Types.INT32),
    ("b", Types.INT32),
    ("c", Types.INT32)],
    [
        m_prog.Move(Registers.RDX, 50),
        m_prog.Move(Registers.RCX, 5),
        m_prog.Add(Registers.RAX, Registers.RCX),
        m_prog.Return()
    ]
)

m_prog.new_function(
    "main",
    [],
    [
        m_prog.Push(1),
        m_prog.Push(2),
        m_prog.Call("add"),
    ]
)



mwt = mcWriter(m_prog, "initramdir/sys/bin/testbin")