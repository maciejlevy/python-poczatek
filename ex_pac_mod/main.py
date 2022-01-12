import formula

running_distance = float(input("Ile km przebiegłeś/przebiegłaś? "))
running_time = float(input("Ile godzin Ci to zajęło? "))

avg_speed = formula.avg_speed(running_distance, running_time)
print(f"Twoja średnia prędkość biegu to {avg_speed} km/h")