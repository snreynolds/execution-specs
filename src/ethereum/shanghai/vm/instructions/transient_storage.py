"""
Ethereum Virtual Machine (EVM) Transient Storage Instructions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: Table of Contents
    :backlinks: none
    :local:

Introduction
------------

Implementations of the EVM transient storage instructions.
"""
from ethereum.utils.ensure import ensure

from .. import Evm
from ..exceptions import WriteInStaticContext
from ...state import get_transient_storage, set_transient_storage
from .. gas import GAS_WARM_ACCESS, charge_gas
from ..stack import pop, push


def tload(evm: Evm) -> None:
    """
    Loads to the stack, the value corresponding to a certain key from the
    transient storage mapping of the current account.

    Parameters
    ----------
    evm :
        The current EVM frame.

    """
    # STACK
    key = pop(evm.stack).to_be_bytes32()

    # GAS
    charge_gas(evm, GAS_WARM_ACCESS)

    # OPERATION
    value = get_transient_storage(
        evm.env.state, evm.message.current_target, key)

    push(evm.stack, value)

    # PROGRAM COUNTER
    evm.pc += 1


def tstore(evm: Evm) -> None:
    """
    Stores a value at a certain key in the current context's transient storage mapping.

    Parameters
    ----------
    evm :
        The current EVM frame.

    """

    # STACK
    key = pop(evm.stack).to_be_bytes32()
    new_value = pop(evm.stack).to_be_bytes32()

    # GAS
    charge_gas(evm, GAS_WARM_ACCESS)

    # OPERATION
    ensure(not evm.message.is_static, WriteInStaticContext)
    set_transient_storage(
        evm.env.state, evm.message.current_target, key, new_value)

    # PROGRAM COUNTER
    evm.pc += 1
