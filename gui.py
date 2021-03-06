#!/usr/local/bin/python
import serial
import pygtk
pygtk.require('2.0')
import gtk
import os, sys
from bitarray import bitarray
import binascii
from bitstring import BitArray

class PipeApp:
	
	def __init__(self):

		#=============Ventana Principal=================					
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_title("MIPS")
		window.connect("destroy", lambda x: gtk.main_quit())
		window.set_border_width(2)
		main_vbox = gtk.VBox(False, 0)
		window.add(main_vbox)
		#~ window.set_size_request(300, 300)
		#=============Frame Acciones Botones y PC=================
		frame_acciones = gtk.Frame("Acciones")
		main_vbox.pack_start(frame_acciones,  False,  False, 10)
		acciones_hbox = gtk.HBox(False, 0)
		acciones_hbox.set_border_width(2)
		frame_acciones.add(acciones_hbox)
		#========Boton Ejecucion Continua=============================
		boton_ejecutar=gtk.Button("Ejecutar")
		acciones_hbox.pack_start(boton_ejecutar, False, False,10)
		boton_ejecutar.connect("clicked", self.botonEjecutar, None)
		#========Boton Paso A Paso========================
		boton_paso=gtk.Button("Paso")
		acciones_hbox.pack_start(boton_paso, False, False,10)
		boton_paso.connect("clicked", self.botonPaso, None)
		#========Boton Reset========================
		boton_reset=gtk.Button("Reset")
		acciones_hbox.pack_start(boton_reset, False, False,10)
		boton_reset.connect("clicked", self.botonReset, None)
		#=============Frame Regitros PIPE=================
		frame_etapas = gtk.Frame("Etapas")
		main_vbox.pack_start(frame_etapas,  False,  False, 10)
		etapas_hbox = gtk.HBox(False, 0)
		etapas_hbox.set_border_width(2)
		frame_etapas.add(etapas_hbox)
		#=============Etapa IF/ID=================
		frame_etapa1 = gtk.Frame("IF/ID")
		etapas_hbox.pack_start(frame_etapa1,  False,  False, 10)
		etapa1_hbox = gtk.HBox(False, 0)
		#~ etapa1_hbox.set_border_width(10)
		etapa1_vbox = gtk.VBox(False, 0)
		etapa1_vbox2 = gtk.VBox(False, 0)
		frame_etapa1.add(etapa1_hbox)
		etapa1_hbox.pack_start(etapa1_vbox,  False,  False, 10)
		etapa1_hbox.pack_start(etapa1_vbox2,  False,  False, 10)
		#=========Registros Etapa Intruccion============
		label_pc = gtk.Label("PC")
		etapa1_vbox.pack_start(label_pc)
		self.entry_pc = gtk.Entry()
		etapa1_vbox2.add(self.entry_pc)
		label_intrucccion = gtk.Label("Instruccion")
		etapa1_vbox.pack_start(label_intrucccion)
		self.entry_instruccion = gtk.Entry()
		etapa1_vbox2.pack_end(self.entry_instruccion)		
		#=============Etapa ID/EX=================
		frame_etapa2 = gtk.Frame("ID/EX")
		etapas_hbox.pack_start(frame_etapa2,  False,  False, 10)
		etapa2_hbox = gtk.HBox(False, 0)
		#~ etapa2_hbox.set_border_width(10)
		etapa2_vbox = gtk.VBox(False, 0)
		etapa2_vbox2 = gtk.VBox(False, 0)
		frame_etapa2.add(etapa2_hbox)
		etapa2_hbox.pack_start(etapa2_vbox,  False,  False, 10)
		etapa2_hbox.pack_start(etapa2_vbox2,  False,  False, 10)
		#=========Registros Etapa Execute============
		label_MemToReg_IDEX = gtk.Label("MemToReg")
		etapa2_vbox.pack_start(label_MemToReg_IDEX)
		self.entry_MemToReg_IDEX = gtk.Entry()
		etapa2_vbox2.add(self.entry_MemToReg_IDEX)
		label_RegWrite_IDEX = gtk.Label("RegWrite")
		etapa2_vbox.pack_start(label_RegWrite_IDEX)
		self.entry_RegWrite_IDEX = gtk.Entry()
		etapa2_vbox2.add(self.entry_RegWrite_IDEX)		
		label_Branch_IDEX = gtk.Label("Branch")
		etapa2_vbox.pack_start(label_Branch_IDEX)
		self.entry_Branch_IDEX = gtk.Entry()
		etapa2_vbox2.add(self.entry_Branch_IDEX)		
		label_MemRead_IDEX = gtk.Label("MemRead")
		etapa2_vbox.pack_start(label_MemRead_IDEX)
		self.entry_MemRead_IDEX = gtk.Entry()
		etapa2_vbox2.add(self.entry_MemRead_IDEX)		
		label_MemWrite_IDEX = gtk.Label("MemWrite")
		etapa2_vbox.pack_start(label_MemWrite_IDEX)
		self.entry_MemWrite_IDEX = gtk.Entry()
		etapa2_vbox2.add(self.entry_MemWrite_IDEX)
		label_RegDst_IDEX = gtk.Label("RegDst")
		etapa2_vbox.pack_start(label_RegDst_IDEX)
		self.entry_RegDst_IDEX = gtk.Entry()
		etapa2_vbox2.add(self.entry_RegDst_IDEX)
		label_AluOp_IDEX = gtk.Label("Alu Operacion")
		etapa2_vbox.pack_start(label_AluOp_IDEX)
		self.entry_AluOp_IDEX = gtk.Entry()
		etapa2_vbox2.add(self.entry_AluOp_IDEX)		
		label_AluSrc_IDEX = gtk.Label("AluSrc")
		etapa2_vbox.pack_start(label_AluSrc_IDEX)
		self.entry_AluSrc_IDEX = gtk.Entry()
		etapa2_vbox2.add(self.entry_AluSrc_IDEX)
		label_PCCount_IDEX = gtk.Label("PCCount")
		etapa2_vbox.pack_start(label_PCCount_IDEX)
		self.entry_PCCount_IDEX = gtk.Entry()
		etapa2_vbox2.add(self.entry_PCCount_IDEX)
		label_d1 = gtk.Label("Registro A")
		etapa2_vbox.pack_start(label_d1)
		self.entry_d1 = gtk.Entry()
		etapa2_vbox2.add(self.entry_d1)		
		label_d1 = gtk.Label("Registro B")
		etapa2_vbox.pack_start(label_d1)
		self.entry_d2 = gtk.Entry()
		etapa2_vbox2.add(self.entry_d2)		
		label_se = gtk.Label("Sign Extend")
		etapa2_vbox.pack_start(label_se)
		self.entry_se = gtk.Entry()
		etapa2_vbox2.add(self.entry_se)
		label_rt = gtk.Label("RT")
		etapa2_vbox.pack_start(label_rt)
		self.entry_rt = gtk.Entry()
		etapa2_vbox2.add(self.entry_rt)
		label_rd = gtk.Label("RD")
		etapa2_vbox.pack_start(label_rd)
		self.entry_rd = gtk.Entry()
		etapa2_vbox2.add(self.entry_rd)		
		#=============Etapa EX/MEM=================
		frame_etapa3 = gtk.Frame("EX/MEM")
		etapas_hbox.pack_start(frame_etapa3,  False,  False, 10)
		etapa3_hbox = gtk.HBox(False, 0)
		#~ etapa3_hbox.set_border_width(10)
		frame_etapa3.add(etapa3_hbox)
		etapa3_vbox = gtk.VBox(False, 0)
		etapa3_vbox2 = gtk.VBox(False, 0)
		etapa3_hbox.pack_start(etapa3_vbox,  False,  False, 10)
		etapa3_hbox.pack_start(etapa3_vbox2,  False,  False, 10)
		#=========Registros Etapa Execute============
		label_MemToReg_EXMEM = gtk.Label("MemToReg")
		etapa3_vbox.pack_start(label_MemToReg_EXMEM)
		self.entry_MemToReg_EXMEM = gtk.Entry()
		etapa3_vbox2.add(self.entry_MemToReg_EXMEM)
		label_RegWrite_EXMEM = gtk.Label("RegWrite")
		etapa3_vbox.pack_start(label_RegWrite_EXMEM)
		self.entry_RegWrite_EXMEM = gtk.Entry()
		etapa3_vbox2.add(self.entry_RegWrite_EXMEM)
		label_Branch_EXMEM = gtk.Label("Branch")
		etapa3_vbox.pack_start(label_Branch_EXMEM)
		self.entry_Branch_EXMEM = gtk.Entry()
		etapa3_vbox2.add(self.entry_Branch_EXMEM)
		label_MemRead_EXMEM = gtk.Label("MemRead")
		etapa3_vbox.pack_start(label_MemRead_EXMEM)
		self.entry_MemRead_EXMEM = gtk.Entry()
		etapa3_vbox2.add(self.entry_MemRead_EXMEM)
		label_currentPC_EXMEM = gtk.Label("currentPC")
		etapa3_vbox.pack_start(label_currentPC_EXMEM)
		self.entry_currentPC_EXMEM = gtk.Entry()
		etapa3_vbox2.add(self.entry_currentPC_EXMEM)
		label_PCJump = gtk.Label(" PCJump")
		etapa3_vbox.pack_start(label_PCJump)
		self.entry_PCJump = gtk.Entry()
		etapa3_vbox2.add(self.entry_PCJump)
		label_MemWrite_EXMEM = gtk.Label("MemWrite")
		etapa3_vbox.pack_start(label_MemWrite_EXMEM)
		self.entry_MemWrite_EXMEM = gtk.Entry()
		etapa3_vbox2.add(self.entry_MemWrite_EXMEM)	
		label_zero_EXMEM = gtk.Label("Zero")
		etapa3_vbox.pack_start(label_zero_EXMEM)
		self.entry_zero_EXMEM = gtk.Entry()
		etapa3_vbox2.add(self.entry_zero_EXMEM)
		label_aluResult_EXMEM = gtk.Label("Alu Resultado")
		etapa3_vbox.pack_start(label_aluResult_EXMEM)
		self.entry_aluResult_EXMEM = gtk.Entry()
		etapa3_vbox2.add(self.entry_aluResult_EXMEM)
		label_RegB_EXMEM = gtk.Label("Reg B")
		etapa3_vbox.pack_start(label_RegB_EXMEM)
		self.entry_RegB_EXMEM = gtk.Entry()
		etapa3_vbox2.add(self.entry_RegB_EXMEM)		
		label_wr_EXMEM = gtk.Label("WR")
		etapa3_vbox.pack_start(label_wr_EXMEM)
		self.entry_wr_EXMEM = gtk.Entry()
		etapa3_vbox2.add(self.entry_wr_EXMEM)
		#~ label_PCSrcOut_EXMEM = gtk.Label("PCSrcOut")
		#~ etapa3_vbox.pack_start(label_PCSrcOut_EXMEM)
		#~ self.entry_PCSrcOut_EXMEM = gtk.Entry()
		#~ etapa3_vbox2.add(self.entry_PCSrcOut_EXMEM)
		#=============Etapa MEM/WB=================
		frame_etapa4 = gtk.Frame("MEM/WB")
		etapas_hbox.pack_start(frame_etapa4,  False,  False, 10)
		etapa4_hbox = gtk.HBox(False, 0)
		#~ etapa4_hbox.set_border_width(10)
		frame_etapa4.add(etapa4_hbox)
		etapa4_vbox = gtk.VBox(False, 0)
		etapa4_vbox2 = gtk.VBox(False, 0)
		etapa4_hbox.pack_start(etapa4_vbox,  False,  False, 10)
		etapa4_hbox.pack_start(etapa4_vbox2,  False,  False, 10)
		#=========Registros Etapa Execute============
		label_PCSrc_MEMIF = gtk.Label("PCSrc")
		etapa4_vbox.pack_start(label_PCSrc_MEMIF)
		self.entry_PCSrc_MEMIF= gtk.Entry()
		etapa4_vbox2.add(self.entry_PCSrc_MEMIF)
		label_MemToReg_MEMW = gtk.Label("MemToReg")
		etapa4_vbox.pack_start(label_MemToReg_MEMW)
		self.entry_MemToReg_MEMW= gtk.Entry()
		etapa4_vbox2.add(self.entry_MemToReg_MEMW)
		label_regWrite_WBID = gtk.Label("RegWrite")
		etapa4_vbox.pack_start(label_regWrite_WBID)
		self.entry_regWrite_WBID = gtk.Entry()
		etapa4_vbox2.add(self.entry_regWrite_WBID)
		label_CurrentPC_MEMWB = gtk.Label("CurrentPC")
		etapa4_vbox.pack_start(label_CurrentPC_MEMWB)
		self.entry_CurrentPC_MEMWB = gtk.Entry()
		etapa4_vbox2.add(self.entry_CurrentPC_MEMWB)
		label_readData_MEMWB = gtk.Label("ReadDataOut")
		etapa4_vbox.pack_start(label_readData_MEMWB)
		self.entry_readData_MEMWB = gtk.Entry()
		etapa4_vbox2.add(self.entry_readData_MEMWB)
		label_ALUResult_MEMWB = gtk.Label("Alu Resultado")
		etapa4_vbox.pack_start(label_ALUResult_MEMWB)
		self.entry_ALUResult_MEMWB = gtk.Entry()
		etapa4_vbox2.add(self.entry_ALUResult_MEMWB)
		label_writeRegister_WBID = gtk.Label(" writeRegister")
		etapa4_vbox.pack_start(label_writeRegister_WBID)
		self.entry_writeRegister_WBID = gtk.Entry()
		etapa4_vbox2.add(self.entry_writeRegister_WBID)
		label_writeData_WBID = gtk.Label("writeData")
		etapa4_vbox.pack_start(label_writeData_WBID)
		self.entry_writeData_WBID = gtk.Entry()
		etapa4_vbox2.add(self.entry_writeData_WBID)
		#=============Frame Banco de Registro y Memoria===============
		frame_datos = gtk.Frame("Banco de Datos")
		main_vbox.pack_start(frame_datos,  False,  False, 10)
		datos_hbox = gtk.HBox(False, 0)
		#~ datos_hbox.set_border_width(10)
		frame_datos.add(datos_hbox)
		#=============Frame Banco de Registro ===============
		frame_registros = gtk.Frame("Banco de Registros")
		datos_hbox.pack_start(frame_registros, False, False, 10)
		registros_hbox = gtk.HBox(False, 0)
		#~ registros_hbox.set_border_width(10)
		frame_registros.add(registros_hbox)
		registros_vbox  = gtk.VBox(False, 0)
		registros_vbox.set_border_width(7)
		registros_vbox2 = gtk.VBox(False, 0)
		registros_vbox2.set_border_width(7)
		registros_vbox3 = gtk.VBox(False, 0)
		registros_vbox3.set_border_width(7)
		registros_vbox4 = gtk.VBox(False, 0)
		registros_vbox4.set_border_width(7)
		registros_vbox5 = gtk.VBox(False, 0)
		registros_vbox5.set_border_width(7)
		registros_vbox6 = gtk.VBox(False, 0)
		registros_vbox6.set_border_width(7)
		registros_vbox7 = gtk.VBox(False, 0)
		registros_vbox7.set_border_width(7)
		registros_vbox8 = gtk.VBox(False, 0)
		registros_vbox8.set_border_width(7)
		registros_hbox.pack_start(registros_vbox,   False,  False)
		registros_hbox.pack_start(registros_vbox2,  False,  False)
		registros_hbox.pack_start(registros_vbox3,  False,  False)
		registros_hbox.pack_start(registros_vbox4,  False,  False)
		registros_hbox.pack_start(registros_vbox5,  False,  False)
		registros_hbox.pack_start(registros_vbox6,  False,  False)
		registros_hbox.pack_start(registros_vbox7,  False,  False)
		registros_hbox.pack_start(registros_vbox8,  False,  False)
		#=============Frame Banco de Memoria ===============
		frame_memoria = gtk.Frame("Banco de Memoria")
		datos_hbox.pack_start(frame_memoria, False, False,10)
		memoria_hbox = gtk.HBox(False, 0)
		memoria_hbox.set_border_width(10)
		frame_memoria.add(memoria_hbox)
		memoria_vbox  = gtk.VBox(False, 0)
		memoria_vbox2 = gtk.VBox(False, 0)
		memoria_vbox3 = gtk.VBox(False, 0)
		memoria_vbox4 = gtk.VBox(False, 0)
		memoria_hbox.pack_start(memoria_vbox,   False,  False, 10)
		memoria_hbox.pack_start(memoria_vbox2,  False,  False)
		memoria_hbox.pack_start(memoria_vbox3,  False,  False)
		memoria_hbox.pack_start(memoria_vbox4,  False,  False)
		#=============Banco de Registro=================
		#Primera columna registros 1-8 | Segunda Columna valores de 1-8
		label = gtk.Label("$1:")
		registros_vbox.pack_start(label)
		self.label_v1 = gtk.Label()
		registros_vbox2.add(self.label_v1)
		label = gtk.Label("$2:")
		registros_vbox.pack_start(label)
		self.label_v2 = gtk.Label()
		registros_vbox2.add(self.label_v2)
		label = gtk.Label("$3:")
		registros_vbox.pack_start(label)
		self.label_v3 = gtk.Label()
		registros_vbox2.add(self.label_v3)
		label = gtk.Label("$4:")
		registros_vbox.pack_start(label)
		self.label_v4 = gtk.Label()
		registros_vbox2.add(self.label_v4)
		label = gtk.Label("$5:")
		registros_vbox.pack_start(label)
		self.label_v5 = gtk.Label()
		registros_vbox2.add(self.label_v5)
		label = gtk.Label("$6:")
		registros_vbox.pack_start(label)
		self.label_v6 = gtk.Label()
		registros_vbox2.add(self.label_v6)
		label = gtk.Label("$7:")
		registros_vbox.pack_start(label)
		self.label_v7 = gtk.Label()
		registros_vbox2.add(self.label_v7)
		label = gtk.Label("$8:")
		registros_vbox.pack_start(label)
		self.label_v8 = gtk.Label()
		registros_vbox2.add(self.label_v8)
		#tercera columna registros 9-16 | Cuarta Columna valores de 9-16
		label = gtk.Label("$9:")
		registros_vbox3.pack_start(label)
		self.label_v9 = gtk.Label()
		registros_vbox4.add(self.label_v9)
		label = gtk.Label("$10:")
		registros_vbox3.pack_start(label)
		self.label_v10 = gtk.Label()
		registros_vbox4.add(self.label_v10)
		label = gtk.Label("$11:")
		registros_vbox3.pack_start(label)
		self.label_v11 = gtk.Label()
		registros_vbox4.add(self.label_v11)
		label = gtk.Label("$12:")
		registros_vbox3.pack_start(label)
		self.label_v12 = gtk.Label()
		registros_vbox4.add(self.label_v12)
		label = gtk.Label("$13:")
		registros_vbox3.pack_start(label)
		self.label_v13 = gtk.Label()
		registros_vbox4.add(self.label_v13)
		label = gtk.Label("$14:")
		registros_vbox3.pack_start(label)
		self.label_v14 = gtk.Label()
		registros_vbox4.add(self.label_v14)
		label = gtk.Label("$15:")
		registros_vbox3.pack_start(label)
		self.label_v15 = gtk.Label()
		registros_vbox4.add(self.label_v15)
		label = gtk.Label("$16:")
		registros_vbox3.pack_start(label)
		self.label_v16 = gtk.Label()
		registros_vbox4.add(self.label_v16)
		#Quinta columna registros 17-24 | Sexta Columna valores de 17-24
		label = gtk.Label("$17:")
		registros_vbox5.pack_start(label)
		self.label_v17 = gtk.Label()
		registros_vbox6.add(self.label_v17)
		label = gtk.Label("$18:")
		registros_vbox5.pack_start(label)
		self.label_v18 = gtk.Label()
		registros_vbox6.add(self.label_v18)
		label = gtk.Label("$19:")
		registros_vbox5.pack_start(label)
		self.label_v19 = gtk.Label()
		registros_vbox6.add(self.label_v19)
		label = gtk.Label("$20:")
		registros_vbox5.pack_start(label)
		self.label_v20 = gtk.Label()
		registros_vbox6.add(self.label_v20)
		label = gtk.Label("$21:")
		registros_vbox5.pack_start(label)
		self.label_v21 = gtk.Label()
		registros_vbox6.add(self.label_v21)
		label = gtk.Label("$22:")
		registros_vbox5.pack_start(label)
		self.label_v22 = gtk.Label()
		registros_vbox6.add(self.label_v22)
		label = gtk.Label("$23:")
		registros_vbox5.pack_start(label)
		self.label_v23 = gtk.Label()
		registros_vbox6.add(self.label_v23)
		label = gtk.Label("$24:")
		registros_vbox5.pack_start(label)
		self.label_v24 = gtk.Label()
		registros_vbox6.add(self.label_v24)
		#Septima columna registros 25-32 | Octava Columna valores de 25-32
		label = gtk.Label("$25:")
		registros_vbox7.pack_start(label)
		self.label_v25 = gtk.Label()
		registros_vbox8.add(self.label_v25)
		label = gtk.Label("$26:")
		registros_vbox7.pack_start(label)
		self.label_v26 = gtk.Label()
		registros_vbox8.add(self.label_v26)
		label = gtk.Label("$27:")
		registros_vbox7.pack_start(label)
		self.label_v27 = gtk.Label()
		registros_vbox8.add(self.label_v27)
		label = gtk.Label("$28:")
		registros_vbox7.pack_start(label)
		self.label_v28 = gtk.Label()
		registros_vbox8.add(self.label_v28)
		label = gtk.Label("$29:")
		registros_vbox7.pack_start(label)
		self.label_v29 = gtk.Label()
		registros_vbox8.add(self.label_v29)
		label = gtk.Label("$30:")
		registros_vbox7.pack_start(label)
		self.label_v30 = gtk.Label()
		registros_vbox8.add(self.label_v30)
		label = gtk.Label("$31:")
		registros_vbox7.pack_start(label)
		self.label_v31 = gtk.Label()
		registros_vbox8.add(self.label_v31)
		label = gtk.Label("$32:")
		registros_vbox7.pack_start(label)
		self.label_v32 = gtk.Label()
		registros_vbox8.add(self.label_v32)
		#=============Banco de Memoria==================
		#Primera columna memoria de 1-5 | Segunda Columna valores de 1-5
		label = gtk.Label("#1:")
		memoria_vbox.pack_start(label)
		self.label_m1 = gtk.Label()
		memoria_vbox2.add(self.label_m1)
		label = gtk.Label("#2:")
		memoria_vbox.pack_start(label)
		self.label_m2 = gtk.Label()
		memoria_vbox2.add(self.label_m2)
		label = gtk.Label("#3:")
		memoria_vbox.pack_start(label)
		self.label_m3 = gtk.Label()
		memoria_vbox2.add(self.label_m3)
		label = gtk.Label("#4:")
		memoria_vbox.pack_start(label)
		self.label_m4 = gtk.Label()
		memoria_vbox2.add(self.label_m4)
		label = gtk.Label("#5:")
		memoria_vbox.pack_start(label)
		self.label_m5 = gtk.Label()
		memoria_vbox2.add(self.label_m5)
		#Tercera columna memoria de 6-10 | Cuarta Columna valores de 6-10
		label = gtk.Label("#6:")
		memoria_vbox3.pack_start(label)
		self.label_m6 = gtk.Label()
		memoria_vbox4.add(self.label_m6)
		label = gtk.Label("#7:")
		memoria_vbox3.pack_start(label)
		self.label_m7 = gtk.Label()
		memoria_vbox4.add(self.label_m7)
		label = gtk.Label("#8:")
		memoria_vbox3.pack_start(label)
		self.label_m8 = gtk.Label()
		memoria_vbox4.add(self.label_m8)
		label = gtk.Label("#9:")
		memoria_vbox3.pack_start(label)
		self.label_m9 = gtk.Label()
		memoria_vbox4.add(self.label_m9)
		label = gtk.Label("#10:")
		memoria_vbox3.pack_start(label)
		self.label_m10 = gtk.Label()
		memoria_vbox4.add(self.label_m10)
		#=====Scroll Ventanas==================================
		ventanascroll = gtk.ScrolledWindow()
		#~ ventanascroll.set_border_width(10)
		ventanascroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
		main_vbox.pack_start(ventanascroll, True, True, 10)
		#~ ventanascroll.add_with_viewport(main_vbox)
		
		ventanascroll.show()
		window.show_all()
		#~ window.maximize()
