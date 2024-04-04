import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ControlDark
		self._button1.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(200, 32)
		self._button1.TabIndex = 0
		self._button1.Text = "Show New Form"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlLight
		self.ClientSize = System.Drawing.Size(224, 56)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "MultiForms"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from Form1 import *
		form1 = Form1(self, "Hello World!")
		from1.Show()
		self.Hide()