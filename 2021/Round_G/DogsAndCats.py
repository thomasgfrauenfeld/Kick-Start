"""
Problem

You work for an animal shelter and you are responsible for feeding the animals. You already
prepared D portions of dog food and C portions of cat food.

There are a total of N animals waiting in a line, some of which are dogs and others are cats. It
might be possible that all the animals in the line are dogs or all the animals are cats. A string S
of N characters C and D represents the order of cats and dogs in the line. The i-th character is
equal to C if the i-th animal in the line is a cat. Similarly, the i-th character is equal to D if
the i-th animal in the line is a dog.

The animals are fed in the order they stay in the line. Each dog eats exactly 1 portion of dog food
and similarly each cat eats exactly 1 portion of cat food. Moreover, you have extra portions of cat
food. Every time a dog eats food, you bring M extra portions of cat food for cats.

Animals have to be fed in the order they wait in line and an animal can only eat if the animal
before it has already eaten. That means that if you run out of dog (or cat food) portions and a dog
(or a cat) is about to get fed, the line will not move, as all the animals will wait patiently.

You need to determine if in this scenario all the dogs in the line will be fed. Note that this
means that some cats might remain in the line, but worry not, you will eventually feed them later!

Input

The first line of the input gives the number of test cases, T. T test cases follow.

The first line of each test case contains four integers N, D, C, and M: the number of animals, the
initial number of dog food portions, the initial number of cat food portions, and the additional
portions of cat food that we add after a dog eats a portion of dog food, respectively.

The next line contains a string S of length N representing the arrangement of animals.

Output

For each test case, output one line containing Case #x: y, where x is the test case number 
(starting from 1) and y is YES if all the dogs will be fed and NO otherwise.

Limits

Memory limit: 1 GB.
1 <= T <= 100.
1 <= N <= 10^4.
0 <= D, C <= 10^6.
S consists of only characters C and D.

Test Set 1

Time limit: 20 seconds.
M = 0

Test Set 2

Time limit: 40 seconds.
0 <= M <= 10^6.

Sample

Note: there are additional samples that are not run on submissions down below.

Sample Input        Sample Output

3                   Case #1: YES
6 10 4 0            Case #2: YES
CCDCDD              Case #3: NO
4 1 2 0
CCCC
4 2 1 0
DCCD

In Sample Case #1, there are 10 portions of dog food and 4 portions of cat food.

1. The first two animals are cats, so after they eat, 2 portions of cat food remain.
2. Then a dog eats one portion of dog food. Now, there are 9 portions of dog food left.
3. Next, a cat eats a portion of cat food, reducing the number of portions of cat food to 1.
4. The last two animals are dogs and they each eat one portion of dog food.

So in this case, all the dogs are able to eat.

In Sample Case #2, there are no dogs, Hence, all (zero) dogs will be able to eat trivially.

In Sample Case #3, the cat before the second dog will not be able to eat because there will not be
enough portions of cat food. Hence, the second dog will also not eat.

Additional Sample - Test Set 2

The following additional sample fits the limits of Test Set 2. It will not be run against your
submitted solutions.

Sample Input        Sample Output

2                   Case #1: YES
12 4 2 2            Case #2: NO
CDCCCDCCDCDC
8 2 1 3
DCCCCCDC

In Sample Case #1, 2 portions of cat food appear whenever a dog eats a portion of dog food.

1. After the first cat eats, there is 1 portion of cat food left.
2. Then a dog eats, leaving 3 portions of dog food and 3 portions of cat food.
3. After the next 3 cats eat, there are 3 portions of dog food and 0 portions of cat food remaining.
4. Then a dog eats, leaving 2 portions of dog food and 2 portions of cat food.
5. After the next 2 cats eat food, there are 2 portions of dog food and 0 portions of cat food left.
6. Now a dog eats, leaving 1 portion of dog food and 2 portions of cat food.
7. Next a cat eats, leaving 1 portion of dog food and 1 portion of cat food.
8. The last dog eats the remaining portion of dog food. 

So in this case, all the dogs are able to eat.

In Sample Case #2, the cat before the second dog will not be able to eat because there will not be
enough portions of cat food.
"""

num_tests = int(input())

for i in range(num_tests):
    parameters = input().split(" ")
    num_animals = int(parameters[0])
    dog_food_portions = int(parameters[1])
    cat_food_portions = int(parameters[2])
    cat_food_multiplier = int(parameters[3])
    animals = list(input())
    answer = 'YES'

    for j in range(num_animals):
        if 'D' not in animals:
            break
            
        if dog_food_portions == 0:
            answer = 'NO'
            break

        current_animal = animals.pop(0)

        if current_animal == 'D':
            dog_food_portions -= 1
            cat_food_portions += cat_food_multiplier
        elif current_animal == 'C':
            if cat_food_portions == 0:
                answer = 'NO'
                break
            cat_food_portions -= 1
    
    if answer == 'YES':
        print("Case #{}: YES".format(i + 1))
    else:
        print("Case #{}: NO".format(i + 1))