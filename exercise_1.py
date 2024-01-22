shopping_dict = {
  "bakery": ["bread", "donuts", "buns"],
  "grocery": ["carrots", "celery", "arugula"]
}

for keys, values in shopping_dict.items():
  for i in range (len(values)):
    values[i] = values[i].capitalize()