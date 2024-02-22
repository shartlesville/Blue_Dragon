#weight = int(input('Enter weight: '))
weight = 41.5

# Ground Shipping
strGround = 'Ground shipping price:'
if weight <= 2:
  print(f'{strGround}\t${weight * 1.5 + 20:.2f}')
elif 2 < weight <= 6:
  print(f'{strGround}\t${weight * 3 + 20:.2f}')
elif 6 < weight <= 10:
  print(f'{strGround}\t${weight * 4 + 20:.2f}')
else:
  print(f'{strGround}\t${weight * 4.75 + 20:.2f}')

# Ground Shipping Premium
strPremium = 'Premium Ground shipping price:'
premium = '125'
print(f'{strPremium}\t${premium}')

# Drone Shipping
strDrone = 'Drone shipping cost:'
if weight <= 2:
  print(f'{strDrone}\t${weight * 4.5:.2f}')
elif 2 < weight <= 6:
  print(f'{strDrone}\t${weight * 9:.2f}')
elif 6 < weight <= 10:
  print(f'{strDrone}\t${weight * 12:.2f}')
else:
  print(f'{strDrone}\t${weight * 14.25:.2f}')