#===================Fin Window========================================
	def botonPaso(self, widget, data=None):
		#~ try:
			#~ ser = serial.Serial('/dev/ttyUSB0',19200)
		#~ except:
			#~ print "No se puede abrir puerto serie"
		#~ try:
			self.cadena = bitarray()
			ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1) # open serial port
			ser.write('1') # write a string
			a = ser.read(175)
			ser.close() 
			self.cadena.frombytes(a)
			print self.cadena
		#~ except serial.serialutil.SerialException:
			#~ pass
			self.actualizarDatos()
			pass
#=================Envia senal de Reset=============================
	def botonReset(self, widget, data=None):
		try:
			ser = serial.Serial('/dev/ttyUSB0',19200, timeout=1)
		except:
			print "No se puede abrir puerto serie"
		try:
			self.cadena = bitarray()
			ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1) # open serial port
			print(ser.name) # check which port was really used
			ser.write('3') # write a string
			a = ser.read(175)
			self.cadena.frombytes(a)
			ser.close()
			print self.cadena
		except:
			print "No se pudo concretar la funcion"
		self.actualizarDatos()
		pass
#===========Funcion de Ejecucion continua========================
	def botonEjecutar(self, widget, data=None):
		try:
			ser = serial.Serial('/dev/ttyUSB0',19200)
		except:
			print "No se puede abrir puerto serie"
		try:
			self.cadena = bitarray()
			ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1) # open serial port
			ser.write('2') # write a string
			a = ser.read(176)
			self.cadena.frombytes(a)
			ser.close()
			print self.cadena
		except:
			print "No se pudo concretar la funcion"
		self.actualizarDatos()
		pass
