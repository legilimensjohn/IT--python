def geberate_truth_table (expression, val_p, val_q):
  header = ['p', 'q', expression]
  print("        | ".join(header))

for p, q in zip(val_p, val_q):
  if 'not q' in expression:
    result = not q
  else:
    result = evaluation(expression, {'p': p, 'q': q})

print(f"{p}          |    {q}        |   {result}")

logical_expression = input ("Kindly input logical expression: ")
val_p = [True, True, False, False]
val_q = [True, False, True, False]

generate_truth_table (logical_expression, val_p, val_q)
