shopping_dict = {
  "bakery": ["bread", "donuts", "buns"],
  "grocery": ["carrots", "celery", "arugula"]
}

for keys, values in shopping_dict.items():
  for i in range (len(values)):
    values[i] = values[i].capitalize()
  print(f"Idę do {keys.capitalize()} kupuję tu następujące rzeczy {values}")

sum = len(shopping_dict["bakery"]) + len(shopping_dict["grocery"])

print(f"Suma to {sum}")