#===========Funciones que Actualizan los Datos en la GUI================
	def actualizarDatos(self):
		# Etapa IF/ID Listo
		#~ self.entry_pc.set_text(str((int((self.cadena[1714:1721]),2)<<2) + int((self.cadena[0:2]),2))) #para archivo
		self.entry_pc.set_text(str((int(str((self.cadena[0:10].to01())),2)))) 
		self.entry_instruccion.set_text(str(self.cadena[10:42].to01()))	
		#~ # Etapa ID/EX Listo
		self.entry_MemToReg_IDEX.set_text(str(int(self.cadena[1066]) == 1))
		self.entry_RegWrite_IDEX.set_text(str(int(self.cadena[1067]) == 1))
		self.entry_Branch_IDEX.set_text  (str(int(self.cadena[1068]) == 1))
		self.entry_MemRead_IDEX.set_text (str(int(self.cadena[1069]) == 1))
		self.entry_MemWrite_IDEX.set_text(str(int(self.cadena[1070]) == 1))
		self.entry_RegDst_IDEX.set_text  (str(int(self.cadena[1071]) == 1))
		self.entry_AluOp_IDEX.set_text(str(self.cadena[1072:1074].to01())) 
		self.entry_AluSrc_IDEX.set_text(str(int(self.cadena[1074]) == 1))
		self.entry_PCCount_IDEX.set_text(str(( int(str((self.cadena[1075:1085].to01())),2)))) 
		self.entry_d1.set_text(str(int((self.cadena[1085:1117].to01()),2)))	
		self.entry_d2.set_text(str(int((self.cadena[1117:1149].to01()),2)))
		self.entry_se.set_text(str(int((self.cadena[1149:1181].to01()),2)))
		self.entry_rt.set_text(str(int((self.cadena[1181:1186].to01()),2)))
		self.entry_rd.set_text(str(int((self.cadena[1186:1191].to01()),2)))
		#~ # Etapa EX/MEM
		self.entry_MemToReg_EXMEM.set_text(str(int(self.cadena[1191]) == 1))
		self.entry_RegWrite_EXMEM.set_text(str(int(self.cadena[1192]) == 1))
		self.entry_Branch_EXMEM.set_text  (str(int(self.cadena[1193]) == 1))
		self.entry_MemRead_EXMEM.set_text (str(int(self.cadena[1194]) == 1))
		self.entry_MemWrite_EXMEM.set_text(str(int(self.cadena[1195]) == 1))
		self.entry_currentPC_EXMEM.set_text(str(( int(str((self.cadena[1196:1206].to01())),2)))) 
		self.entry_PCJump.set_text(str(( int(str((self.cadena[1206:1216].to01())),2)))) 
		self.entry_zero_EXMEM.set_text	  (str(int(self.cadena[1216]) == 1))
		self.entry_aluResult_EXMEM.set_text(str(int((self.cadena[1217:1249].to01()),2)))
		self.entry_RegB_EXMEM.set_text(str((int(str((self.cadena[1249:1281].to01())),2)))) 
		self.entry_wr_EXMEM.set_text(str((int(str((self.cadena[1281:1285].to01())),2))))
		#~ # Etapa MEM/WB
		self.entry_PCSrc_MEMIF.set_text(str(int(self.cadena[1286]) == 1))
		self.entry_MemToReg_MEMW.set_text(str(int(self.cadena[1287]) == 1))
		self.entry_regWrite_WBID.set_text(str(int(self.cadena[1288]) == 1))
		self.entry_CurrentPC_MEMWB.set_text(str(( int(str((self.cadena[1289:1299].to01())),2))))
		self.entry_readData_MEMWB.set_text(str(( int(str((self.cadena[1249:1281].to01())),2))))
		self.entry_ALUResult_MEMWB.set_text(str(( int(str((self.cadena[1331:1363].to01())),2))))
		self.entry_writeRegister_WBID.set_text(str(( int(str((self.cadena[1363:1368].to01())),2))))
		self.entry_writeData_WBID.set_text(str(( int(str((self.cadena[1368:1400].to01())),2))))
		#~ Regitros de Instruccuiones
							#~(str((int(str((self.cadena[0:10].to01 ())),2))))  
		self.label_v1.set_text(str((int(str((self.cadena[42:74].to01 ())),2))))	
		self.label_v2.set_text(str((int(str((self.cadena[74:106].to01())),2))))
		self.label_v3.set_text(str((int(str((self.cadena[106:138].to01())),2))))	
		self.label_v4.set_text(str((int(str((self.cadena[138:170].to01())),2))))
		self.label_v5.set_text(str((int(str((self.cadena[170:202].to01())),2))))
		self.label_v6.set_text(str((int(str((self.cadena[202:234].to01())),2))))
		self.label_v7.set_text(str((int(str((self.cadena[234:266].to01())),2))))
		self.label_v8.set_text(str((int(str((self.cadena[266:298].to01())),2))))
		self.label_v9.set_text(str((int(str((self.cadena[298:330].to01())),2))))
		self.label_v10.set_text(str((int(str((self.cadena[330:362].to01())),2))))
		self.label_v11.set_text(str((int(str((self.cadena[362:394].to01())),2))))
		self.label_v12.set_text(str((int(str((self.cadena[394:426].to01())),2))))
		self.label_v13.set_text(str((int(str((self.cadena[426:458].to01())),2))))
		self.label_v14.set_text(str((int(str((self.cadena[458:490].to01())),2))))
		self.label_v15.set_text(str((int(str((self.cadena[490:522].to01())),2))))
		self.label_v16.set_text(str((int(str((self.cadena[522:554].to01())),2))))
		self.label_v17.set_text(str((int(str((self.cadena[554:586].to01())),2))))
		self.label_v18.set_text(str((int(str((self.cadena[586:618].to01())),2))))
		self.label_v19.set_text(str((int(str((self.cadena[618:650].to01())),2))))
		self.label_v20.set_text(str((int(str((self.cadena[650:682].to01())),2))))
		self.label_v21.set_text(str((int(str((self.cadena[682:714].to01())),2))))
		self.label_v22.set_text(str((int(str((self.cadena[714:746].to01())),2))))
		self.label_v23.set_text(str((int(str((self.cadena[746:778].to01())),2))))
		self.label_v24.set_text(str((int(str((self.cadena[778:810].to01())),2))))
		self.label_v25.set_text(str((int(str((self.cadena[810:842].to01())),2))))
		self.label_v26.set_text(str((int(str((self.cadena[842:874].to01())),2))))
		self.label_v27.set_text(str((int(str((self.cadena[874:906].to01())),2))))
		self.label_v28.set_text(str((int(str((self.cadena[906:938].to01())),2))))
		self.label_v29.set_text(str((int(str((self.cadena[938:970].to01())),2))))
		self.label_v30.set_text(str((int(str((self.cadena[970:1002].to01())),2))))
		self.label_v31.set_text(str((int(str((self.cadena[1002:1034].to01())),2))))
		self.label_v32.set_text(str((int(str((self.cadena[1034:1066].to01())),2))))
		#~ Registros de Memoria Ram
		
def main():
	gtk.main()
	return 0

if __name__ == "__main__":
    PipeApp()
    main()


