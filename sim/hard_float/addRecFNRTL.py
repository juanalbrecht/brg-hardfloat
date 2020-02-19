#=========================================================================
# Wrapper for HardFloat's addition and subtraction module

#=========================================================================

from pymtl3 import *
from pymtl3.passes.backends.verilog import \
    VerilogPlaceholderConfigs, VerilatorImportConfigs, TranslationConfigs
from pymtl3.stdlib.ifcs   import MinionIfcRTL

class addRecFNRTL( Placeholder, Component ):

  # Constructor

  def construct( s, expWidth = 3, sigWidth = 3 ):

    # Interface
	
    s.control        = InPort ()
    s.subOp          = InPort ()
    s.a              = InPort ( mk_bits(expWidth + sigWidth + 1) )
    s.b              = InPort ( mk_bits(expWidth + sigWidth + 1) )
    s.roundingMode   = InPort ( mk_bits(3) ) 
    
    s.out            = OutPort ( mk_bits(expWidth + sigWidth + 1) )
    s.exceptionFlags = OutPort ( mk_bits(5) )

    # Configurations

    from os import path
    s.config_placeholder = VerilogPlaceholderConfigs(
      src_file   = path.dirname(__file__) + '/addRecFN.v',
      top_module = 'addRecFN',
      has_clk    = False,
      has_reset  = False,
    )

