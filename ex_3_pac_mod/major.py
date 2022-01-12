import calculations.investment

initial_value = float(input("Jaką kwotę wpłaciłeś/wpłaciłaś na start? "))
percentage = float(input("Jakie jest oprocentwoanie lokaty? "))
years = float(input("Ile lat trwa lokata? "))

final_value = calculations.investment.calculate_investment_value(initial_value, percentage, years)
print(f"Po {years} latah Twoja lokata będzie warta {final_value:.2f} ")