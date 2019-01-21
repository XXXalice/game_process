name = input()
print('こんにちは' + name + 'さん')
height = float(input()) / 100
weight = float(input())

bmi_float = weight / height ** 2
bmi_round = round(bmi_float, 1)

print('あなたのbmi数値は:' + str(bmi_round))