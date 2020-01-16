class CsvReader():
	def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.header = header
	def __enter__(self):
		try:
			self.f = open(self.filename, 'r')
		except FileNotFoundError:
			print("file not found")
			self.f = None
			return None
		if self.check() == False:
			print("corrupted")
			return None
		return self

	def __exit__(self, type, value, traceback):
		self.f.close()

	def check(self):
		n = len(self.f.readline().split(self.sep))
		for m in self.f.readlines():
			if m == "": break
			if len([s for s in m.split(self.sep) if s.strip() != ""]) != n: return False
		return True

	def getdata(self):
		lst2 = []
		if self.f != None:
			self.f.seek(0)
			self.f.readline()
			return [ [s.strip() for s in l] for l in [ln.split(self.sep) for ln in self.f.readlines() if ln != "\n"]
]
	def getheader(self):
		if self.f != None:
			self.f.seek(0)
			return [s.strip() for s in self.f.readline().split(self.sep)]

with CsvReader("good.csv") as f:
	header = f.getheader()
	data = f.getdata()
	print(header)
	for d in data:
		print(d)
with CsvReader("bad.csv") as f:
	if f == None:
		print("boo")
	
