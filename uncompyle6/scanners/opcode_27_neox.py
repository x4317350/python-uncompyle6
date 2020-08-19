
from xdis.opcodes.base import def_op, finalize_opcodes, init_opdata, update_pj3
import xdis.opcodes.opcode_27 as opcode_27

version = 2.7
python_implementation = "CPython"

l = locals()
init_opdata(l, opcode_27, 2.7)

def_op(l, "LOAD_VAR_ZERO_LOAD_CONST", 173, 0, 2)

update_pj3(globals(), l)

finalize_opcodes(l)
