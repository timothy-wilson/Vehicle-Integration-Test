#Python
dict={105:"FizzFizzyBuzz",35:"FizzyBuzz",21:"FizzBuzz",
      15:"FizzFizzy",7:"Buzz",5:"Fizzy",3:"Fizz"}
text=""

for i in range(1,251):
    taken=True
    for j in dict:
        if i%j == 0 and taken:
            text += dict[j]+" "
            taken = False
    if taken:
        text += str(i)+" "

print(text)
