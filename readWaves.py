import tkinter as tk
import time
from CaChannel import  CaChannel, CaChannelException

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.create_widgets()
	
	def create_widgets(self):
		self.readRCSRFWaves1 = tk.Button(self)
		self.readRCSRFWaves1["text"] = "ReadWaves On rcsRf1!"
		self.readRCSRFWaves1["bg"] = "yellow"
		self.readRCSRFWaves1["command"] = lambda : self.readWavesFunc(num = 1)
		self.readRCSRFWaves1.pack(side="top")
		
		self.readRCSRFWaves2 = tk.Button(self)
		self.readRCSRFWaves2["text"] = "ReadWaves On rcsRf2!"
		self.readRCSRFWaves2["bg"] = "yellow"
		self.readRCSRFWaves2["command"] = lambda : self.readWavesFunc(num = 2)
		self.readRCSRFWaves2.pack(side="top")
		
		self.readRCSRFWaves3 = tk.Button(self)
		self.readRCSRFWaves3["text"] = "ReadWaves On rcsRf3!"
		self.readRCSRFWaves3["bg"] = "yellow"
		self.readRCSRFWaves3["command"] = lambda : self.readWavesFunc(num = 3)
		self.readRCSRFWaves3.pack(side="top")
		
		self.readRCSRFWaves4 = tk.Button(self)
		self.readRCSRFWaves4["text"] = "ReadWaves On rcsRf4!"
		self.readRCSRFWaves4["bg"] = "yellow"
		self.readRCSRFWaves4["command"] = lambda : self.readWavesFunc(num = 4)
		self.readRCSRFWaves4.pack(side="top")
		
		self.readRCSRFWaves5 = tk.Button(self)
		self.readRCSRFWaves5["text"] = "ReadWaves On rcsRf5!"
		self.readRCSRFWaves5["bg"] = "yellow"
		self.readRCSRFWaves5["command"] = lambda : self.readWavesFunc(num = 5)
		self.readRCSRFWaves5.pack(side="top")
		
		self.readRCSRFWaves6 = tk.Button(self)
		self.readRCSRFWaves6["text"] = "ReadWaves On rcsRf6!"
		self.readRCSRFWaves6["bg"] = "yellow"
		self.readRCSRFWaves6["command"] = lambda : self.readWavesFunc(num = 6)
		self.readRCSRFWaves6.pack(side="top")
		
		self.readRCSRFWaves7 = tk.Button(self)
		self.readRCSRFWaves7["text"] = "ReadWaves On rcsRf7!"
		self.readRCSRFWaves7["bg"] = "yellow"
		self.readRCSRFWaves7["command"] = lambda : self.readWavesFunc(num = 7)
		self.readRCSRFWaves7.pack(side="top")
		
		self.readRCSRFWaves8 = tk.Button(self)
		self.readRCSRFWaves8["text"] = "ReadWaves On rcsRf8!"
		self.readRCSRFWaves8["bg"] = "yellow"
		self.readRCSRFWaves8["command"] = lambda : self.readWavesFunc(num = 8)
		self.readRCSRFWaves8.pack(side="top")
		
		self.quit = tk.Button(self, text="Quit", fg="red", command=root.destroy)
		self.quit.pack(side="bottom")
	def readWavesFunc(self, num):
		try:
			#初始化参数
			chan = CaChannel('rcsRf'+str(num)+':wf_amp_skew.VALA')
			chan.searchw()
			
			#parmFile = open(r'C:\Users\HP\Desktop\Waves\ampSkew'+str(num)+'.txt', 'w', encoding='utf-8')
			parmFile = open(r'ampSkew'+str(num)+'.txt', 'w', encoding='utf-8')
			parmFile.write('%s\n'%(chan.getw()))
			parmFile.close()
			
			chan = CaChannel('rcsRf'+str(num)+':wf_gridTunningError.VALA')
			chan.searchw()
			
			parmFile = open(r'gridTunningError'+str(num)+'.txt', 'w', encoding='utf-8')
			parmFile.write('%s\n'%(chan.getw()))
			parmFile.close()
			
			chan = CaChannel('rcsRf'+str(num)+':wf_cavTunningError.VALA')
			chan.searchw()
			
			parmFile = open(r'cavTunningError'+str(num)+'.txt', 'w', encoding='utf-8')
			parmFile.write('%s\n'%(chan.getw()))
			parmFile.close()
			
			chan = CaChannel('rcsRf'+str(num)+':wf_phaseError.VALA')
			chan.searchw()
			
			parmFile = open(r'phaseError'+str(num)+'.txt', 'w', encoding='utf-8')
			parmFile.write('%s\n'%(chan.getw()))
			parmFile.close()
			
			chan = CaChannel('rcsRf'+str(num)+':wf_beamPhase.VALA')
			chan.searchw()
			
			parmFile = open(r'beamPhase'+str(num)+'.txt', 'w', encoding='utf-8')
			parmFile.write('%s\n'%(chan.getw()))
			parmFile.close()
			
			chan = CaChannel('rcsRf'+str(num)+':wf_cavBias.VALA')
			chan.searchw()
			
			parmFile = open(r'cavBias'+str(num)+'.txt', 'w', encoding='utf-8')
			parmFile.write('%s\n'%(chan.getw()))
			parmFile.close()
			
			chan = CaChannel('rcsRf'+str(num)+':wf_cavBiasFF.VALA')
			chan.searchw()
			
			parmFile = open(r'cavBiasFF'+str(num)+'.txt', 'w', encoding='utf-8')
			parmFile.write('%s\n'%(chan.getw()))
			parmFile.close()
			
			chan = CaChannel('rcsRf'+str(num)+':wf_gridBias.VALA')
			chan.searchw()
			
			parmFile = open(r'gridBias'+str(num)+'.txt', 'w', encoding='utf-8')
			parmFile.write('%s\n'%(chan.getw()))
			parmFile.close()
			
			chan = CaChannel('rcsRf'+str(num)+':wf_cavAmp.VALA')
			chan.searchw()
			
			parmFile = open(r'cavAmp'+str(num)+'.txt', 'w', encoding='utf-8')
			parmFile.write('%s\n'%(chan.getw()))
			parmFile.close()
			
			chan = CaChannel('rcsRf'+str(num)+':wf_gridAmp.VALA')
			chan.searchw()
			
			parmFile = open(r'gridAmp'+str(num)+'.txt', 'w', encoding='utf-8')
			parmFile.write('%s\n'%(chan.getw()))
			parmFile.close()
			
			chan = CaChannel('rcsRf'+str(num)+':wf_frontAmp.VALA')
			chan.searchw()
			
			parmFile = open(r'frontAmp'+str(num)+'.txt', 'w', encoding='utf-8')
			parmFile.write('%s\n'%(chan.getw()))
			parmFile.close()
			
			chan = CaChannel('rcsRf'+str(num)+':wf_beamAmp.VALA')
			chan.searchw()
			
			parmFile = open(r'beamAmp'+str(num)+'.txt', 'w', encoding='utf-8')
			parmFile.write('%s\n'%(chan.getw()))
			parmFile.close()
			
			#延时10s
			time.sleep(20)
			print("delay 20 s")			

		except CaChannelException as e:
			print(e)
root = tk.Tk()
app = Application(master = root)
app.mainloop()