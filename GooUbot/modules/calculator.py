import ast
import operator
from pyrogram import Client, filters
from GooUbot import *

__MODULE__ = "calc"
__HELP__ = """
<blockquote><b>--\u0299\u1d00\u0274\u1d1b\u1d1c\u1d00\u0274 \u1d1c\u0274\u1d1b\u1d1c\u1d0b \u1d04\u1d00\u029f\u1d04\u1d1c\u029f\u1d00\u1d1b\u1d0f\u0280--</b></blockquote>

<blockquote><b>\ud83d\udea6 \u1d18\u1d07\u0280\u026a\u0274\u1d1b\u1d00\u029c :</b> <code>{0}calc</code>
\ud83e\udda0 \u1d0b\u1d07\u1d1b : \u1d0d\u1d07\u0274\u0262\u029c\u026a\u1d1b\u1d1c\u0274\u0262 \u1d07\u1d0b\ua731\u1d18\u0280\u1d07\ua731\u026a \u1d0d\u1d00\u1d1b\u1d07\u1d0d\u1d00\u1d1b\u026a\u1d0b\u1d00.
\ud83e\udda0 \u1d04\u1d0f\u0274\u1d1b\u1d0f\u029c : <code>{0}calc 5 + 10 * 2</code></b></blockquote>
"""

SAFE_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

def safe_eval(node):
    if isinstance(node, ast.Expression):
        return safe_eval(node.body)
    elif isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Tipe data tidak didukung")
    elif isinstance(node, ast.BinOp):
        op = SAFE_OPS.get(type(node.op))
        if not op:
            raise ValueError(f"Operator tidak didukung: {type(node.op).__name__}")
        left = safe_eval(node.left)
        right = safe_eval(node.right)
        if isinstance(node.op, ast.Pow) and right > 100:
            raise ValueError("Eksponen terlalu besar (max 100)")
        return op(left, right)
    elif isinstance(node, ast.UnaryOp):
        op = SAFE_OPS.get(type(node.op))
        if not op:
            raise ValueError(f"Operator tidak didukung: {type(node.op).__name__}")
        return op(safe_eval(node.operand))
    else:
        raise ValueError("Ekspresi tidak valid atau tidak aman")

@PY.UBOT("calc")
@PY.TOP_CMD
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        return await message.reply("\u274c Format salah! Gunakan: <code>.calc [ekspresi]</code>")

    expression = args[1].strip()

    try:
        tree = ast.parse(expression, mode="eval")
        result = safe_eval(tree)
        await message.reply(f"\u2705 Hasil: <code>{result}</code>")
    except Exception as e:
        await message.reply(f"\u274c Error: {str(e)}")
