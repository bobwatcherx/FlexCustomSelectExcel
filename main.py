from flet import *
import pandas as pd

def main(page:Page):

	# CHANGE THEMe
	page.theme_mode = "light"

	# CREATE SAMPLE DATA

	mydata = [
	{"name":"jun","job":"accounting","select":False},
	{"name":"boy","job":"programmer","select":False},
	{"name":"oop","job":"office","select":False},
	{"name":"loi","job":"precident","select":False},

	]

	# NOW CREATE TABLE AND SET ROW FROM mydata
	mytable = DataTable(
		columns=[
			DataColumn(Text("name")),
			DataColumn(Text("job")),
			DataColumn(Text("select")),
			],
			rows=[]
		)
	youselect = []

	# IF YOU CLICK SELECT CHECKBOX THEN ADD TO ARRAY
	def myselect(e):
		if e.control.value == True:
			data = {
				"name":e.control.data.controls[0].value,
				"age":e.control.data.controls[1].value,
			}

			# NOW APPEND TO youselect
			youselect.append(data)
			print(youselect)
		# AND IF YOU UNCHECKBOX THEN REMOVE NAME AND jobFROM 
		# ARRAY
		if e.control.value == False:
			data = {
				"name":e.control.data.controls[0].value,
				"age":e.control.data.controls[1].value,
			}

			# NOW APPEND TO youselect
			youselect.remove(data)
			print(youselect)
		page.update()


	# NOW ADD MYDATA TO MYTABLE
	def load_tbl():
		for x in mydata:
			mytable.rows.append(
			DataRow(
				cells=[
					DataCell(Text(x['name'])),
					DataCell(Text(x['job'])),
					DataCell(
						# CREATE CHECKBOX 
						Checkbox(value=x['select'],
							data=Row([
								Text(x['name']),
								Text(x['job']),
								]),
							on_change=myselect
							)

						),
					]
				)
			)
	def exportexcel(e):
		try:
			# NOW LOAD ARRAY youselect to datafrom
			df = pd.DataFrame.from_dict(youselect)
			# NOW SAVE TO excel
			df.to_excel("youfile.xlsx",index=False)

			# SHOW SNACKBAR IF SUCCESS
			page.snack_bar = SnackBar(
				Text("success export",size=30),
				bgcolor="green"
				)
			page.snack_bar.open = True
			# NOW REFRESH THE TABLE AND UNSELECT CHECKBOX ALL
			mytable.rows.clear()
			load_tbl()
			page.update()
		except Exception as e:
			print(e)
			page.snack_bar = SnackBar(
				Text("success export",size=30),
				bgcolor="green"
				)
			page.snack_bar.open = True
			page.update()
		page.update()







	load_tbl()

	page.add(
		Column([
		Text("custom select exprt to excel",size=30,weight="bold"),
		mytable,
		ElevatedButton("export to excel",
			on_click=exportexcel
			)	

			])
		)

flet.app(target=main)
