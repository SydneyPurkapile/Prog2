import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.ControlDark
		self._textBox1.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(181, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(223, 32)
		self._textBox1.TabIndex = 13
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ControlDark
		self._label3.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(181, 103)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(223, 23)
		self._label3.TabIndex = 12
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ControlDark
		self._label2.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 100)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(163, 23)
		self._label2.TabIndex = 11
		self._label2.Text = "Anagrams:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ControlDark
		self._label1.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(163, 23)
		self._label1.TabIndex = 10
		self._label1.Text = "Enter Text 1:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ControlDark
		self._button3.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(311, 142)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(93, 36)
		self._button3.TabIndex = 9
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ControlDark
		self._button2.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(160, 142)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(93, 36)
		self._button2.TabIndex = 8
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ControlDark
		self._button1.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 142)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(93, 36)
		self._button1.TabIndex = 7
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.SystemColors.ControlDark
		self._textBox2.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(181, 47)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(223, 32)
		self._textBox2.TabIndex = 15
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ControlDark
		self._label4.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 47)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(163, 23)
		self._label4.TabIndex = 14
		self._label4.Text = "Enter Text 2:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlLight
		self.ClientSize = System.Drawing.Size(416, 199)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "str_int_2"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		self._label3.Text = ""
		word = self._textBox1.Text.lower()
		anagram = self._textBox2.Text.lower()
		if len(word) != len(anagram):
			self._label3.Text = "False"
		else:
			for lcv in range(len(word)):
				c = word[lcv]
				index = anagram.index(c)
				if index != -1:
					anagram = anagram[0:index] + anagram[index+1:]
				else:
					self._label3.Text = "False"
		self._label3.Text = str(len(anagram) == 0)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label3.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()