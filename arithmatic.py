import re

class Arithmetic:
	@staticmethod
	def Format_Formater(expression, solve = False):
		try:
			for exp in expression:
				Num_1 = re.findall('^[0-9]+', expression);
				operator = re.findall('[\+\-\*\/]', expression);
				Num_2 = re.findall('[0-9]+$', expression);
			
				number_1 = str(Num_1[0]);
				number_2 = str(Num_2[0]);

			ans = "";
			
			operators = "";
			if operator[0] == "+":
				operators = "+";
				ans = str(int(number_1) + int(number_2));
				
			elif operator[0] == "-":
				operators = "-";
				ans = str(int(number_1) - int(number_2));
			
			elif operator[0] == "*":
				operators = "x"; 
				ans = str(int(number_1) * int(number_2));

			elif operator[0] == "/":		
				operators = "%";
				ans = str(int(number_1) / int(number_2));
			else:
				print("Invalid Operator")	
			
			ans = round(float(ans));
			ans = str(ans);

			arangedNum_1 = number_1.rjust(len(number_1) + 10);
			aranged_Operators = operators.rjust(len(arangedNum_1) - len(number_1) - 2);

			le_ao = len(aranged_Operators);
			arangedNum_2 = number_2.rjust(len(number_1) + 10 - le_ao);

			ara_ans = ans.rjust(len(number_1) + 10);
			dash = "";
			for d in range(len(number_1) + 3):
				dash += "-"; 

			newDashes = dash.rjust(len(number_1) + 10);
			if solve == False and len(number_1) <= 5 and len(number_2) <= 5:
				return arangedNum_1 + "\n" + aranged_Operators + arangedNum_2 + "\n" + newDashes + "\n\n";
			if solve == True and len(number_1) <= 5 and len(number_2) <= 5:
				return arangedNum_1 + "\n" + aranged_Operators + arangedNum_2 + "\n" + newDashes + "\n" + ara_ans + "\n\n";	
			if len(number_1) > 5 or len(number_2) > 5:
				return "Can not arrange or calculate more than 5 characters";
		except:
			print("An error occured");
				
print(Arithmetic.Format_Formater("134*3", True));



